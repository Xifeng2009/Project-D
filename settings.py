# -*- coding: utf-8 -*-

import sys
import pymysql

# MySQL
dbConfig = {
          'host'    : '127.0.0.1',
          'port'    : 3306,
          'user'    : 'root',
          'password': 'n1nja!!!',
          'db'      : 'mysql',
          'charset' : 'utf8',
}
'''
db = pymysql.connect(
    host="localhost",user="root",password="n1nja!!!",db="mysql",port=3306
)
cursor = db.cursor()
sql = "select * from user"
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
db.close()
db.commit()
db.rollback()
'''
