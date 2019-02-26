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


user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
headers={'User-Agent':user_agent}
#pool = PooledDB(pymysql,5,host='localhost',user='root',passwd='147258',db='qidian',port=3306,charset='utf8mb4') #5为连接池里的最少连接数
#conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
import re
def selectMysql(connection):
    with connection.cursor() as cursor:
        sql = 'select * from `qd_Links_bad` '
        cursor.execute(sql)
        qd_links = cursor.fetchall()
        connection.commit()
        return qd_links
def collect_bookes(next_url,i,bookId,bookName,bookType,rank):#收集书籍内容
    next_url='https:'+next_url
    r=requests.get(next_url,headers=headers);
    soup = BeautifulSoup(r.text,'html.parser')#html.parser
    chapterId=i
    chapName=soup.find(class_='j_chapterName')
    if chapName is None:
        chapterName=''
    else:
        chapterName=chapName.get_text()
    chapCont=soup.find(class_="read-content j_readContent")
    if chapCont is None:
        chapterContent=''
    else:
        chapterContent=chapCont.get_text().strip()
    #chapterContent=soup.find(class_="read-content j_readContent").get_text().strip()
    chapterContent=re.sub('\s','',chapterContent)
    #chapterContent=str(chapterContent,'utf8')
    #print(chapterContent)
    nextCl=soup.find(id="j_chapterNext")
    if nextCl is None:
        return None
    else :
        nextChapterLink=nextCl.get('href')
    #chapterContent = re.findall(u'[\u4e00-\u9fa5].+?',chapterContent)
    connectMysql(conn, bookId, bookName,bookType, chapterId, chapterName, chapterContent,rank)
    return nextChapterLink
def connectMysql(connection,bookId,bookName,bookType,chapterId,chapterName,chapterContent,rank):#连接数据库并插入数据
#获取会话指针
    with connection.cursor() as cursor:
#创建sql语句
        sql = "insert into `qd_books_bad` (`bookId`,`bookName`,`bookType`,`chapterId`,`chapterName`,`chapterContent`,`rank`) values (%s,%s,%s,%s,%s,%s,%s)"
#执行sql语句
        cursor.execute(sql,(bookId,bookName,bookType,chapterId,chapterName,chapterContent,rank))
#提交数据库
        connection.commit()
def deleteMysql(connection,bookId,rank):
    with connection.cursor() as cursor:
        # 创建sql语句
        sql = "DELETE from `qd_books_bad` where bookID=%s"

        # 执行sql语句
        cursor.execute(sql, (bookId))
        rank -=1
        # 提交数据库
        connection.commit()
def collect_singlebook(firstchapter_url,bookId,bookName,bookType,rank):#收集单本书的章节
    next_url=firstchapter_url
    for i in range(1,11):
        if next_url :
            next_url=collect_bookes(next_url,i,bookId,bookName,bookType,rank)
            print(next_url,i,bookId,bookName,bookType,rank)
        else:
            if i<11:
                deleteMysql(conn,bookId,rank)
            break
if __name__ == '__main__':
    #i=1;
    conn = pymysql.connect(host='127.0.0.1', user='root', password='lzjwang', db='qidian1', charset='utf8')
    # mongo_con=pymysql.connect(host='127.0.0.1', user='root', password='lzjwang', db='qidian1', charset='utf8mb4')

    all_book_firstlink=selectMysql(conn)
    rank=2060#书籍排名
    # deleteMysql(conn,"107580")

    for i in all_book_firstlink[2050:3000]:
        print(i)
        bookId=i[0]
        bookName=i[2]
        bookType=i[3]
        book_firstchapter_link=i[4]
        if str(book_firstchapter_link) is None:
            continue
        else:
            collect_singlebook(book_firstchapter_link,bookId,bookName,bookType,rank)
            rank+=1

    conn.close()