import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
import boto3

s3 = boto3.client('s3')

raves = Blueprint('raves', __name__)


@raves.route("/get_raves")
def get_raves():
    raves = mongo.db.raves.find()
    return render_template("raves.html", title="RAVES", raves=raves)


@raves.route("/add_rave", methods=["GET", "POST"])
def add_rave():
    if request.method == "POST":

        banger = "on" if request.form.get("banger") else "off"

        image_url = upload(request.files["rave_image"])

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


def upload(file):
    if request.method == "POST":

        object_name = f'rave_images/{file.filename}'

        # Get the uploaded file
        file = mongo.db.raves.files.find["rave_image"]

        # Upload the file to S3
        bucket_name = "rave-reviews-bucket"
        s3.upload_fileobj(file, bucket_name, object_name)

        object_url = f'https://{bucket_name}.s3.amazonaws.com/{object_name}'

    return object_url
