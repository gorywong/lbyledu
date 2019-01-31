# -*- coding: utf-8 -*-
import random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from lbyledu.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def forget_password_email(email, send_type="forget"):
    email_record = EmailVerifyRecord()
    code = random_str(6)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "forget":
        email_title = "豫灵镇中心学校找回密码验证"
        email_body = "您的找回密码验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass