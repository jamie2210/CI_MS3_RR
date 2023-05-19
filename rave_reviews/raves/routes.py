import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from rave_reviews import mongo
from bson.objectid import ObjectId
from flask import request
from flask_paginate import Pagination, get_page_args
from math import ceil
import boto3
from werkzeug.utils import secure_filename

# Specify the folder/directory where files will be uploaded
UPLOAD_FOLDER = "uploads"
# Specify the name of the S3 bucket where files will be stored
BUCKET = "rave-review-bucket"

# Create an S3 client object with the provided AWS credentials
s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

# Create a raves object as a blueprint
raves = Blueprint('raves', __name__)


@raves.route("/get_raves/", methods=["GET"])
def get_raves():
    """
    This function renders the raves template to display
    all raves and if the amount is greater than 4 a
    pagination is displayed
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    try:
        # Get the 'rave_id' from the request arguments
        rave_id = request.args.get('rave_id')
        # Get the page, per_page, and offset values from the request arguments
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page',
            offset_parameter='offset')
        # Set the number of items per page to 4
        per_page = 4
        # Create pagination for the raves by calling the pagination function
        raves, num_pages = create_pagination(page, per_page)
        # Find comments in the MongoDB collection
        comments = list(mongo.db.comments.find(
            {"rave_id": rave_id}).sort("comment_created_by", 1))
        # Render the 'raves.html' template with the provided variables
        return render_template(
            "raves.html", title="RAVE REVIEWS",
            raves=raves, comments=comments, num_pages=num_pages, page=page)
    except Exception as e:
        flash("An exception occurred while retrieving rave reviews" + str(e))
        return redirect(url_for("index.home"))


@raves.route("/get_user_raves/", methods=["GET"])
def get_user_raves():
    """
    This function renders the raves template to display
    only the raves uploaded by the user if the amount is
    greater than 4 a pagination is displayed
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))
    try:
        # Get the 'rave_id' from the request arguments
        rave_id = request.args.get('rave_id')
        # Get the page, per_page, and offset values from the request arguments
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page',
            offset_parameter='offset')
        # Call the user in session
        session_user = session.get("user")
        # Check if a user session exists and has a valid value
        if session_user:
            # Perform pagination with user-specific information
            raves, num_pages = create_pagination(
                page, per_page, session_user=session_user)
            title = f"{session_user}'s RAVES"
        else:
            # Perform pagination with all information
            raves, num_pages = create_pagination(
                page, per_page)
            title = "RAVE REVIEWS"
        # Find comments in the MongoDB collection
        comments = list(mongo.db.comments.find(
            {"rave_id": rave_id}).sort("comment_created_by", 1))
        # Render the 'raves.html' template with the provided variables
        return render_template(
            "raves.html", title=title,
            raves=raves, comments=comments,
            num_pages=num_pages, page=page, session_user=session_user)
    except Exception as e:
        flash("An exception occurred while retrieving the rave reviews" +
              str(e))
        return redirect(url_for("index.home"))


@raves.route("/search", methods=["GET", "POST"])
def search():
    """
    This function searches the mongo db index and displays
    only the raves with the search criteria if the amount is
    greater than 4 a pagination is displayed
    """
    # Get the query from the form submission
    query = request.form.get("query")
    # Get the 'rave_id' from the request arguments
    rave_id = request.args.get('rave_id')
    # Get the page, per_page, and offset values from the request arguments
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    # Find comments in the MongoDB collection
    try:
        comments = list(mongo.db.comments.find(
            {"rave_id": rave_id}).sort("comment_created_by", 1))
        # Render the 'raves.html' template with the provided variables
    except Exception as e:
        flash("An exception occurred while searching the rave reviews" +
              str(e))
        return redirect(url_for("raves.get_raves"))
    # Create pagination for the raves by calling the pagination function
    raves, num_pages = create_pagination(page, per_page, query)
    return render_template(
        "raves.html", title="RAVES",
        raves=raves, comments=comments, num_pages=num_pages, page=page)


