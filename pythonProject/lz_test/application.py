import tornado.ioloop
import tornado.web
from pythonProject.lz_test.handler import *


def map_app():
    return tornado.web.Application(
        [
            (r"/apply", MainMnadeler)
        ]
    )
