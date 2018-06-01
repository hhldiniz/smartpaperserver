from views.BaseView import BaseView


class SourcesView(BaseView):
    def __init__(self, template_name, title="Fontes"):
        super().__init__(template_name, title)
