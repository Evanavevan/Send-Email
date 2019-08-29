#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import logging


email_dict = {
    "operator_inform_email": {
        "desc": "向操作员发送通知邮件",
        "subject": "【JX IoT Edge】操作员账户验证",
        "template": "operator_inform.html",  # 使用的模板文件
        "handler": None
    },
    "account_verify_fail_email": {
        "desc": "账户审核失败",
        "subject": "【JX IoT Edge】账号审核通知",
        "template": "account_verify_fail.html",
        "handler": None
    },
    "account_verify_success_email": {
        "desc": "账户审核成功",
        "subject": "【JX IoT Edge】账号审核通知",
        "template": "account_verify_success.html",
        "handler": None
    },
    "application_verify_fail_email": {
        "desc": "应用审核失败",
        "subject": "【JX IoT Edge】应用审核通知",
        "template": "application_verify_fail.html",
        "handler": None
    },
    "application_verify_success_email": {
        "desc": "应用审核成功",
        "subject": "【JX IoT Edge】应用审核通知",
        "template": "application_verify_success.html",
        "handler": None
    },
    "deliver_manager_email": {
        "desc": "转交管理员通知",
        "subject": "【JX IoT Edge】转交管理员通知",
        "template": "deliver_manager.html",
        "handler": None
    },
    "register_verify_email": {
        "desc": "注册账户验证",
        "subject": "【JX IoT Edge】注册账户验证",
        "template": "register_verify.html",
        "handler": None
    },
    "reset_pwd_email": {
        "desc": "密码重置验证",
        "subject": "【JX IoT Edge】密码重置验证",
        "template": "reset_pwd.html",
        "handler": None
    },
    "subaccount_verify_email": {
        "desc": "子账户验证",
        "subject": "【JX IoT Edge】子账户验证",
        "template": "subaccount_verify.html",
        "handler": None
    }
}


def parse_message(data, topic):
    # type: (str, str) -> None
    """
    解析消息队列中的topic为email的消息
    data: str
    topic: str
    """
    if not isinstance(data, dict):
        data = json.loads(data)

    try:
        email_type = data.get("type")
        email_info = data.get("info")
    except KeyError:
        logging.error("parse data error")
        return None

    try:
        ret = email_dict.get(email_type)["handler"](email_info)
        return ret
    except TypeError:
        logging.warning("email type error")
        return None
    except Exception as e:
        logging.exception("handler errror: {}".format(e))
        return None
