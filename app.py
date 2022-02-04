import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/login', 'Login',  #ulrs o raices de las diferentes páginas html que vamos a utlizar
    '/registrar', 'Registrar',
    '/bienvenida', 'Bienvenido',
)
app = web.application(urls, globals())#configura las urls en la aplicacion web
render = web.template.render('views') # configura la carpeta donde estan las vistas (archivos html)


class Bienvenido:
    def GET(self):
        return render.bienvenida() # nos devuleve al render de nuestro html bienvenida


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
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            auth = firebase.auth()  # se inicializa el metodo de autentificación
            formulario = web.input() # se crea una variable formulario para recibir los datos del login
            email = formulario.email # se crea una varible donde se guardara los datos ingresados en el formulario
            password= formulario.password # se crea una varible donde se guardara los datos ingresados en el formulario
            print(email,password)  # se imprime el email y contraseña para rectificar internamente
            verificacion_usuario = auth.sign_in_with_email_and_password(email, password) # se crea una varible donde se verificara si el email y la contraseña con correctas
            print(verificacion_usuario)  # nos devuelve la verificación de esta
            return web.seeother("bienvenida") # nos devuelve al html bievenida
        except Exception as error: # atrapa el error a arreglar
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # obtiene el json de error
            message = error['message'] # obtiene el mensaje de error
            if message == "INVALID_PASSWORD" :
                return render.login("la contraseña que ingreso no es válida , intente de nuevo ") 
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
           # se muestra nuevamente login mostrando el mensaje de error

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
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            auth = firebase.auth()  # se inicializa el metodo de autentificación
            formulario = web.input() # se crea una variable formulario para recibir los datos del registrar.html
            email = formulario.email  # se crea una varible donde se guardara los datos ingresados en el formulario
            password= formulario.password  # se crea una varible donde se guardara los datos ingresados en el formulario
            print(email,password) # se imprime el email y contraseña para rectificar internamente
            usuario_creado = auth.create_user_with_email_and_password(email, password) # se crea una varible donde se verificara si el email y la contraseña son correctas para crear un nuevo usuario
            print(usuario_creado) # nos devuelve la verificación de esta
            return web.seeother("login")# nos devuelve el login
        except Exception as error: # atrapa el error a arreglar
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # se obtiene el json de error
            message2 = error['message'] # se obtiene el mensaje de error
            if message2 == "EMAIL_EXISTS" :
                return render.registrar("el correo que quiso ingresar ya está registrado, porfavor pruebe con otros datos ") 
            print("Error Login.POST: {}".format(message2)) # se imprime el message enviado por firebase
        

if __name__ == "__main__":
    web.config.debug = True # activa o desactiva el modo de repuracion de firebase
    app.run()