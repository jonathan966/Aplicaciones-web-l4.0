import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/login', 'Login',
    '/registrar', 'Registrar',
    '/bienvenida', 'Bienvenido',
)
app = web.application(urls, globals())
render = web.template.render('views')


class Bienvenido:
    def GET(self):
        return render.bienvenida()


class Login:
    def GET(self):
        try: # prueba el  codigo
            message = None # se crear una variable para el mensaje de error
            return render.login(message) # renderiza la pagina login.html con el mensaje
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.login(message) # se renderiza nuevamente login con el mensaje de error

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            formulario = web.input()
            email = formulario.email
            password= formulario.password
            print(email,password) 
            verificacion_usuario = auth.sign_in_with_email_and_password(email, password)
            print(verificacion_usuario)
            return web.seeother("bienvenida")
        except Exception as error: # atrapa el error a arreglar
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600) # se resetea el localID en la cookie
            return render.login(message) # se muestra nuevamente login mostrando el mensaje de error

class Registrar:
    def GET(self):
        try: # prueba el  codigo
            message2 = None # se crear una variable para el mensaje de error
            return render.registrar(message2) # renderiza la pagina login.html con el mensaje
        except Exception as error: # atrapa el error a arreglar
            message2 = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.registrar(message2) # se renderiza nuevamente login con el mensaje de error

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            formulario = web.input()
            email = formulario.email
            password= formulario.password
            print(email,password) 
            usuario_creado = auth.create_user_with_email_and_password(email, password)
            print(usuario_creado)
            return web.seeother("login")
        except Exception as error: # atrapa el error a arreglar
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message2 = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message2)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600) # se resetea el localID en la cookie
            return render.registrar(message2) # se muestra nuevamente login mostrando el mensaje de error
        

if __name__ == "__main__":
    web.config.debug = True # Activa o desactiva el modo de repuracion de firebase
    app.run()