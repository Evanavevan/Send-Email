#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from email_sender.handlers import config, inform, send

url_patterns = [
    (r"/api/v2/email/health", config.HealthHandler),

    (r"/api/v2/email/config", config.DefaultConfigHandler),

    (r"/api/v2/email/send", send.TextEmailHandler),

    (r"/api/v2/email/inform/account", inform.AccountInformHandler),

    (r"/api/v2/email/inform/application", inform.ApplicationInformHandler),

    (r"/api/v2/email/inform/manager", inform.DeliverManagerInfomHandler),

    (r"/api/v2/email/inform/operator", inform.OperatorInformHandler),

    (r"/api/v2/email/inform/pwd", inform.ResetPwdInformHanler),

    (r"/api/v2/email/inform/subaccount", inform.SubAccountInformHandler),

    (r"/api/v2/email/inform/register", inform.RegisterInformHandler),
]
