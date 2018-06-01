from views.BaseView import BaseView


class AboutView(BaseView):
    def __init__(self, template_name, title="Sobre"):
        super().__init__(template_name, title)
