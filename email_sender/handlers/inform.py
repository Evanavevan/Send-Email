#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
发送不同模板
"""
import logging

from email_sender.controllers.parse_message import email_dict
from email_sender.handlers import base
from email_sender.models.template_sender import template_email_core
from email_sender.settings import settings


class AccountInformHandler(base.BaseHandler):

    """账户审核"""

    def post(self):
        data = self.parse_json_body()
        try:
            is_success = data["is_success"]
            receivers = data["receivers"]
            verify_link = data["verify_link"]
            if is_success:
                subject = email_dict["account_verify_success_email"]["subject"]
                template = email_dict["account_verify_success_email"]["template"]
                reason = None
            else:
                reason = data["reason"]
                subject = email_dict["account_verify_fail_email"]["subject"]
                template = email_dict["account_verify_fail_email"]["template"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    verify_link=verify_link,
                    client=receiver.split("@")[0],
                    reason=reason)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class ApplicationInformHandler(base.BaseHandler):

    """应用审核"""

    def post(self):
        data = self.parse_json_body()
        try:
            is_success = data["is_success"]
            receivers = data["receivers"]
            application_name = data["application_name"]
            application_version = data["application_version"]
            verify_link = data["verify_link"]
            if is_success:
                reason = None
                template = email_dict["application_verify_success_email"]["template"]
                subject = email_dict["application_verify_success_email"]["subject"]
            else:
                reason = data["reason"]
                template = email_dict["application_verify_fail_email"]["template"]
                subject = email_dict["application_verify_fail_email"]["subject"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    client=receiver.split("@")[0],
                    verify_link=verify_link,
                    reason=reason,
                    application_name=application_name,
                    application_version=application_version)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class RegisterInformHandler(base.BaseHandler):

    """注册账户验证"""

    def post(self):
        data = self.parse_json_body()
        try:
            verify_link = data["verify_link"]
            receivers = data["receivers"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        template = email_dict["register_verify_email"]["template"]
        subject = email_dict["register_verify_email"]["subject"]
        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    client=receiver.split("@")[0],
                    verify_link=verify_link)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class ResetPwdInformHanler(base.BaseHandler):

    """重置密码通知"""

    def post(self):
        data = self.parse_json_body()
        try:
            reset_time = data["reset_time"]
            receivers = data["receivers"]
            email_address = data["email_address"]
            verify_link = data["verify_link"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        template = email_dict["reset_pwd_email"]["template"]
        subject = email_dict["reset_pwd_email"]["subject"]
        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    client=receiver.split("@")[0],
                    verify_link=verify_link,
                    reset_time=reset_time,
                    email_address=email_address)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class SubAccountInformHandler(base.BaseHandler):

    """子账户验证通知"""

    def post(self):
        data = self.parse_json_body()
        try:
            company = data["company"]
            verify_link = data["verify_link"]
            receivers = data["receivers"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        template = email_dict["subaccount_verify_email"]["template"]
        subject = email_dict["subaccount_verify_email"]["subject"]
        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    company=company,
                    verify_link=verify_link)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class DeliverManagerInfomHandler(base.BaseHandler):

    """转交管理员通知"""

    def post(self):
        data = self.parse_json_body()
        try:
            company = data["company"]
            verify_link = data["verify_link"]
            receivers = data["receivers"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        template = email_dict["deliver_manager_email"]["template"]
        subject = email_dict["deliver_manager_email"]["subject"]
        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    client=receiver.split("@")[0],
                    company=company,
                    verify_link=verify_link)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()


class OperatorInformHandler(base.BaseHandler):

    """操作员账户验证"""

    def post(self):
        data = self.parse_json_body()
        try:
            company = data["company"]
            verify_link = data["verify_link"]
            receivers = data["receivers"]
        except KeyError:
            self.write_error(400, desc="parameter wrong")
            return

        template = email_dict["operator_inform_email"]["template"]
        subject = email_dict["operator_inform_email"]["subject"]
        sender = settings["email"]["mail_user"]
        try:
            template_email_core.login(sender, settings["email"]["mail_pwd"])
            for receiver in receivers:
                msg = template_email_core.generate_msg(
                    template_file=template,
                    sender=sender,
                    receiver=receiver,
                    subject=subject,
                    client=receiver.split("@")[0],
                    company=company,
                    verify_link=verify_link)
            template_email_core.send_email(sender=sender, receivers=receiver, msg=msg)
        except Exception as e:
            logging.exception("send email exception: {}".format(e))
            self.write_error(500, desc="send email failed")
            return
        self.write_success_json()
