from datetime import datetime
import re
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/html/")
@app.route("/html/<name>")
def html_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
