from .handlers import app, new_user,new_staff,new_department,new_key
from flask import Response, render_template, url_for, redirect,request


@app.route("/", methods=["GET"])
def index_route():
    return render_template("index.html")

@app.route("/signin", methods=["GET"])
def signin_route():
    return render_template("signin.html")

@app.route("/login", methods=["GET"])
def login_route():
    return redirect(url_for("signin_route"))


@app.route("/users", methods=["GET", "POST"])
def users_route():
    if(request.method == "POST"):
        if(new_user(request.form)):
            return "Success"
        else:
            return "Couldn't add new user!"

    if(request.method == "GET"):

        return render_template("index.html")


@app.route("/users/<user_id>", methods=["GET", "PUT", "PATCH"])
def user_route(user_id):
    if(request.method == "GET"):
        pass
    if(request.method == "PUT" or request.method == "PATCH"):
        pass


@app.route("/staffs", methods=["GET", "POST"])
def staffs_route():
    if(request.method == "POST"):
        if(new_staff(request.form)):
            return "Success"
        else:
            return "Couldn't add new user!"

    if(request.method == "GET"):

        return render_template("index.html")

@app.route("/departments", methods=["GET", "POST"])
def departments_route():
    if(request.method == "POST"):

        response = new_department(request.form)
        return {"message": response}

    if(request.method == "GET"):

        return render_template("index.html")

@app.route("/keys", methods=["GET", "POST"])
def keys_route():
    if(request.method == "POST"):

        response = new_key(request.form)
        return {"message": response}

    if(request.method == "GET"):

        return render_template("index.html")