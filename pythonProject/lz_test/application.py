import tornado.ioloop
import tornado.web

from pythonProject.lz_test.handler import MainMnadeler, test1, test2, test3, test5


def map_app():
    return tornado.web.Application(
        [
            (r"/apply", MainMnadeler),
            (r"/api/login", test1),
            (r"/api/today-orders", test2),
            (r"/api/history-orders", test2),
            (r"/api/data", test3),
            (r"/api/dishes", test5)

        ]
    )
