#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

from email_sender import controllers
from email_sender.models.normal_sender import normal_email_core
from email_sender.settings import settings


def NormalEmailHandler(info):
    """
    普通邮件发送，可指定附件，附件可以为图片或文本文件等
    info: dict
    example:
    ```
        {
            "email_addresses": [xxx.com],
            "content": xxx,
            "files": [
                "file1": {
                    "name": a.zip,
                    "body": xx,  # bytes
                ],
            "images": [
                "file2": {
                    "name": a.jpg,
                    "body: xx,  # bytes
                }
            ]
            }
        }
    ```
    """
    email_addresses = info.get("email_addresses")
    content = info.get("content")
    files = info.get("files")
    images = info.get("images")

    subject = controllers.parse_message.email_dict["text_email"]["subject"]

    if not email_addresses:
        logging.error("email_addresses do not exist")
        return False

    try:
        normal_email_core.login(settings["email"]["mail_user"],
                                settings["email"]["mail_pwd"])
        sender = settings["email"]["mail_user"]
        for email_address in email_addresses:
            msg = normal_email_core.generate_msg(
                sender=sender,
                receiver=email_address,
                subject=subject,
                text_content=content,
                imgs_data=images,
                files_data=files)

            normal_email_core.send_email(
                sender=sender,
                receivers=email_address,
                msg=msg
            )
    except Exception as e:
        logging.exception("send email exception: {}".format(e))
        return False
    return True
