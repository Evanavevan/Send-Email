#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

from email_sender.controllers.email_pool import email_pool
from email_sender.handlers import base
from email_sender.models.normal_sender import normal_email_core
from email_sender.settings import settings


class TextEmailHandler(base.BaseHandler):

    """文本邮件发送"""

    def post(self):
        # TODO:需要支持附件的发送
        data = self.parse_json_body()
        try:
            receivers = data["receivers"]
            subject = data["subject"]
            email_content = data["content"]
        except KeyError:
            self.write_error(400, desc="parameters wrong")
            return

        if self.request.files:
            files = self.request.files
            files_data = []
            for file in files:
                files_data.append({
                    "name": files[file][0]["filename"],
                    "body": files[file][0]["body"]
                })

        sender = settings["email"]["mail_user"]
        try:
            normal_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = normal_email_core.generate_msg(
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    text_content=email_content,
                    files_data=files_data)
                normal_email_core.send_email(
                    sender=sender,
                    receivers=receiver,
                    msg=msg)
        except Exception as e:
            logging.exception(e)
            self.write_error(500, desc="send email failed: {}".format(e))
            return
        self.write_success_json()
