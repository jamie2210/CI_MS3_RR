import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)

index = Blueprint('index', __name__)


@index.route("/")
def home():
    """
    HOME FUNCTION
    Renders template for the home page
    """
    return render_template("index.html")