@raves.route("/add_rave", methods=["GET", "POST"])
def add_rave():
    """
    This function adds a rave review to mongoDB
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("index.home"))

    if request.method == "POST":
        try:
            # Check if the file type is an allowed image file type
            image_url = upload("rave_image")
            if image_url == "invalid":
                flash("Invalid file format. Please use 'JPG', 'jpeg', 'PNG'")
                return redirect(url_for("raves.add_rave"))

            # Retrieve the value of the "rave_set"
            # field from the submitted form
            rave_set_link = request.form.get("rave_set")
            # Call fucntion to modify youtube link
            modified_link = modify_youtube_link(rave_set_link)
            # Check ifbanger is checked and set value
            banger = "on" if request.form.get("banger") else "off"

            # Create a dictionary to store the rave review data
            rave = {
                "organisation_name": request.form.get("organisation_name"),
                "rave_image": image_url,
                "rave_name": request.form.get("rave_name"),
                "date": request.form.get("date"),
                "venue": request.form.get("venue"),
                "rave_description": request.form.get("rave_description"),
                "rave_set": modified_link,
                "banger": banger,
                "created_by": session["user"]
            }
            # Insert dictionary into mongoDB collection
            mongo.db.raves.insert_one(rave)
            flash("Rave Review Uploaded!")
        except Exception as e:
            flash("An exception occurred while adding the review" + str(e))
        # Redirect the user to the page displaying all raves
        return redirect(url_for("raves.get_raves"))
    # Retrieve the list of organisations from the database and sort them
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    # Render the "add_rave.html" template
    return render_template(
        "add_rave.html", title="REVIEW RAVE", organisations=organisations)


# S3 Bucket functions
# Allowed image types for uploads
ALLOWED_EXTENSIONS = {'jpg', 'JPG', 'png', 'PNG', 'jpeg'}


def allowed_file(filename):
    """
    Check if the file extension is allowed based on the ALLOWED_EXTENSIONS set.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(file_key):
    """
    This function uploads the file to an S3
    bucket and returns the generated image URL.
    """
    # Retrieve the file from the request using the provided file key
    f = request.files[file_key]
    # Check if the file exists and the extension is allowed
    if f and allowed_file(f.filename):
        # Generate a secure filename to avoid any security issues
        file_name = secure_filename(f.filename)
        file_content = f.read()
        # Upload the file content to an S3 bucket
        s3.put_object(
            Bucket=BUCKET, Key=file_name, Body=file_content,
            ContentType=f.content_type)
        # Construct the URL of the uploaded image
        image_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"
        # Return the generated image URL or "invalid" if file not valid
        return image_url
    else:
        return "invalid"


def modify_youtube_link(link):
    """
    This function takes a YouTube link and
    returns it edited so it will embed correctly
    """
    if "youtube.com" in link:
        if "embed/" not in link:
            if "watch?v=" in link:
                # If the condition is True, replace "watch?v=" with "embed/"
                link = link.replace("watch?v=", "embed/")
        # Otherwise, already contains "embed/" or is a valid YouTube link
        # and doesn't need any modification
    elif "youtu.be" in link:
        # If link is youtu.be format it is replaced with
        # the web based embed structure
        link = link.replace(
            "youtu.be/", "www.youtube.com/embed/")
    else:
        # Ignore the link if it is not a YouTube link
        link = ""
    return link


