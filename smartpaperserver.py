from flask import Flask
from flask import request

from miners.ScienceDirectMiner import ScienceDirectMiner
from utils.DBController import DBController

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


if __name__ == '__main__':
    app.run()
