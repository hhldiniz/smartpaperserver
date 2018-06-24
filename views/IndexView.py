from views.BaseView import BaseView
from flask import session, request
from models.User import User


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name, "Index")

    def get(self, **context):
        try:
            user = session["user"]
            context.__setitem__("user", user)
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)

    def post(self, **context):
        username = request.form["username"]
        password = request.form["password"]
        user = User(username=username, password=password)
        user = user.get({"username": username, "password": password})
        context.__setattr__("user", user)
        return super().post(**context)
