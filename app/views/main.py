#coding:utf8
__author__ = 'Li'

from flask import Blueprint
from flask import render_template, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')

