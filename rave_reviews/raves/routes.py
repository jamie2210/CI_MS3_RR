import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo

raves = Blueprint('raves', __name__)


@raves.route("/get_raves")
def get_raves():
    raves = mongo.db.raves.find()
    return render_template("raves.html", title="RAVES", raves=raves)


@raves.route("/add_rave")
def add_rave():
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    return render_template(
        "add_rave.html", title="REVIEW RAVE", organisations=organisations)
