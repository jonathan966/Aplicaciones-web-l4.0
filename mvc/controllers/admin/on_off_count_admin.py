import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos




render = web.template.render("mvc/views/admin/",base="layout_on_off_count_admin")



class On_off_count_admin:
    def GET(self, localId): 
        try: # prueba el codigo
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            user = db.child("usuario_creado").child(localId).get()
            return render.on_off_count_admin(user)
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio

    def POST(self, localId):
       firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
       db = firebase.database()  # se inicializa el metodo de base de datos en firebase
       formulario1 = web.input() # se crea una variable formulario para recibir los datos del registrar.html
       print(formulario1)
       nombre = formulario1.nombre # se crea la variable nombre donde se guardara los datos ingresados en el formulario
       level = formulario1.level # se crea la variable level donde se guardara los datos ingresados en el formulario
       email = formulario1.email # se crea la variable email donde se guardara los datos ingresados en el formulario
       estado = formulario1.estado # se crea la variable estado donde se guardara los datos ingresados en el formulario
       data = { "nombre": nombre,  
        "email" : email,
        "level" : level,
        "estado" : estado
       }
       results = db.child("usuario_creado").child(localId).update(data)# se hace utilización de funcion la base en firebase para actualizar en este caso
       return web.seeother("/user_list_admin")
