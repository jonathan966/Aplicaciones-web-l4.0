import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/', 'mvc.controllers.public.index.Index',  #ulrs o raices de las diferentes páginas html que vamos a utlizar
    '/login', 'mvc.controllers.public.login.Login',
    '/user_list_admin', 'mvc.controllers.admin.user_list_admin.User_list_admin',#true
    '/add_users_admin', 'mvc.controllers.admin.add_users_admin.Add_users_admin',#true
    '/bienvenida_admin','mvc.controllers.admin.bienvenida_admin.Bienvenida_admin',#true
    '/dashboard_admin','mvc.controllers.admin.dashboard_admin.Dashboard_admin', #true
    '/update_users_admin/(.*)','mvc.controllers.admin.update_users_admin.Update_users_admin',#false
    '/user_view_admin/(.*)','mvc.controllers.admin.user_view_admin.User_view_admin',#fasle
    '/on_off_count_admin/(.*)','mvc.controllers.admin.on_off_count_admin.On_off_count_admin',#false
    '/bienvenida_operador','mvc.controllers.operador.bienvenida.Bienvenida',
    '/dashboard','mvc.controllers.operador.dashboard.Dashboard',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',   
)
app = web.application(urls, globals())#configura las urls en la aplicacion web
wsgiapp = app.wsgifunc()







if __name__ == "__main__":
    web.config.debug = True # activa o desactiva el modo de repuracion de firebase
    app.run()