import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
from bson.objectid import ObjectId
import boto3
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
BUCKET = "rave-review-bucket"

s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

raves = Blueprint('raves', __name__)


@raves.route("/get_raves")
def get_raves():
    raves = mongo.db.raves.find()
    return render_template("raves.html", title="RAVES", raves=raves)


@raves.route("/add_rave", methods=["GET", "POST"])
def add_rave():
    if request.method == "POST":

        image_url = upload("rave_image")

        rave_set_link = request.form.get("rave_set")
        modified_link = modify_youtube_link(rave_set_link)

        banger = "on" if request.form.get("banger") else "off"

        rave = {
            "organisation_name": request.form.get("organisation_name"),
            "rave_image": image_url,
            "rave_name": request.form.get("rave_name"),
            "date": request.form.get("date"),
            "venue": request.form.get("venue"),
            "rave_description": request.form.get("rave_description"),
            "rave_set": modified_link,
            "banger": banger,
            "created_by": session["user"]
        }
        mongo.db.raves.insert_one(rave)
        flash("Rave Review Uploaded!")
        return redirect(url_for("raves.get_raves"))

    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)

    return render_template(
        "add_rave.html", title="REVIEW RAVE", organisations=organisations)


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


@raves.route("/edit_rave/<rave_id>", methods=["GET", "POST"])
def edit_rave(rave_id):
    if request.method == "POST":

        banger = "on" if request.form.get("banger") else "off"

        image_url = upload("rave_image")

        submit = {
            "organisation_name": request.form.get("organisation_name"),
            "rave_image": image_url,
            "rave_name": request.form.get("rave_name"),
            "date": request.form.get("date"),
            "venue": request.form.get("venue"),
            "rave_description": request.form.get("rave_description"),
            "rave_set": request.form.get("rave_set"),
            "banger": banger,
            "created_by": session["user"]
        }
        mongo.db.raves.update_one({"_id": ObjectId(rave_id)}, {"$set": submit})
        flash("Rave Review Uploaded!")
        return redirect(url_for("raves.get_raves"))

    rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    return render_template(
        "edit_rave.html", rave=rave,
        title="EDIT REVIEW", organisations=organisations)


@raves.route("/delete_rave/<rave_id>")
def delete_rave(rave_id):
    # finds the rave name before deleting it
    rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
    rave_name = rave['rave_name']
    mongo.db.raves.delete_one({"_id": ObjectId(rave_id)})
    # f string adds rave name to the flash message once deleted
    flash(f"{rave_name} is Gone!")
    return redirect(url_for("raves.get_raves"))
