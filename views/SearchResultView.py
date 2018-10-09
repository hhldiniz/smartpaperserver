from flask import session, request

from views.BaseView import BaseView


class SearchResultView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name, "Resultados")

    def get(self, **context):
        try:
            user = session["user"]
            context.__setitem__("user", user)
            try:
                search_result = request.headers["search_result"]
                context.__setitem__("search_result", search_result)
            except KeyError:
                context.__setitem__("search_result", None)
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)
