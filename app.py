from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='background-color:yellow; color:mediumseagreen;font-size: 100px'>Hello, Flask!</h1>"
