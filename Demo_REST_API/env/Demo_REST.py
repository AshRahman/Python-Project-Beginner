from distutils.log import debug
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")

def index():
    return "Welcome to REST"


if __name__=="__main__":
    app.run(debug=True)