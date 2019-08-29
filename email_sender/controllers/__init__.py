#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from email_sender.controllers.detector_queue import detector_email_queue


def start_detector():
    detector_email_queue.start()


def stop_detector():
    detector_email_queue.stop()
