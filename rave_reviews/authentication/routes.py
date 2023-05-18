import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from rave_reviews import mongo
from bson.objectid import ObjectId
import boto3
from werkzeug.utils import secure_filename

# Specify the folder/directory where files will be uploaded
UPLOAD_FOLDER = "uploads"
# Specify the name of the S3 bucket where files will be stored
BUCKET = "rave-review-bucket"

# Create an S3 client object with the provided AWS credentials
s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

# Create an authentication object as a blueprint
authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"])
def register():
    """
    This function registers a new user and uploads
    their profile information to mongoDB then
    displays it on the profile page
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("authentication.register"))

        # Check if the file type is an allowed image file type
        image_url = upload("profile_image")
        if image_url == "invalid":
            flash("Invalid file format. Please use 'JPG', 'jpeg', 'PNG'")
            return redirect(url_for("authentication.register"))

        # Retrieve the value of the "fave_set" field from the submitted form
        fave_set_link = request.form.get("fave_set")
        # Call fucntion to modify youtube link
        modified_link = modify_youtube_link(fave_set_link)

        # Create a dictionary to store the profile data
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fave_dj": request.form.get("fave_dj"),
            "fave_mc": request.form.get("fave_mc"),
            "fave_venue": request.form.get("fave_venue"),
            "fave_organisation": request.form.get("fave_organisation"),
            "fave_set": modified_link,
            "profile_image": image_url,
        }
        # Insert dictionjary into mongoDB collection
        mongo.db.users.insert_one(register)
        # Retrieve the list of organisations from the database and sort them
        organisations = mongo.db.organisation.find().sort(
         "organisation_name", 1)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))
    # Retrieve the list of organisations from the database and sort them
    organisations = mongo.db.organisation.find().sort(
     "organisation_name", 1)
    # Render the "register.html" template
    return render_template("register.html",
                           title="REGISTER", organisations=organisations)


@authentication.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    """
    This function edits the users profile and adds the
    eidts to mongoDB then displays them on the profile
    page
    """
    if request.method == "POST":

        # Check if the file type is an allowed image file type
        image_url = upload("profile_image")
        if image_url == "invalid":
            flash("Invalid file format. Please use 'JPG', 'jpeg', 'PNG'")
            return redirect(url_for(
                "authentication.profile", username=session["user"]))

        # Retrieve the value of the "fave_set" field from the submitted form
        fave_set_link = request.form.get("fave_set")
        # Call fucntion to modify youtube link
        modified_link = modify_youtube_link(fave_set_link)

        # Create updated the dictionary to store the profile data
        update_profile = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fave_dj": request.form.get("fave_dj"),
            "fave_mc": request.form.get("fave_mc"),
            "fave_venue": request.form.get("fave_venue"),
            "fave_organisation": request.form.get("fave_organisation"),
            "fave_set": modified_link,
            "profile_image": image_url,
        }
        # Insert updated dictionary into mongoDB collection
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": update_profile})
        # Search for the user and redirect them back to their profile page
        # with their updated information displayed
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        user_name = user['username']
        flash(f"{user_name} Profile Updated!")
        return redirect(
            url_for("authentication.profile", username=session["user"]))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    # Retrieve the list of organisations from the database and sort them
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    # Render the "edit_profile.html" template
    return render_template(
        "edit_profile.html", user=user,
        title="EDIT PROFILE", organisations=organisations)


# S3 Bucket functions
# Allowed image types for uploads
ALLOWED_EXTENSIONS = {'jpg', 'JPG', 'jpeg', 'png', 'PNG'}


def allowed_file(filename):
    """
    Check if the file extension is allowed based on the ALLOWED_EXTENSIONS set.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(file_key):
    """
    This function uploads the file to an S3
    bucket and returns the generated image URL.
    """
    # Retrieve the file from the request using the provided file key
    f = request.files[file_key]
    # Check if the file exists and the extension is allowed
    if f and allowed_file(f.filename):
        # Generate a secure filename to avoid any security issues
        file_name = secure_filename(f.filename)
        file_content = f.read()
        # Upload the file content to an S3 bucket
        s3.put_object(
            Bucket=BUCKET, Key=file_name, Body=file_content,
            ContentType=f.content_type)
        # Construct the URL of the uploaded image
        image_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"
        # Return the generated image URL or "invalid" if file not valid
        return image_url
    else:
        return "invalid"


def modify_youtube_link(link):
    """
    This function takes a YouTube link and
    returns it edited so it will embed correctly
    """
    if "youtube.com" in link or "youtu.be" in link:
        if "embed/" not in link:
            if "watch?v=" in link:
                # If the condition is True, replace "watch?v=" with "embed/"
                link = link.replace("watch?v=", "embed/")
        # Otherwise, already contains "embed/" or is a valid YouTube link
        # and doesn't need any modification
    else:
        # Ignore the link if it is not a YouTube link
        link = ""
    return link


@authentication.route("/login", methods=["GET", "POST"])
def login():
    """
    This function checks the user exists and successfully logs
    in the user and redirects them to their profile page.
    """
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
                # Redirect to users profile page
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
    # Render the "login.html" template
    return render_template("login.html", title="LOGIN")


@authentication.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    This function renders the users profile page through
    the username ARG asnd redirects if user not logged in
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    # Retrieve user information from the database
    user = mongo.db.users.find_one({"username": username})
    # Render profile.html template using username and user information
    return render_template("profile.html",
                           username=session['user'],
                           user=user, title="{}'s PROFILE".format(username))


@authentication.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    This function deletes the users profile using
    the user_id ARG
    """
    # finds the rave name before deleting it
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = user['username']
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    # f string adds rave name to the flash message once deleted
    flash(f"{username} is Gone!")
    # ensures the user is logged out once deleted
    session.pop("user")
    return redirect(url_for("authentication.register"))


@authentication.route("/logout")
def logout():
    """
    This function logs out the user
    """
    # remove user from session cookies
    flash("CYA! You've been logged out")
    session.pop("user")
    return redirect(url_for("index.home"))
