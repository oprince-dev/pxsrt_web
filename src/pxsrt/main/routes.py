from flask import render_template, Blueprint
from flask_login import current_user
from pxsrt.models import Upload


main = Blueprint('main', __name__)


@main.route('/')
def home():
    uploads = Upload.query.all()
    bgcolor = "white" if current_user.is_authenticated else "transparent"
    return render_template('home.html', uploads=uploads, bgcolor=bgcolor)
