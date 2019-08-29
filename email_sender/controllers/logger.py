#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import logging
import os

from email_sender.settings import settings


class LogConfig(object):

    def __init__(self, log_type="console"):
        """默认指定日志输出到控制台"""
        if log_type == "console":
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(levelname)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S")
        elif log_type == "file":
            log_dir = os.path.join(settings["log_dir"], "email-sender")
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)

            current_time = datetime.datetime.now().strftime("%Y-%m-%d")
            file_name = os.path.join(log_dir, "{}.log".format(current_time))

            file_handler = logging.FileHandler(filename=file_name, encoding="utf-8",
                                               mode="a")
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                handlers=[file_handler])

    def getLogger(self):
        logger = logging.getLogger()
        return logger


logger = LogConfig().getLogger()
