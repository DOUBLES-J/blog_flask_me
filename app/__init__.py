#coding:utf8
__author__ = 'Li'

from flask import Flask, render_template
from app.config import CONFIG_CHOOSE
from app.extensions import db, mail, moment, bootstrap, login_manage
from app.views import DEFAULT_BLUEPRINT

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(CONFIG_CHOOSE.get(config_name))
    # 调用初始化函数
    CONFIG_CHOOSE[config_name].init_appp(app)
    # 初始化扩展app
    config_extensions(app)
    # 配置蓝本
    config_blueprint(app)
    # 配置错误页面
    config_errors(app)

    return app


def config_extensions(app):
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    login_manage.init_app(app)

def config_blueprint(app):
    for blue_print, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blue_print, url_prefix=url_prefix)

# 错误界面
def config_errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')