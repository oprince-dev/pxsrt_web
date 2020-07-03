from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pxsrt.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from pxsrt.users.routes import users
from pxsrt.images.routes import images
from pxsrt.main.routes import main
app.register_blueprint(users)
app.register_blueprint(images)
app.register_blueprint(main)
