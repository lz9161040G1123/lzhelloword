import json

import tornado.web
import configparser
import os
from pythonProject.DB_test.DB_operate import dbconf
class MainMnadeler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        argus = self.request.arguments
        print(argus)
        cur_path = os.path.abspath(os.curdir)
        cf = configparser.ConfigParser()
        cur_path = cur_path + "/data.conf"
        cf.read(cur_path)
        sql1 = "INSERT INTO `trade` (`ID`, `order_id`) VALUES (3, '3456789')"
        sec = "lzdata"
        res = dbconf(cf, sql1, sec)
        sql2 = "select *from trade"
        res = dbconf(cf, sql2, sec)


        orderid = self.get_argument("order_id")
        print(orderid)
        data = {
            'orderid': orderid,
            'data': res
        }

        self.write(data)

    def get(self):
        argus = self.request.arguments
        print(argus)
        cur_path = os.path.abspath(os.curdir)
        cf = configparser.ConfigParser()
        cur_path = cur_path + "/data.conf"
        cf.read(cur_path)
        sql1 = "INSERT INTO `trade` (`ID`, `order_id`) VALUES (3, '3456789')"
        sec = "lzdata"
        res = dbconf(cf, sql1, sec)
        sql2 = "select *from trade"
        res = dbconf(cf, sql2, sec)

        orderid = self.get_argument("order_id")
        print(orderid)
        data = {
            'orderid': orderid,
            'data': res
        }
        self.write(data)
