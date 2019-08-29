import logging
import os

from edgebox import event
from jinja2 import Environment, PackageLoader
from tornado.options import define, options
from tornado_jinja2 import Jinja2Loader

__BASE_PACKAGE__ = "email_sender"
__BASE_DIR__ = os.path.dirname(os.path.abspath(__file__))

# TODO:read the local config
event.setup(host="192.168.6.200", type_mq=event.type_redis)

define("port", default=9995, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("conf", default=None, help="email_sender config path")

jinja2loader = Jinja2Loader('templates')

settings = {
    "host_ip": "10.201.0.1",
    "email": {
        "smtp_host": "smtp.exmail.qq.com",
        "smtp_port": 25,
        "mail_user": "evan",
        "mail_pwd": "xxxxxxxxxxx",
    },
    "topic": "email",
    "log_dir": "/var/log",
    "template_loader": jinja2loader
}


def get_template_content(template_file_path, **kwargs):
    """
    :param template_file_path: str,example 'base.html'
    :param **kwargs: the content filled in the file
    :return : str
    """
    env = Environment(loader=PackageLoader(__BASE_PACKAGE__))
    template = env.get_template(template_file_path)
    content = template.render(kwargs)
    return content
