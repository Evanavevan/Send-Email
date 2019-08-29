#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
用来从消息队列中读取任务，发送验证邮件
"""
import email
import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_sender.models import base
from email_sender.settings import __BASE_DIR__, get_template_content, settings


class TemplateEmailSender(base.BaseEmail):
    """
    发送指定模板的的邮件信息
    使用example:
    ```python
    template_email_core = Email("smtp.qq.com", 25)
    template_email_core.login(user, password)
    msg = email.generate_msg(xxx)
    template_email_core.send_email(xxx)
    ```
    或者: template_email_core.one_key_send()
    """

    def __init__(self, host, port=25):
        """
        :param host: str, 发件人的邮箱服务器(smtp.sina.com)
        """
        self.host = host
        self.port = port

    def generate_msg(self, template_file, sender, receiver, subject, **kwargs):
        """
        根据指定的模板文件和内容生成邮件内容
        :param sender: str, 邮件显示的发送者
        :param receiver: str, 邮件显示的接收者
        :param subject: str, 邮件的主题
        :return msg: MIMEMultipart
        """
        content = get_template_content(template_file, **kwargs)
        msg = MIMEMultipart()
        template_msg = MIMEText(content, "html", "utf-8")
        msg.attach(template_msg)

        msg["From"] = Header(sender)
        msg["To"] = Header(receiver)
        msg["Subject"] = Header(subject, "utf-8")
        return msg


template_email_core = TemplateEmailSender(
    settings["email"]["smtp_host"],
    settings["email"]["smtp_port"])
