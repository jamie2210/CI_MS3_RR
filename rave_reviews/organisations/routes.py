import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
from bson.objectid import ObjectId

organisations = Blueprint('organisations', __name__)


@organisations.route("/get_organisations")
def get_organisations():
    """
    This function renders the organisations template with all
    organisations in the organisation collection
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    # If the user is not admin, redirect them to home/landing page
    if session.get("user") != 'admin':
        return redirect(url_for("index.logged_in_home"))

    # Retrieve the list of organizations from the database
    # and sort them by "organisation_name" in ascending order
    organisations = list(
        mongo.db.organisation.find().sort("organisation_name", 1))
    # Render the "organisations.html" template
    return render_template(
        "organisations.html", title="ORGANISATIONS",
        organisations=organisations)


@organisations.route("/add_organisation", methods=["GET", "POST"])
def add_organisation():
    """
    This function adds an organisation to mongoDB
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    # If the user is not admin, redirect them to home/landing page
    if session.get("user") != 'admin':
        return redirect(url_for("index.logged_in_home"))

    # Get the organisation name from the form data
    if request.method == "POST":
        organisation = {
            "organisation_name": request.form.get("organisation_name")
        }
        # Insert the organisation into the database
        mongo.db.organisation.insert_one(organisation)
        flash("New Organisation Added")
        # Redirect to the page that displays all organisations
        return redirect(url_for("organisations.get_organisations"))
    # Render the add_organisation template
    return render_template("add_organisation.html", title="ADD ORGANISATION")


@organisations.route(
    "/edit_organisation/<organisation_id>", methods=["GET", "POST"])
def edit_organisation(organisation_id):
    """
    This function edits an existing organisation
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    # If the user is not admin, redirect them to home/landing page
    if session.get("user") != 'admin':
        return redirect(url_for("index.logged_in_home"))

    if request.method == "POST":
        # Get the submitted form data
        submit = {
            "organisation_name": request.form.get("organisation_name")
        }
        # Update the organisation in the database
        mongo.db.organisation.update_one(
            {"_id": ObjectId(organisation_id)}, {"$set": submit})
        org = mongo.db.organisation.find_one(
            {"_id": ObjectId(organisation_id)})
        # Retrieve the updated organisation from the database
        org_name = org['organisation_name']
        flash(f"{org_name} Updated")
        # Redirect the user to the organisations list page
        return redirect(url_for("organisations.get_organisations"))

    # Retrieve the organisation to be edited from the database
    organisation = mongo.db.organisation.find_one(
        {"_id": ObjectId(organisation_id)})

    # Render the edit_organisation template
    return render_template("edit_organisation.html", title="EDIT ORGANISATION",
                           organisation=organisation)


@organisations.route("/delete_organisation/<organisation_id>")
def delete_organisation(organisation_id):
    """
    This function deletes an existing organisation
    """
    # finds the organisation name before deleting it
    organisation = mongo.db.organisation.find_one(
        {"_id": ObjectId(organisation_id)})
    organisation_name = organisation['organisation_name']
    mongo.db.organisation.delete_one({"_id": ObjectId(organisation_id)})
    # f string adds organisation name to the flash message once deleted
    flash(f"{organisation_name} is Gone!")
    return redirect(url_for("organisations.get_organisations"))
