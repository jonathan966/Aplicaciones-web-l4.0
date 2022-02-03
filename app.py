import web
import pyrebase
import firebase_config as token
import json

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
        return render.login()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        password= formulario.password
        print(email,password) 
        verificacion_usuario = auth.sign_in_with_email_and_password(email, password)
        print(verificacion_usuario)
        return render.login()

class Registrar:
    def GET(self):
        return render.registrar()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        password= formulario.password
        print(email,password) 
        usuario_creado = auth.create_user_with_email_and_password(email, password)
         
        print(usuario_creado)
        return render.registrar()

if __name__ == "__main__":
    app.run()