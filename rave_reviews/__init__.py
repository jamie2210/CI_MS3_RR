import os
from flask import Flask
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

# IMPORT env if there is an env.py file
# Used in local dev as not pushed to github & heroku
if os.path.exists("env.py"):
    import env

# App variables for setup and mongodb connectivity
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# app & db need to be defined first before the routes
from rave_reviews.index.routes import index  # noqa: E402
from rave_reviews.raves.routes import raves  # noqa: E402
from rave_reviews.authentication.routes import authentication  # noqa: E402
from rave_reviews.organisations.routes import organisations  # noqa: E402
from rave_reviews.error_handlers.routes import errors  # noqa: E402
app.register_blueprint(index)
app.register_blueprint(raves)
app.register_blueprint(authentication)
app.register_blueprint(organisations)
app.register_blueprint(errors)
