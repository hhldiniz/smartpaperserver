import json

from flask import request

from models.User import User
from views.BaseView import BaseView


class SignupView(BaseView):
    def __init__(self, template_name, title="Cadastro"):
        super().__init__(template_name, title)

    def post(self, **kwargs):
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        try:
            photo = request.files["photo"]
        except KeyError:
            print("No photo")
            photo = ""
        user = User(name, email, username, password, photo)
        return json.dumps({"result": user.save()})
