import json

from werkzeug.datastructures import FileStorage

from models.User import User
from views.BaseView import BaseView


class SignupView(BaseView):
    def __init__(self, template_name, title="Cadastro"):
        super().__init__(template_name, title)

    def post(self, **kwargs):
        name = self.get_post_data("name")
        email = self.get_post_data("email")
        username = self.get_post_data("username")
        password = self.get_post_data("password")
        try:
            photo = self.get_post_data("photo")
            if type(photo) == str:
                photo = FileStorage(open("./files/blank-profile-picture-973460_640.png", "rb"))
        except KeyError:
            photo = FileStorage(open("./files/blank-profile-picture-973460_640.png", "rb"))
        user = User(name, email, username, password, photo)
        return json.dumps([{"result": user.save()}])

