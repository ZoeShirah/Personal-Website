"""Personal Website"""
import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET']
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/bio')
def bio():
    """About Me page"""

    return render_template("bio.html")


@app.route('/contact')
def contact():
    """Contact Information Page"""

    return render_template('contact.html')

if __name__ == "__main__":  # pragma: no cover

    # while developing/debugging *********
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode
    #***********************************
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    # connect_to_db(app, os.environ.get("DATABASE_URL", "postgresql:///stars"))

    # db.create_all(app=app)
    PORT = int(os.environ.get("PORT", 5000))

    #while developing/debugging ****************
    app.run(host="0.0.0.0", port=PORT)
    # #***********************************

    #for deployment on heroku ***********
    # DEBUG = "NO_DEBUG" not in os.environ
    # app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
    #********************************
