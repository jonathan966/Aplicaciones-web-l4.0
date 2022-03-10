import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/', 'Login',  #ulrs o raices de las diferentes páginas html que vamos a utlizar
    '/registrar', 'Registrar',
    '/user_list', 'Userlist',
    '/user_view/(.*)', 'Userview',
    '/update/(.*)', 'Update',
    '/bienvenida', 'Bienvenido',
    '/logout', 'Logout',
    '/recuperar', 'Recuperar',
    
)
app = web.application(urls, globals())#configura las urls en la aplicacion web
wsgiapp = app.wsgifunc()
render = web.template.render('views', base='layout') # configura la carpeta donde estan las vistas (archivos html)


class Recuperar:
    def GET(self):
        return render.recuperar()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
        auth = firebase.auth() # se inicializa el metodo de autentificación
        formulario = web.input() # se crea una variable formulario para recibir los datos del login
        email = formulario.email # se crea una varible donde se guardara los datos ingresados en el formulario
        result = auth.send_password_reset_email(email)  # se crea una varible donde se pondra resetar la contraseña
        return web.seeother("/") # nos devuelve al html bievenida
      

class Logout:
    def GET(self):
        web.setcookie('localid', None) # configuramos la cookie para que cuando el usuario presione el logout , la cookie cambie a un valor vacio asi limitando su acesso si es que quisieran entrar otra vez a la raiz
        return web.seeother("/")  # nos devuelve el login


class Bienvenido:
    def GET(self):
        if ( web.cookies().get('localid')) == "": # se pone una condicional si localid es igual a vacio que esta nos vuelva a mandar a la pagina login
            return web.seeother("/")
        else :
            return render.bienvenida() # nos devuelve el render bienvendia


class Userview:
    def GET(self, localId):
        try: # prueba el codigo
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            user = db.child(" usuario_creado ").child(localId).get()
            return render.user_view(user)
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio


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

class Userlist:
    def GET(self):
        try: # prueba el codigo
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            users = db.child("usuario_creado").get()
            return render.user_list(users)
        except Exception as error: # atrapa el error a arreglar
            message = "Error en el sistema" # se alamacena un mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
    



class Login:
    def GET(self):
        try: # prueba el codigo
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
            local_id = ( verificacion_usuario ['localId']) # se crea la varible donde se almacenara el localid
            web.setcookie('localid', local_id) # confguramos nuestra cookie con el nombre y el valor 
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
            db = firebase.database()  # se inicializa el metodo de base de datos en firebase
            formulario = web.input() # se crea una variable formulario para recibir los datos del registrar.html
            nombre = formulario.nombre # se crea la variable nombre donde se guardara los datos ingresados en el formulario
            telefono = formulario.telefono  # se crea la variable telefono donde se guardara los datos ingresados en el formulario
            email = formulario.email  # se crea la variable email donde se guardara los datos ingresados en el formulario
            password= formulario.password  # se crea la variable password donde se guardara los datos ingresados en el formulario
            usuario_creado = auth.create_user_with_email_and_password(email, password) # se crea una varible donde se verificara si el email y la contraseña son correctas para crear un nuevo usuario
            print("localid :" ,usuario_creado ['localId'] ) # se imprimeel localid
            data = { "nombre": nombre,  # se hace uso de la base de datos de fire base donde se mostraran los soguiientes campos
                "telefono" : telefono,
                "email" : email
            }
            results = db.child("usuario_creado").child(usuario_creado ['localId'] ).set(data) # nos dara la creacion de un hijo en firebase
            return web.seeother("/")# nos devuelve el login
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