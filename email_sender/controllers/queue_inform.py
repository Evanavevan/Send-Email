#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

from email_sender import controllers
from email_sender.models.template_sender import template_email_core
from email_sender.settings import get_template_content, settings


def OperatorInformHandler(info):
    """
    操作员通知邮件发送
    info: dict {"company": x, "email_addresses": x}
    """
    email_addresses = info.get("email_addresses")
    company = info.get("company")
    verify_link = info.get("verify_link")

    template = controllers.parse_message.email_dict["operator_inform_email"]["template"]
    subject = controllers.parse_message.email_dict["operator_inform_email"]["subject"]

    if not email_addresses or not company:
        logging.error("email_addresses and company not complete")
        return False

    try:
        template_email_core.login(
            settings["email"]["mail_user"],
            settings["email"]["mail_pwd"])

        sender = settings["email"]["mail_user"]
        for email_address in email_addresses:
            msg = template_email_core.generate_msg(
                template_file=template,
                sender=sender,
                receiver=email_address,
                subject=subject,
                company=company,
                verify_link=verify_link,
                client=email_address.split("@")[0])

            template_email_core.send_email(
                sender=sender,
                receivers=email_address,
                msg=msg)
    except Exception as e:
        logging.exception("send email exception: {}".format(e))
        return False
    return True
