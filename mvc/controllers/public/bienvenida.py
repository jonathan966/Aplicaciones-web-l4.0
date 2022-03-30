

import web # se importa la libreria de web.py para hacer sus del framework




render = web.template.render("mvc/views/public/",base="layout")


class Bienvenida:
    def GET(self):
        if ( web.cookies().get('localid')) == "": # se pone una condicional si localid es igual a vacio que esta nos vuelva a mandar a la pagina login
            return web.seeother("/")
        else :
            return render.bienvenida() # nos devuelve el render bienvendia

