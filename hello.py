from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>coba uaaa...</p>"

@app.route("/works")
def it_works():
    return "ini kedua"