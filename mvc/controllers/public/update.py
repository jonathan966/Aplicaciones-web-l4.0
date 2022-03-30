
import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos




render = web.template.render("mvc/views/public/",base="layout")



class Update:
    def GET(self, localId):
        try: # prueba el codigo
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            user = db.child(" usuario_creado ").child(localId).get()
            return render.update(user)
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio

    def POST(self, localId):
       firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
       db = firebase.database()  # se inicializa el metodo de base de datos en firebase
       formulario1 = web.input() # se crea una variable formulario para recibir los datos del registrar.html
       print(formulario1)
       nombre = formulario1.nombre # se crea la variable nombre donde se guardara los datos ingresados en el formulario
       telefono = formulario1.telefono  # se crea la variable telefono donde se guardara los datos ingresados en el formulario
       email = formulario1.email  # se crea la variable email donde se guardara los datos ingresados en el formulario
       level = formulario1.level
       localid = formulario1.localid 
       # se hace uso de la base de datos de fire base donde se mostraran los soguiientes campos
       data = { "nombre": nombre,  
        "telefono" : telefono,
        "email" : email,
        "level" : level
       }
       results = db.child("usuario_creado").child(localid).update(data)
       return web.seeother("update")# nos devuelve el login
