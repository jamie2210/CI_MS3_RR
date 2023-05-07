import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from rave_reviews import mongo
from bson.objectid import ObjectId
import boto3

UPLOAD_FOLDER = "uploads"
BUCKET = "rave-review-bucket"

s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

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

        image_url = upload("profile_image")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_image": image_url,
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))
    return render_template("register.html", title="REGISTER")


ALLOWED_EXTENSIONS = {'jpg', 'JPG', 'png', 'PNG'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(file_key):
    f = request.files[file_key]
    if f and allowed_file(f.filename):
        file_name = secure_filename(f.filename)
        file_content = f.read()
        s3.put_object(
            Bucket=BUCKET, Key=file_name, Body=file_content,
            ContentType=f.content_type)
        image_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"
        return image_url
    else:
        flash("Invalid file format. Use 'jpg', 'JPG', 'png', 'PNG'")
        return redirect(request.url)


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
