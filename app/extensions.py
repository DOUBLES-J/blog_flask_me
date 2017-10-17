#coding:utf8
__author__ = 'Li'

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

mail = Mail()
db = SQLAlchemy()
moment = Moment()
bootstrap = Bootstrap()
login_manage = LoginManager()