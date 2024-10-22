import tornado.ioloop
import tornado.web
from handler import *


def map_app():
    return tornado.web.Application(
        [
            (r"/apply", MainMnadeler)
        ]
    )
