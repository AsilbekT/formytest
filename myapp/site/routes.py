from flask import Blueprint
from flask import render_template, request

site = Blueprint("site", __name__)


@site.route('/')
def index():
    place = ''

    if request.method == "POST":
        data = request.form.to_dict()

    return render_template('index.html', data=place)
