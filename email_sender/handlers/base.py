#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
import tornado.web
import json
import base64


class MainHandler(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self):
        self.render('index.html')


class BaseHandler(tornado.web.RequestHandler):

    # @tornado.web.authenticated
    def get(self):
        self.render('index.html')

    def parse_json(self, raw_data):
        if raw_data == b"":
            return {}
        if isinstance(raw_data, bytes):
            try:
                data = str(raw_data, encoding='utf-8')
            except Exception:
                return {"data": str(base64.b64encode(raw_data),
                        encoding='utf-8')}
        else:
            data = raw_data
        data = json.loads(data)
        return data

    def parse_json_body(self):
        try:
            self.request_data = self.parse_json(self.request.body)
        except (KeyError, ValueError) as e:
            self.write_error(500, "bad json format: {}".format(str(e)))
            self.request_data = None
        return self.request_data

    def parse_query_arguments(self):
        ret = {}
        for k, v in self.request.query_arguments.items():
            if isinstance(v, list) and len(v) != 0:
                if isinstance(v[0], bytes):
                    ret[k] = str(v[0], encoding='utf-8')
                else:
                    ret[k] = v[0]
            else:
                ret[k] = v
        return ret

    def finish_request(self, body):
        self.write(json.dumps(body, sort_keys=True, separators=(',', ': ')))
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.finish()

    def write_success_json(self, data=None):
        self.set_status(200)
        if data is None:
            return self.finish_request({"desc": "success"})
        else:
            return self.finish_request({"desc": "success", "data": data})

    def write_error(self, status_code, desc=None, reason=None, **kwargs):
        result = {}
        if reason:
            self.set_status(status_code, reason=reason)
        else:
            self.set_status(status_code)

        if desc is None and "exc_info" in kwargs:
            desc = str(kwargs["exc_info"][1])

        result['desc'] = desc
        self.finish_request(result)


class AsyncHandler(BaseHandler):

    def success(self, result=None):
        return 200, result

    def failed(self, status_code, result=None):
        return status_code, result

    def write_success(self, result):
        return self.write_success_json(result)

    @property
    def executor(self):
        return self.application.executor

    @tornado.gen.coroutine
    def async_worker(self, func, data):
        status, result = yield self.executor.submit(func, (data))
        if status == 200:
            return self.write_success(result)
        else:
            return self.write_error(status, result)

    def do_post(self, data):
        return self.failed(404, "no implement")

    def do_put(self, data):
        return self.failed(404, "no implement")

    def do_get(self, data):
        return self.failed(404, "no implement")

    def do_delete(self, data):
        return self.failed(404, "no implement")

    def post(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_post, data)

    def put(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_put, data)

    def get(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_get, data)

    def delete(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_delete, data)
