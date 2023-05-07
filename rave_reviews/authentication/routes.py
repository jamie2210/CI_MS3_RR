import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from rave_reviews import mongo
from bson.objectid import ObjectId
import boto3
from werkzeug.utils import secure_filename

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

        fave_set_link = request.form.get("fave_set")
        modified_link = modify_youtube_link(fave_set_link)

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fave_dj": request.form.get("fave_dj"),
            "fave_mc": request.form.get("fave_mc"),
            "fave_venue": request.form.get("fave_venue"),
            "fave_organisation": request.form.get("organisation_name"),
            "fave_set": modified_link,
            "profile_image": image_url,
        }
        mongo.db.users.insert_one(register)

        organisations = mongo.db.organisation.find().sort(
         "organisation_name", 1)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))

    organisations = mongo.db.organisation.find().sort(
     "organisation_name", 1)

    return render_template("register.html",
                           title="REGISTER", organisations=organisations)


@authentication.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        image_url = upload("profile_image")

        fave_set_link = request.form.get("fave_set")
        modified_link = modify_youtube_link(fave_set_link)

        update_profile = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fave_dj": request.form.get("fave_dj"),
            "fave_mc": request.form.get("fave_mc"),
            "fave_venue": request.form.get("fave_venue"),
            "fave_organisation": request.form.get("organisation_name"),
            "fave_set": modified_link,
            "profile_image": image_url,
        }
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": update_profile})
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        user_name = user['username']
        flash(f"{user_name} Profile Updated!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    return render_template(
        "edit_profile.html", user=user,
        title="EDIT PROFILE", organisations=organisations)


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


def modify_youtube_link(link):
    if "watch?v=" in link:
        link = link.replace("watch?v=", "embed/")
    return link


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
    user = mongo.db.users.find_one({"username": username})
    return render_template("profile.html",
                           username=session['user'],
                           user=user, title="{}'s PROFILE".format(username))


@authentication.route("/delete_user/<user_id>")
def delete_user(user_id):
    # finds the rave name before deleting it
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = user['username']
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    # f string adds rave name to the flash message once deleted
    flash(f"{username} is Gone!")
    session.pop("user")
    return redirect(url_for("authentication.register"))


@authentication.route("/logout")
def logout():
    # remove user from session cookies
    flash("CYA! You've been logged out")
    session.pop("user")
    return redirect(url_for("authentication.login"))
