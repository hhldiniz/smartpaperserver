from flask import Flask
from miners.ScienceDirectMiner import ScienceDirectMiner

app = Flask(__name__)


@app.route('/')
def search():
    science_miner = ScienceDirectMiner()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
