from views.BaseView import BaseView
from flask import request
from models.User import User
import json


class SignupView(BaseView):
    def __init__(self, template_name, title="Cadastro"):
        super().__init__(template_name, title)

    def post(self, **kwargs):
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        user = User(name, email, username, password)
        return json.dumps({"result": user.save()})
