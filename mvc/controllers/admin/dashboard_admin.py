import web
import app


render = web.template.render("mvc/views/admin/",base="layout_dashboard_admin")

class Dashboard_admin:
    def GET(self):
        return render.dashboard_admin()