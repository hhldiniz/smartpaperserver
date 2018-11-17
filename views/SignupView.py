import json

from flask import request
from werkzeug.datastructures import FileStorage

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
            photo = FileStorage(open("./files/blank-profile-picture-973460_640.png", "rb"))
        user = User(name, email, username, password, photo)
        return json.dumps({"result": user.save()})
