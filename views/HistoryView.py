from views.BaseView import BaseView
from flask import render_template, session
from models.Article import Article


class HistoryView(BaseView):
    def __init__(self, template_name, title="Histórico"):
        super().__init__(template_name, title)

    def get(self, **kwargs):
        articles = Article.get(
            {
                "user.username": session["user"]["username"],
                "user.password": session["user"]["password"]
            })
        kwargs.__setitem__("articles", articles)
        return render_template(self.get_template_name(), **kwargs)
