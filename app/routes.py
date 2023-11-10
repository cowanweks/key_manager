from .models import app
from flask import render_template, url_for, redirect


@app.route("/", methods=["GET"])
def index_route():
    return render_template("index.html")

@app.route("/signin", methods=["GET"])
def signin_route():
    return render_template("signin.html")

@app.route("/login", methods=["GET"])
def login_route():
    return redirect(url_for("signin_route"))