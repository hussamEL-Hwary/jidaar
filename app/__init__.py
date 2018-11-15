from helper import *
from career.view import career_view as caca
from home.view import home_view as hv
from clients.view import client_view
from auth.view import auth_view
from project.view import project_view
from admin.view import admin_view

app.register_blueprint(caca)
app.register_blueprint(hv)
app.register_blueprint(client_view)
app.register_blueprint(auth_view)
app.register_blueprint(project_view)
app.register_blueprint(admin_view)
