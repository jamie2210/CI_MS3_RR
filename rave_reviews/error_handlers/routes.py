import os
from rave_reviews import app
from flask import (render_template, Blueprint)

errors = Blueprint('errors', __name__)


@app.errorhandler(400)
def error_400(e):
    """
    400 ERROR FUNCTION - bad request
    400 Error page return with 400 message
    """
    message = "Oh dear, the request has somehow been corrupted,\
         rewind this one back and \
            hit the return button below!"
    return render_template("errors.html", title="400 Error", message=message)


@app.errorhandler(401)
def error_401(e):
    """
    401 ERROR FUNCTION - unauthorised access
    401 Error page return with 401 message
    """
    message = "Oh dear, you are not authorised to access this page,\
         you may need to log in.\
             Rewind this one back and hit the return button below!"
    return render_template("errors.html", title="401 Error", message=message)


@app.errorhandler(403)
def error_403(e):
    """
    403 ERROR FUNCTION - forbidden
    403 Error page return with 403 message
    """
    message = "Oh dear, the page you are looking for cannot be found,,\
         rewind this one back and \
            hit the return button below!"
    return render_template("errors.html", title="403 Error", message=message)


@app.errorhandler(404)
def error_404(e):
    """
    404 ERROR FUNCTION - if address incorrect
    404 Error page return with 404 message
    """
    message = "Oh dear, the page you are looking for cannot be found, \
        rewind this one back and \
            hit the return button below!"
    return render_template("errors.html", title="404 Error", message=message)


@app.errorhandler(500)
def error_500(e):
    """
    500 ERROR FUNCTION - internal server error
    500 Error page return with 500 message
    """
    message = "Oh dear, we are experiencing an internal server error, \
        rewind this one back and \
            hit the return button below!"
    return render_template("errors.html", title="500 Error", message=message)
