import os
from flask import render_template, Blueprint

index = Blueprint('index', __name__)


@index.route("/")
def home():
    """
    HOME FUNCTION
    Renders template for the home page
    """
    return render_template("index.html")
