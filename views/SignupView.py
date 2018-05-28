from views.BaseView import BaseView
from flask import request, render_template
from models.User import User


class SignupView(BaseView):
    def __init__(self, template_name, title="Cadastro"):
        super().__init__(template_name, title)

    def post(self, **kwargs):
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        user = User(name, email, username, password)
        if user.save():
            kwargs.__setitem__("user", user)
        return render_template(self.get_template_name(), **kwargs)
