import json
import random
import string
import tornado.gen
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

    def post(self):
        self.api1()

    def get(self):
        self.api1()

    def api1(self):
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
        data4 = {
            'orderId': '456',
            'dish': '青椒',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data5 = {
            'orderId': '567',
            'dish': '辣椒',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data6 = {
            'orderId': '678',
            'dish': '黄瓜',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data7 = {
            'orderId': '789',
            'dish': '西红柿',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data8 = {
            'orderId': '890',
            'dish': '土豆',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data9 = {
            'orderId': '901',
            'dish': '胡萝卜',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data10 = {
            'orderId': '012',
            'dish': '茄子',
            'quantity': 1,
            'danwei': '斤',
            'price': 100,
            'totalPrice': 100
        }
        data11 = {
            'orderId': '123',
            'dish': '鱼',
            'quantity': 2,
            'danwei': '斤',
            'price': 200,
            'totalPrice': 400
        }
        data_list = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]
        # 需要继续for循环，将数据添加到列表中
        # 随机字符串长度
        length = 5
        for i in range(20):
            letters = string.ascii_letters + string.digits  # 包含字母和数字
            result_str = 'dish' + random.choice(letters) + str(i)
            data_item = {
                'orderId': str(i),
                'dish': result_str,
                'quantity': i,
                'danwei': '斤',
                'price': i + 1,
                'totalPrice': i * (i + 1)
            }
            data_list.append(data_item)

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
