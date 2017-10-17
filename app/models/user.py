#coding:utf8
__author__ = 'Li'

from flask import current_app
from app.extensions import db, login_manage
# 导入密码散列及校验函数
from werkzeug.security import generate_password_hash, check_password_hash
# 导入生成和校验token的类库
from itsdangerous import TimedJSONWebSignatureSerializer
# 导入Mixin
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), unique=True)
    confirmed = db.Column(db.Boolean, default=False)

    # 保护密码属性，使其不可读
    @property
    def password(self):
        raise AttributeError('密码是不可读属性')

    # 把密码变成加密格式
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验密码
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 生成校验token
    def create_token(self, expiration=3600):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm_id': self.id})

    # 校验token
    @staticmethod
    def verify_token(token):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        user = None
        try:
            data = s.loads(token)
            # print(data.get('confirm_id'), type(data.get('confirm_id')))
            user = User.query.get(data.get('confirm_id'))
        except:
            return False
        # 用户是否存在
        if user is None:
            return False
        # 用户是否已经激活
        if not user.confirmed:
            user.confirmed = True
            db.session.add(user)
            return True

@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))