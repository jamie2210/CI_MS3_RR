import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from rave_reviews import mongo

authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))
    return render_template("register.html", title="REGISTER")


@authentication.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(
                    url_for(
                        "authentication.profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("authentication.login"))

        else:
            # user doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("authentication.login"))

    return render_template("login.html", title="LOGIN")


@authentication.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username form the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", title="{}'s PROFILE".format(username))

    return redirect(url_for("authentication.login"))


@authentication.route("/logout")
def logout():
    # remove user from session cookies
    flash("CYA! You've been logged out")
    session.pop("user")
    return redirect(url_for("authentication.login"))
