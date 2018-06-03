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
        photo = request.files["photo"]
        user = User(name, email, username, password, photo)
        return json.dumps({"result": user.save()})
