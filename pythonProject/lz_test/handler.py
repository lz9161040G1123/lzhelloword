import json

import tornado.web
import configparser
import os
import tornado.ioloop
from pythonProject.DB_test.DB_operate import dbconf


class MainMnadeler(tornado.web.RequestHandler):

    def set_default_headers(self):
        # 设置CORS头
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

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


class test1(tornado.web.RequestHandler):

    def set_default_headers(self):
        # 设置CORS头
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    @tornado.gen.coroutine
    def post(self):
        data = {
            'status': 'success'
        }
        data = json.dumps(data)

        self.write(data)

    def get(self):
        data = {
            'status': 'success'
        }
        data = json.dumps(data)

        self.write(data)


class test2(tornado.web.RequestHandler):

    def set_default_headers(self):
        # 设置CORS头
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    @tornado.gen.coroutine
    def post(self):
        data1 = {
            'orderId': '123',
            'dish': '鱼',
            'quantity': 2,
            'danwei': '斤',
            'price': 200,
            'totalPrice': 400
        }
        data2 = {
            'orderId': '234',
            'dish': '肉',
            'quantity': 3,
            'danwei': '斤',
            'price': 200,
            'totalPrice': 600
        }
        data3 = {
            'orderId': '345',
            'dish': '白菜',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data_list = [data1, data2, data3]
        data = {
            'data': data_list
        }

        data = json.dumps(data, ensure_ascii=False)

        self.write(data)

    def get(self):
        data1 = {
            'orderId': '123',
            'dish': '鱼',
            'quantity': 2,
            'danwei': '斤',
            'price': 200,
            'totalPrice': 400
        }
        data2 = {
            'orderId': '234',
            'dish': '肉',
            'quantity': 3,
            'danwei': '斤',
            'price': 200,
            'totalPrice': 600
        }
        data3 = {
            'orderId': '345',
            'dish': '白菜',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data_list = [data1, data2, data3]
        data = {
            'data': data_list
        }

        data = json.dumps(data, ensure_ascii=False)

        self.write(data)


class test3(tornado.web.RequestHandler):

    def set_default_headers(self):
        # 设置CORS头
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    @tornado.gen.coroutine
    def post(self):
        data = {
            'msg': 'success'
        }
        data = json.dumps(data)

        self.write(data)

    def get(self):
        data = {
            'msg': 'success'
        }
        data = json.dumps(data)

        self.write(data)
