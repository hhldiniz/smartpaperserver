from flask.views import View
from flask import request, render_template


class BaseView(View):
    def __init__(self, template_name, title):
        self.__template_name = template_name
        self.__title = title

    def get_template_name(self):
        return self.__template_name

    def dispatch_request(self):
        if request.method == "GET":
            return self.get(title=self.__title)
        elif request.method == "POST":
            return self.post(title=self.__title)

    def get(self, **kwargs):
        return render_template(self.__template_name, **kwargs)

    def post(self, **kwargs):
        return render_template(self.__template_name, **kwargs)
