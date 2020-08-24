from flask import render_template, Blueprint
from pxsrt.models import Upload


main = Blueprint('main', __name__)


@main.route('/')
def home():
    uploads = Upload.query.all()
    return render_template('home.html', uploads=uploads)
