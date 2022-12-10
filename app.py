from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ma-deuxieme-page")
def page2():
    return render_template("page-2.html")
