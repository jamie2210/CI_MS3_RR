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
