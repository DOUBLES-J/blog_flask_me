#coding:utf8
__author__ = 'Li'

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 基本配置
class Config:
    # 密钥
    SECRET_KEY = 'this is hard to guess'

    # 数据库自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 数据库禁用追踪数据修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 发邮件的三项
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_appp(app):
        pass

# 开发环境配置
class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'blog_dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:111111@localhost/blog'

# 测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'blog_test.sqlite')

# 生产环境配置
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.sqlite')

CONFIG_CHOOSE = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig,
}