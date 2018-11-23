from abc import ABC

from flask import request, render_template
from flask.views import View


class BaseView(View, ABC):
    def __init__(self, template_name, title):
        self.__template_name = template_name
        self.__title = title

    def get_template_name(self):
        return self.__template_name

    def set_title(self, title):
        self.__title = title

    def dispatch_request(self):
        if request.method == "GET":
            return self.get(title=self.__title)
        elif request.method == "POST":
            return self.post(title=self.__title)

    def get(self, **kwargs):
        return render_template(self.__template_name, **kwargs)

    def post(self, **kwargs):
        return render_template(self.__template_name, **kwargs)

    @staticmethod
    def get_post_data(property_name):
        if property_name in request.form:
            return request.form[property_name]
        if property_name in request.args:
            return request.args[property_name]
        if property_name in request.files:
            return request.files[property_name]
