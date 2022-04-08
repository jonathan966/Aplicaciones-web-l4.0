import web
import app


render = web.template.render("mvc/views/public/",base="layout_index")

class Index:
    def GET(self):
        return render.index()# se renderizara el html de index