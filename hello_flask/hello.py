from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<center><h1>Hello Flask!</h1></center>"
