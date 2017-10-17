#coding:utf8
__author__ = 'Li'

from .main import main
from .posts import posts
from .user import user

DEFAULT_BLUEPRINT = (
    (main, ''),
    (user, '/user'),
    (posts, '/posts'),
)