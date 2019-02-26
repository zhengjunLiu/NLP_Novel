#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*-
'''
Created on 2018年7月17日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
from bs4 import BeautifulSoup
from datetime import datetime
import threading
import requests
import logging
import urllib.request;
import time
import random
import json
import re

import pymysql
from http import cookiejar

# import DBUtils
# from DBUtils.PooledDB import PooledDB
user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
headers = {'User-Agent': user_agent}
# pool = PooledDB(pymysql,5,host='localhost',user='root',passwd='147258',db='math_model',port=3306,charset='utf8mb4') #5为连接池里的最少连接数
# conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
import re


def book_link_collect(url):  # 解析页面
    linkarray = []
    songdetail = requests.get(url, headers=headers);
    soup = BeautifulSoup(songdetail.text, 'html.parser')  # html.parser
    # print(soup)
    soup = soup.find(class_="all-book-list")
    # print(soup)
    for li in soup.select('li'):
        book_id = li.find_all('a')[0]['data-bid']
        authorName = li.find_all('a')[2].text
        bookName = li.find_all('a')[1].text
        bookType = li.find_all('a')[3].text + ' ' + li.find_all('a')[4].text
        # print(book_id+authorName+bookName+bookType)
        connectMysql(conn, book_id, authorName, bookName, bookType)


def connectMysql(connection, book_id, authorName, bookName, bookType):  # 连接数据库并插入数据
    # 获取会话指针
    with connection.cursor() as cursor:
        # 创建sql语句
        sql = "insert into `qd_Links_good_Type` (`bookId`,`authorName`,`bookName`,`bookType`) values (%s,%s,%s,%s)"
        # 执行sql语句
        cursor.execute(sql, (book_id, authorName, bookName, bookType))
        # 提交数据库
        connection.commit()


def selectMysql(connection):
    with connection.cursor() as cursor:
        sql = 'select * from `qd_Links_good_Type` '
        cursor.execute(sql)
        qd_links = cursor.fetchall()
        connection.commit()
        return qd_links


if __name__ == '__main__':
    # i=1;
    # Collection = pymysql.connect(host='localhost', user='root', password='lzjwang', db='qidian1', charset='utf8mb4')
    # coll=Collection.cursor()
    conn = pymysql.connect(host='localhost', user='root', password='lzjwang', db='qidian1', charset='utf8mb4')

    # for i in range(1,201):
    #     url="https://www.qidian.com/finish?action=hidden&orderId=2&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page="+str(i)#构造url链接
    #     book_link_collect(url)
    qd_links = selectMysql(conn)
    cru=conn.cursor()
    # cookies={'csrfToken':'obI18HgaI6M22do2EuWMvKC4G6irVv76ayzlkQGF', 'newstatisticUUID':'1531725562_792732245' e1=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_B58%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22mqd_P_finishm%22%2C%22eid%22%3A%22%22%7D; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; lrbc=1005238666%7C356441115%7C0%2C2750457%7C46354696%7C0%2C1003665757%7C312844288%7C0; rcr=1005238666%2C2750457%2C1004836098%2C3197456%2C1011327373%2C1010504384%2C1003665757; hiijack=0; bc=1005238666}
    for i in qd_links[3900:4000]:
        # print(i[0])
        url = 'https://book.qidian.com/info/' + str(i[0])
        logging.captureWarnings(True)
        r = requests.get(url, headers=headers)
        _cookies = r.cookies  # 获取cookie
        # print(r.text)
        # print(_cookies['_csrfToken'])
        # time.sleep(1)
        book_url = 'https://book.qidian.com/ajax/book/category?_csrfToken=' + _cookies['_csrfToken'] + '&bookId=' + str(
            i[0])
        html = requests.get(book_url, cookies=_cookies, headers=headers);
        # print(html.text)
        long_data = json.loads(html.text)  # json的数据格式
        try:
            book_chapter_address = long_data['data']['firstChapterJumpurl']
        except Exception as err:
            book_chapter_address=""
            print(err)
        bookId = str(i[0])
        authorName = str(i[1])
        bookName = str(i[2])
        bookType = str(i[3])
        print(bookId, authorName, bookName, bookType ,book_chapter_address)
        sql = "insert into `qd_Links_good` (`bookId`,`authorName`,`bookName`,`bookType`,`book_first_chapter_link`) values (%s,%s,%s,%s,%s)"
        # 执行sql语句
        cru.execute(sql, (bookId, authorName, bookName, bookType ,book_chapter_address))
        # 提交数据库
        conn.commit()
    conn.close()