#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import logging
import os
import sys
import unittest

from edgebox import event

email_sender_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, email_sender_dir)

from email_sender.controllers.parse_message import parse_message
from email_sender.handlers import inform
from email_sender.models.template_sender import template_email_core
from email_sender.settings import settings


def push_to_mq():
    topic = "email"
    message = {
        "type": "operator_inform_email",
        "info": {
            "email_addresses": ["2713281245@qq.com"],
            "company": "company"}}

    event.publish_raw(json.dumps(message), topic)

class TestInform(unittest.TestCase):
    """测试发送操作员同时邮件是否成功"""

    def setUp(self):
        self.event = event
        self.event.setup(host="192.168.6.200", type_mq=event.type_redis)
        self.template_email_core = template_email_core
        self.topic = "email"
        self.message = {
            "type": "operator_inform_email",
            "info": {
                "email_addresses": ["2713281245@qq.com"],
                "company": "company"}}

    def test_parse_message(self):
        """测试解析"""
        ret = parse_message(self.message, self.topic)
        logging.info("ret: {}".format(ret))
        self.assertNotEqual(ret, None)


if __name__ == "__main__":
    unittest.main()
