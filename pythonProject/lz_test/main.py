import tornado.ioloop
import tornado.web
from pythonProject.lz_test import application
if __name__ == '__main__':
    app = application.map_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8800)
    tornado.ioloop.IOLoop.instance().start()