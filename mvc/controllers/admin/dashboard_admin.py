import web
import app


render = web.template.render("mvc/views/admin/",base="layout_dashboard_admin")

class Dashboard_admin:
    def GET(self):
        if ( web.cookies().get('localid')) == "": # se pone una condicional si localid es igual a vacio que esta nos vuelva a mandar a la pagina login
            return web.seeother("/index")
        else :
         return render.dashboard_admin() # nos devuelve el render bienvendia   