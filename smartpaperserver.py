from flask import Flask, session
from flask import request

from miners.ScienceDirectMiner import ScienceDirectMiner
from utils.DBController import DBController
from models.User import User
from modules.Login import Login
import json

app = Flask(__name__)


@app.route('/', methods=["POST"])
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
        if session["user"] == user:
            return json.dumps({"result": True})
        else:
            login_module = Login(user)
            login_result = login_module.login()
            session["user"] = user
            return json.dumps({"result": login_result})


if __name__ == '__main__':
    app.run()
