import os

import pymysql
import configparser


def dbconf(conf, sql, sec):
    """
    :return:
    """
    connect = pymysql.connect(
        host=conf.get(sec, 'host'),
        port=int(conf.get(sec, 'port')),
        user=conf.get(sec, 'user'),
        passwd=conf.get(sec, 'password'),
        charset="utf8",
        database=conf.get(sec, 'database'),
        autocommit=True  # 这里不设置会出现无法插入值的奇怪bug
    )

    cur = connect.cursor()  # 创建游标，用于读取数据

    if connect:
        print("数据库连接成功！")
    try:
        list = cur.execute(sql)
        re_list = []
        a = []
        for i in cur.description:
            a.append(i[0])
        res = cur.fetchall()
        for i in res:
            data = {}
            for m in range(len(i)):
                data[a[m]] = i[m]
            re_list.append(data)

        return re_list

    except Exception as e:
        print(e)

    finally:
        cur.close()
        connect.close()


if __name__ == '__main__':
    # print(dbconf())
    cur_path = os.path.abspath(os.curdir)
    cf = configparser.ConfigParser()
    cur_path = cur_path + "/data.conf"
    cf.read(cur_path)
    sql = "select *from trade"
    sec = "lzdata"
    re_list = dbconf(cf, sql, sec)
    print(re_list)




    # （2）创建数据库
    # create_db = "CREATE DATABASE IF NOT EXISTS `pdf_info`;"
    # try:
    #     cur.execute(create_db)
    #     cur.execute("use pdf_info")  # 选择数据库
    # except Exception as e:
    #     print("数据库创建失败:", e)
    # else:
    #     print("数据库创建成功！")
    #
    # # （3）创建数据表
    # create_table = "CREATE TABLE IF NOT EXISTS info (t1 VARCHAR(100),pro_name VARCHAR(100), code VARCHAR(100), num VARCHAR(100),date VARCHAR(100),year VARCHAR(100),month VARCHAR(100),day VARCHAR(100), client_name VARCHAR(100),client_itin VARCHAR(100), seller_name VARCHAR(100),seller_itin VARCHAR(100), car_num VARCHAR(100),car_type VARCHAR(100),total_price VARCHAR(100),price VARCHAR(100),tax_rate VARCHAR(100),tax_price VARCHAR(100),dir VARCHAR(200),path VARCHAR(200),file VARCHAR(200))"
    # try:
    #     cur.execute(create_table)
    # except Exception as e:
    #     print("数据表创建失败:", e)
    # else:
    #     print("数据表创建成功！")
    #
    # # （4）插入数据
    # pdfs = []
    # try:
    #     for file in pdfs:
    #         insert_data = "INSERT INTO `info` VALUES('" + file["t1"] + "','" + file["pro_name"] + "','" + file[
    #             "code"] + "','" + file["num"] + "','" + file["date"] + "','" + file["year"] + "','" + file[
    #                           "month"] + "','" + file["day"] + "','" + file["client_name"] + "','" + file[
    #                           "client_itin"] + "','" + file["seller_name"] + "','" + file["seller_itin"] + "','" + file[
    #                           "car_num"] + "','" + file["car_type"] + "','" + file["total_price"] + "','" + file[
    #                           "price"] + "','" + file["tax_rate"] + "','" + file["tax_price"] + "','" + file[
    #                           "dir"] + "','" + file["path"] + "','" + file["file"] + "');"
    #         cur.execute(insert_data)
    # except Exception as e:
    #     print("数据信息插入失败:", e)
    # else:
    #     print("信息插入成功！")
    #
    # # （5）查询数据
    # try:
    #     query_info = "select * from info;"
    #     cur.execute(query_info)
    #     res = cur.fetchall()
    # except Exception as e:
    #     print("数据表创建失败:", e)
    # else:
    #     print("数据如下：")
    #     for i in res: print(i)
    #
    # # （6）关闭数据库连接
    # cur.close()
    # connect.close()
