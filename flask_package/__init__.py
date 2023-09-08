
from datetime import datetime
from flask import Flask
from logging import DEBUG
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = b'E=+\x9f\x0b5\x04\xa1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.logger.setLevel(DEBUG)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager  = LoginManager(app)
#--------------------------------------------------------------------------------------------------------------
from flask_package import routes