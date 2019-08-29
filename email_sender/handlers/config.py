#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from email_sender.handlers import base


class DefaultConfigHandler(base.BaseHandler):

    def post(self):
        pass


class HealthHandler(base.BaseHandler):

    """用于检查docker提供服务时的"""

    def get(self):
        self.write_success_json()
