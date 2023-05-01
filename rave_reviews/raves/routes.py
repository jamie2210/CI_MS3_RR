import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
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

        banger = "on" if request.form.get("banger") else "off"

        image_url = upload("rave_image")

        rave = {
            "organisation_name": request.form.get("organisation_name"),
            "rave_image": image_url,
            "rave_name": request.form.get("rave_name"),
            "date": request.form.get("date"),
            "venue": request.form.get("venue"),
            "rave_description": request.form.get("rave_description"),
            "banger": banger,
            "created_by": session["user"]
        }
        mongo.db.raves.insert_one(rave)
        flash("Rave Review Uploaded!")
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)

    return render_template(
        "add_rave.html", title="REVIEW RAVE", organisations=organisations)


def upload(file_key):
    f = request.files[file_key]
    file_name = secure_filename(f.filename)
    file_content = f.read()
    s3.put_object(Bucket=BUCKET, Key=file_name, Body=file_content)
    image_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"
    return image_url
