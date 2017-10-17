#coding:utf8
__author__ = 'Li'

from flask import Blueprint

posts = Blueprint('posts', __name__)

@posts.route('/')
def index():
    return 'posts模板'