# -*- coding: utf-8 -*-

import pymysql
from settings import dbConfig, NOW, DEBUG
from models import Master, Monster, Item, NPC

def createMaster(ownerid, name, gender):

    # 写入数据库
    try:
        db = pymysql.connect(**dbConfig)
        cursor = db.cursor()
    except Exception as e:
        print("[{0}] [MySQL] Database Connect Error:\n{1}".format(NOW(), e))
    sql = '''
        INSERT INTO 
        PocketDragonMaster(ownerid, name, gender) 
        VALUES ('{0}', '{1}', '{2}')
    '''.format(ownerid, name, gender)
    try:
        cursor.execute(sql)
        db.commit() # delete when select
    except Exception as e:
        print("[{0}] [MySQL] Database INSERT Error:\n{1}".format(NOW(), e))
    cursor.close()
    db.close()
    if DEBUG:
        print("[{0}] [MySQL] Create Master Success.".format(NOW()))


def getMonster(pid, mid):
    # pid =  PlayerID
    # mid = MonsterID
    pass


# TEST
# createMaster(1, "Zy3", 1)