@raves.route("/edit_rave/<rave_id>", methods=["GET", "POST"])
def edit_rave(rave_id):
    """
    This function edits a rave review and updates the
    information in mongoDB
    """
    if request.method == "POST":
        try:
            # Check if the file type is an allowed image file type
            image_url = upload("rave_image")
            if image_url == "invalid":
                flash("Invalid file format. Please use 'JPG', 'jpeg', 'PNG'")
                return redirect(url_for("raves.get_raves"))

            # Check ifbanger is checked and set value
            banger = "on" if request.form.get("banger") else "off"
            # Retrieve the value of the "rave_set"
            # field from the submitted form
            rave_set_link = request.form.get("rave_set")
            # Call the function to modify youtube link
            modified_link = modify_youtube_link(rave_set_link)

            # Create a dictionary to store the rave review data
            submit = {
                "organisation_name": request.form.get("organisation_name"),
                "rave_image": image_url,
                "rave_name": request.form.get("rave_name"),
                "date": request.form.get("date"),
                "venue": request.form.get("venue"),
                "rave_description": request.form.get("rave_description"),
                "rave_set": modified_link,
                "banger": banger,
                "created_by": session["user"]
            }
            # Update the rave document in the MongoDB collection
            mongo.db.raves.update_one(
                {"_id": ObjectId(rave_id)}, {"$set": submit})
            rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
            rave_name = rave['rave_name']
            flash(f"{rave_name} Edit Uploaded!")
        except Exception as e:
            flash("An exception occurred while editing the review" + str(e))
        # Redirect the user to the "get_raves" route
        return redirect(url_for("raves.get_raves"))

    # Retrieve the rave document from the MongoDB and sort
    rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
    organisations = mongo.db.organisation.find().sort(
        "organisation_name", 1)
    return render_template(
        "edit_rave.html", rave=rave,
        title="EDIT REVIEW", organisations=organisations)


@raves.route("/delete_rave/<rave_id>")
def delete_rave(rave_id):
    """
    This function deletes a rave review
    """
    try:
        # finds the rave name before deleting it
        rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
        rave_name = rave['rave_name']
        mongo.db.raves.delete_one({"_id": ObjectId(rave_id)})
        # f string adds rave name to the flash message once deleted
        flash(f"{rave_name} is Gone!")
    except Exception as e:
        flash("An exception occurred while deleting the review" + str(e))
    return redirect(url_for("raves.get_raves"))


@raves.route("/add_comment/<rave_id>", methods=["POST"])
def add_comment(rave_id):
    """
    This function adds a comment to the specific
    review (rave_id) it was commented on
    """
    # check the user is logged in
    if 'user' not in session:
        return redirect(url_for("index.home"))

    # create a comment object
    comment = {
        "comment_text": request.form.get("comment"),
        "comment_created_by": session["user"],
        "comment_id": ObjectId(rave_id),
    }
    try:
        # Insert the comment into collection in MongoDB
        mongo.db.comments.insert_one(comment)
        # Retrieves all comments that match the rave_id
        # Sorts comments by who made the comment
        comments = list(
            mongo.db.comments.find(
                {"rave_id": rave_id}).sort("comment_created_by", 1))
        flash("Comment successfully added")
    except Exception as e:
        flash("An exception occurred while adding the comment" + str(e))
    # Redirect the user to the 'get_raves' route
    return redirect(
        url_for("raves.get_raves", raves=raves, comments=comments))


def create_pagination(page, per_page, query=None,
                      session_user=None, rave_id=None):
    offset = (page - 1) * per_page
    """
    This function sets up pagination for the rave reviews.

    Args:
        page: The current page number.
        per_page: The number of items per page.
        query: A search query for filtering raves. Defaults to None.
        session_user: The user associated with the session. Defaults to None.
        rave_id: The ID of a specific rave. Defaults to None.
    """
    if query:
        # Search raves based on the given query
        search_raves = mongo.db.raves.find({"$text": {"$search": query}})
        num_raves = mongo.db.raves.count_documents(
            {"$text": {"$search": query}})
        raves = search_raves.skip(offset).limit(per_page)
    elif session_user:
        # Fetch raves created by the session user
        user_raves = mongo.db.raves.find({"created_by": session_user})
        num_raves = mongo.db.raves.count_documents(
            {"created_by": session_user})
        raves = user_raves.skip(offset).limit(per_page)
    else:
        # Fetch all raves
        raves = mongo.db.raves.find().skip(offset).limit(per_page)
        num_raves = mongo.db.raves.count_documents({})

    num_pages = (num_raves // per_page) + (
        num_raves % per_page > 0)  # calculate number of pages

    return raves, num_pages
