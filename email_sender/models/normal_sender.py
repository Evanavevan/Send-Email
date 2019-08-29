#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_sender.models import base
from email_sender.settings import settings


class NormalEmailSender(base.BaseEmail):
    """
    发送普通自定义格式的邮件
    """
    def __init__(self, host, port=25):
        self.host = host
        self.port = 25

    def generate_msg(self, sender, receiver, subject, text_content=None, imgs_data=[], files_data=[], **kwargs):
        """
        text_content: str，文本消息,纯文本或者html格式
        imgs_data: list，图片信息，作为附件发送，元素中body为bytes[{"name": "a.jpg", "body": xxx}]
        files：list，作为附件发送的普通文件列表，元素中body为bytes[{"name": "a.zip", "body": xxx}]
        """
        msg = MIMEMultipart()
        if text_content:
            # judge if this content is htmnl format
            if text_content.startswith("<html>") and text_content.endswith("</html>"):
                text_msg = MIMEText(text_content, "html", "utf-8")
            else:
                text_msg = MIMEText(text_content, "plain", "utf-8")
            msg.attach(text_msg)

        for img_data in imgs_data:
            img_msg = MIMEImage(img_data["body"])
            img_msg.add_header("Content-Disposition", "attachment", filename=img_data["name"])
            msg.attach(img_msg)

        for file_data in files_data:
            file_msg = MIMEText(file_data, "base64", "utf-8")
            file_msg.add_header("Content-Disposition", "attachment", filename=("utf-8", "", file_data["name"]))
            file_msg["content_type"] = "application/octet-stream"
            msg.attach(file_msg)

        msg["From"] = Header(sender)
        msg["To"] = Header(receiver)
        msg["Subject"] = Header(subject, "utf-8")
        return msg


normal_email_core = NormalEmailSender(
    settings["email"]["smtp_host"],
    settings["email"]["smtp_port"])
