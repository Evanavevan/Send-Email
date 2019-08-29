#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib


class BaseEmail(object):

    def __init__(self):
        pass

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def set_protocol(self, protocol="smtp"):
        self.protocol = protocol

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_protocol(self):
        return self.protocol

    def login(self, user, pwd):
        """
        本地没有sendmail访问的时候，使用其他邮件服务商的SMTP访问
        :param pwd: str, 当使用sina的时候，为密码，当为qq时候，使用auth_code，生成的授权码
        """
        if "sina" in self.host.split("."):
            self.smtp_obj = smtplib.SMTP(host=self.host, port=self.port)
            self.smtp_obj.starttls()
        elif "qq" in self.host.split("."):
            self.port = 465
            self.smtp_obj = smtplib.SMTP_SSL(host=self.host, port=self.port)
        (code, resp) = self.smtp_obj.login(user, pwd)
        return (code, resp)

    def generate_msg(self):
        pass

    def send_email(self, sender, receivers, msg):
        """
        发送邮件
        :param: sender: str, 发送邮件的地址(xxx@sina.com)
        :param: receivers: list, 目标地址列表
        :param: msg: MIMEMultipart, 构建完成的邮件内容
        :return ret: dict,全部发送成功则返回空字典，出错则会返回错误码
        """
        ret = self.smtp_obj.sendmail(
            from_addr=sender,
            to_addrs=receivers,
            msg=msg.as_string())
        return ret
