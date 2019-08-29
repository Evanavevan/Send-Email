#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from email_sender.controllers import start_detector, stop_detector
from email_sender.settings import settings
from email_sender.urls import url_patterns


class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self.executor = tornado.concurrent.futures.ThreadPoolExecutor(8)


def main():
    options.parse_command_line()
    app = TornadoApplication()
    app.listen(options.port)
    logging.info("start service at {}".format(options.port))
    start_detector()
    try:
        tornado.ioloop.IOLoop.current().start()
    finally:
        logging.info("stop service")
        stop_detector()


if __name__ == "__main__":
    main()
