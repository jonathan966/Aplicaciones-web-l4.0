import web
import app


render = web.template.render("mvc/views/operador/",base="layout_dashboar_op")

class Dashboard:
    def GET(self):
        if ( web.cookies().get('localid')) == "": # se pone una condicional si localid es igual a vacio que esta nos vuelva a mandar a la pagina login
            return web.seeother("/index")
        else :
         return render.dashboard() # nos devuelve el render bienvendia
