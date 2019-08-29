#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""monitor the queue"""
import json
import logging
import threading

from email_sender.controllers.parse_message import parse_message
from email_sender.settings import event, settings


class DetectorEmailQueue(threading.Thread):

    def __init__(self):
        super().__init__()
        self.stopped = threading.Event()

    def run(self):
        try:
            logging.warning(event.current_api_settings().settings)
            # parse_message as the callback for the specific topic
            event.subscribe_str(parse_message, _topic=settings["topic"])
            event.loop()
        except Exception as e:
            logging.exception(e)

    def stop(self):
        self.stopped.set()


detector_email_queue = DetectorEmailQueue()
