from views.BaseView import BaseView
from flask import render_template, session, request
from models.Source import Source
from models.User import User


class SourcesView(BaseView):
    def __init__(self, template_name, title="Fontes"):
        super().__init__(template_name, title)

    def get(self, **kwargs):
        sources = Source.get({"user.username": session["user"]["username"],
                              "user.password": session["user"]["password"]})
        kwargs.__setitem__("sources", sources)
        kwargs.__setitem__("user", session["user"])
        return render_template(self.get_template_name(), **kwargs)

    def post(self, **kwargs):
        url = request.form["url"]
        user = User.get({"username": session["user"]["username"],
                         "password": session["user"]["password"]})[0]
        source = Source(url, user)
        return source.save()
