#coding:utf8
__author__ = 'Li'

from flask import Blueprint, flash
from flask import render_template, redirect, url_for, request
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from app.email import send_mail
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return 'user模板'

@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 创建数据
        u = User(username=form.username.data, password=form.password.data, email=form.email.data)
        # 提交到数据库
        db.session.add(u)
        db.session.commit()
        # 发送邮件
        token = u.create_token()
        send_mail(form.email.data, '账户激活', 'email/account_activate', token=token, u=u)
        flash('激活邮件已发送，请去激活。')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)

@user.route('/verify/<token>')
def verify(token):
    if User.verify_token(token):
        flash('邮箱激活成功')
        return redirect(url_for('user.login'))
    else:
        flash('无效的链接')
        return redirect(url_for('main.index'))

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        remember_me = form.remember_me.data
        u = User.query.filter_by(username=form.username.data).first()
        if u:
            if u.confirmed:
                if u.verify_password(form.password.data):
                    flash('欢迎登录')
                    login_user(u, remember=remember_me)
                    return redirect(request.args.get('next') or url_for('main.index'))
                else:
                    flash('用户名或密码错误。')
            else:
                flash('账户未激活，请前往邮箱激活。')
        else:
            flash('用户名或密码错误')
    return render_template('user/login.html', form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
