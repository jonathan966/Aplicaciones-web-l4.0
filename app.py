import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/', 'mvc.controllers.public.index.Index',  #ulrs o raices de las diferentes páginas html que vamos a utlizar
    '/login', 'mvc.controllers.public.login.Login',
    '/registrar','mvc.controllers.public.registrar.Registrar',
    '/user_list', 'mvc.controllers.public.userlist.Userlist',
    '/user_view/(.*)', 'mvc.controllers.public.userview.Userview',
    '/user_list_admin', 'mvc.controllers.admin.user_list_admin.User_list_admin',
    '/update/(.*)','mvc.controllers.public.update.Update',
    '/index','mvc.controllers.public.bienvenida.Bienvenida',
    '/bienvenida_operador','mvc.controllers.operador.bienvenida.Bienvenida',
    '/bienvenida','mvc.controllers.public.bienvenida.Bienvenida',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
    '/dashboard','mvc.controllers.operador.dashboard.Dashboard',
    '/bienvenida_admin','mvc.controllers.admin.bienvenida_admin.Bienvenida_admin',
    
)
app = web.application(urls, globals())#configura las urls en la aplicacion web
wsgiapp = app.wsgifunc()







if __name__ == "__main__":
    web.config.debug = True # activa o desactiva el modo de repuracion de firebase
    app.run()