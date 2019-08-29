#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import multiprocessing


class EmailPool(object):

    # TODO:暂时还没有使用到

    def __init__(self, processes=5):
        self.pool = multiprocessing.Pool(processes=processes)

    def async_run_task(self, func, args=(), kwds={}, callback=None,
                 error_callback=None):
        self.pool.apply_async(func, args=args, kwds=kwds,
                              callback=callback, error_callback=error_callback)


email_pool = EmailPool()
