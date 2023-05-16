import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)

index = Blueprint('index', __name__)


@index.route("/")
def home():
    """
    HOME FUNCTION WHEN NO USER LOGGED IN
    Renders template for the home page
    """
    # If the user is logged in, redirect them to logged in home/landing page
    if 'user' in session:
        return redirect(url_for("logged_in_index.home"))
    return render_template("index.html")


@index.route("/logged_in_home")
def logged_in_home():
    """
    HOME FUNCTION WHEN USER LOGGED IN
    Renders template for the home page
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    return render_template("logged_in_index.html")


@index.route("/contact")
def contact():
    """
    CONTACT PAGE
    Renders template for the contact page
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    return render_template("contact.html", title="PLEASE GET IN TOUCH")
