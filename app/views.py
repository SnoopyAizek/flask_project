from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route("/")
def index():
    entered_name = request.args.get('entered_name', default=None, type=str)
    if entered_name and entered_name != '':
        name = entered_name
    else:
        name = None
    return render_template('index.html', name=name)
