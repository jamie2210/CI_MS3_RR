import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)

index = Blueprint('index', __name__)


@index.route("/home")
def home():
    """
    HOME FUNCTION
    Renders template for the home page
    """
    return render_template("index.html")


@index.route("/logged_in_home")
def logged_in_home():
    """
    HOME FUNCTION WHEN USER LOGGED IN
    Renders template for the home page
    """
    return render_template("logged_in_index.html")
