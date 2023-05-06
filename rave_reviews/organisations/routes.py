import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
from bson.objectid import ObjectId

organisations = Blueprint('organisations', __name__)


@organisations.route("/get_organisations")
def get_organisations():
    organisations = list(
        mongo.db.organisation.find().sort("organisation_name", 1))
    return render_template(
        "organisations.html", title="ORGANISATIONS",
        organisations=organisations)


@organisations.route("/add_organisation", methods=["GET", "POST"])
def add_organisation():
    if request.method == "POST":
        organisation = {
            "organisation_name": request.form.get("organisation_name")
        }
        mongo.db.organisation.insert_one(organisation)
        flash("New Organisation Added")
        return redirect(url_for("organisations.get_organisations"))
    return render_template("add_organisation.html", title="ADD ORGANISATION")


@organisations.route("/delete_organisation/<organisation_id>")
def delete_organisation(organisation_id):
    # finds the organisation name before deleting it
    organisation = mongo.db.organisation.find_one(
        {"_id": ObjectId(organisation_id)})
    organisation_name = organisation['organisation_name']
    mongo.db.organisation.delete_one({"_id": ObjectId(organisation_id)})
    # f string adds organisation name to the flash message once deleted
    flash(f"{organisation_name} is Gone!")
    return redirect(url_for("organisations.get_organisations"))
