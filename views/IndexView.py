from views.BaseView import BaseView
from flask import session, render_template, request
from models.User import User


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name, "Index")

    def get(self, **kwargs):
        try:
            user = session["user"]
            kwargs.__setitem__("user", user)
        except KeyError:
            kwargs.__setitem__("user", None)
        return render_template(self.get_template_name(), **kwargs)

    def post(self, **kwargs):
        username = request.form["username"]
        password = request.form["password"]
        user = User(username=username, password=password)
        user = user.get({"username": username, "password": password})
        kwargs.__setattr__("user", user)
        return render_template(self.get_template_name(), **kwargs)
