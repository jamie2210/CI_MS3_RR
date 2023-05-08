import os
from rave_reviews import app
from flask import (render_template, Blueprint)

errors = Blueprint('errors', __name__)


@app.errorhandler(404)
def error_404(e):
    """
    404 ERROR FUNCTION - if address isn't right
    Takes in 404 error and returns the error page with
    error message for 404 error
    """
    message = "Oh dear, the page you are looking for cannot be found, \
        rewind this one back and \
            hit the return button below!"
    return render_template("errors.html", title="404 Error", message=message)
