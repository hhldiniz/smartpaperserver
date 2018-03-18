from flask import Flask
from flask import request
from miners.ScienceDirectMiner import ScienceDirectMiner

app = Flask(__name__)


@app.route('/', methods=["POST"])
def search():
    if request.method == "POST":
        key = request.form["key"]
        science_miner = ScienceDirectMiner()
        science_miner.set_main_key(new_key=key)
        return science_miner.send_request()


if __name__ == '__main__':
    app.run()
