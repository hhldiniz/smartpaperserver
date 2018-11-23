import json

from flask import Flask, session, request, send_from_directory

from models.Article import Article
from models.User import User
from modules.Login import Login
from utils.DBController import DBController
from utils.MakePDF import MakePDF
from views.AboutView import AboutView
from views.HistoryView import HistoryView
from views.IndexView import IndexView
from views.SignupView import SignupView
from views.SourcesView import SourcesView

app = Flask(__name__)
app.secret_key = "E7162800D84BFB861148F6F8E17462697866C542FE2E0E7D87AF0D01E209AB12"


@app.route('/articles-names', methods=["GET"])
def get_articles_names():
    if request.method == "GET":
        db_controller = DBController()
        db_controller.connect()


@app.route('/authenticate', methods=["POST"])
def authenticate():
    if request.method == "POST":
        try:
            user = User(username=request.form["username"], password=request.form["password"])
            user_array = user.get({"username": user.get_username(), "password": user.get_password()})[0]
            user.set_name(user_array["name"])
        except IndexError:
            return json.dumps([{"result": False}])
        try:
            if session["user"] == user:
                return json.dumps([{"result": True}])
            else:
                login_module = Login(user)
                login_result = login_module.login()
                if login_result:
                    session["user"] = {"username": user.get_username(),
                                       "password": user.get_password(),
                                       "name": user.get_name()}
                return json.dumps({"result": login_result})
        except KeyError:
            login_module = Login(user)
            login_result = login_module.login()
            if login_result:
                session["user"] = {"username": user.get_username(),
                                   "password": user.get_password(),
                                   "name": user.get_name()}
            return json.dumps([{"result": login_result}])


@app.route("/logout")
def logout():
    try:
        session.__delitem__("user")
        return json.dumps({"result": True})
    except KeyError:
        return json.dumps({"result": False})


@app.route("/user_photo", methods=["GET"])
def user_photo():
    try:
        session_user = session["user"]
        user = User(username=session_user["username"], password=session_user["password"])
        return user.get_user_photo(send_from_directory)
    except KeyError:
        return json.dumps({"result": False})


@app.route("/download_history")
def download_history():
    try:
        session_user = session["user"]
        articles = Article.get({"user.username": session_user["username"],
                                "user.password": session_user["password"]})
        print(articles)
        make_pdf = MakePDF(json.dumps(articles))
        return send_from_directory("./files/pdf", make_pdf.generate_from_string())
    except KeyError:
        return json.dumps([{"result": False}])


@app.route("/user_info", methods=["GET", "POST"])
def get_user_info():
    try:
        session_user = session["user"]
        db_controller = DBController()
        db_controller.connect()
        return json.dumps(db_controller.as_array("users", {"username": session_user["username"],
                                                           "password": session_user["password"]}))
    except KeyError:
        return json.dumps([{"result": False}])


index_view = IndexView("index.html")
about_view = AboutView("about.html")
signup_view = SignupView("signup.html")
history_view = HistoryView("history.html")
sources_view = SourcesView("sources.html")

app.add_url_rule("/", methods=["GET", "POST"],
                 view_func=index_view.as_view("index", template_name=index_view.get_template_name()))
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
