from .models import app
from flask import render_template, url_for


@app.route("/", methods=["GET"])
def index_route():
    return render_template("index.html")