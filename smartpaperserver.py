from flask import Flask, session, request

from miners.ScienceDirectMiner import ScienceDirectMiner
from utils.DBController import DBController
from models.User import User
from modules.Login import Login
from views.IndexView import IndexView
from views.AboutView import AboutView
from views.SignupView import SignupView
from views.HistoryView import HistoryView
from views.SourcesView import SourcesView
import json

app = Flask(__name__)
app.secret_key = "E7162800D84BFB861148F6F8E17462697866C542FE2E0E7D87AF0D01E209AB12"


@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        key = request.form["key"]
        science_miner = ScienceDirectMiner()
        science_miner.set_main_key(new_key=key)
        return science_miner.send_request()


@app.route('/articles-names', methods=["GET"])
def get_articles_names():
    if request.method == "GET":
        db_controller = DBController()
        db_controller.connect()


@app.route('/authenticate', methods=["POST"])
def authenticate():
    if request.method == "POST":
        user = User(username=request.form["username"], password=request.form["password"])
        try:
            if session["user"] == user:
                return json.dumps({"result": True})
            else:
                login_module = Login(user)
                login_result = login_module.login()
                if login_result:
                    session["user"] = {"username": user.get_username(), "password": user.get_password()}
                return json.dumps({"result": login_result})
        except KeyError:
            login_module = Login(user)
            login_result = login_module.login()
            if login_result:
                session["user"] = {"username": user.get_username(), "password": user.get_password()}
            return json.dumps({"result": login_result})


@app.route("/logout")
def logout():
    try:
        session["user"] = None
        return json.dumps({"result": True})
    except KeyError:
        return json.dumps({"result": False})


index_view = IndexView(template_name="index.html")
about_view = AboutView("about.html")
signup_view = SignupView("signup.html")
history_view = HistoryView("history.html")
sources_view = SourcesView("sources.html")
app.add_url_rule("/", view_func=index_view.as_view("index", template_name=index_view.get_template_name()))
app.add_url_rule("/about", view_func=about_view.as_view("about", template_name=about_view.get_template_name()))
app.add_url_rule("/signup", methods=["GET", "POST"],
                 view_func=signup_view.as_view("signup", template_name=signup_view.get_template_name()))
app.add_url_rule("/history", methods=["GET", "POST"],
                 view_func=history_view.as_view("history", template_name=history_view.get_template_name()))
app.add_url_rule("/sources", methods=["GET", "POST"],
                 view_func=sources_view.as_view("sources", template_name=sources_view.get_template_name()))

if __name__ == '__main__':
    app.config["SESSION_TYPE"] = "mongodb"
    app.run()
