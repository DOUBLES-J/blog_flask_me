#coding:utf8
__author__ = 'Li'

from threading import Thread
from app.extensions import mail
from flask import current_app, render_template
from flask_mail import Message

def send_async_mail(app, msg):
    # 邮件发送必须在线程上下文中，因此需要自己创建上下文
    with app.app_context():
        mail.send(msg)

# 封装异步发送邮件函数
def send_mail(to, subject, template, **kwargs):
    # 在任意文件中找到项目的app
    app = current_app._get_current_object()
    # 创建邮件消息对象
    msg = Message(subject=subject,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs) # 文件内容是模板文件
    msg.html = render_template(template+'.html', **kwargs)
    # 线程发送
    thr = Thread(target=send_async_mail, args=[app, msg]) # 线程里要用原始的app，不能是current_app
    thr.start()
    return thr