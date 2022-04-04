import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos


render = web.template.render("mvc/views/admin/",base="layout_user_view")



class User_view_admin:
    def GET(self, localId):
        try: # prueba el codigo
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            user = db.child("usuario_creado").child(localId).get()
            return render.user_view_admin(user)
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
