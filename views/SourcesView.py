from views.BaseView import BaseView
from flask import session, request
from models.Source import Source
from models.User import User
import json


class SourcesView(BaseView):
    def __init__(self, template_name, title="Fontes"):
        super().__init__(template_name, title)

    def get(self, **kwargs):
        sources = Source.get({"user.username": session["user"]["username"],
                              "user.password": session["user"]["password"]})
        kwargs.__setitem__("sources", sources)
        kwargs.__setitem__("user", session["user"])
        return super().get(**kwargs)

    def post(self, **kwargs):
        status = True
        user = User.get({"username": session["user"]["username"],
                         "password": session["user"]["password"]})[0]
        try:
            count = 1
            while True:
                obj = f"source-input{count}"
                new_source = Source(request.form[obj], user)
                status = new_source.save()
                if not status:
                    return json.dumps({"result": status})
                count += 1
        except KeyError:
            return json.dumps({"result": status})
