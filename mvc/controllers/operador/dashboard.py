import web
import app


render = web.template.render("mvc/views/operador/",base="layout_dashboar_op")

class Dashboard:
    def GET(self):
        return render.dashboard()