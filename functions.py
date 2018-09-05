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

def genMonsterInstance(raceID):

    # 生成的怪兽受天赋和性格影响其数值, talent暂定0.8-1.5, character暂定0.9-1.1
    # 从Race表提取种族值,
    # 生成实例
    try:
        db = pymysql.connect(**dbConfig)
        cursor = db.cursor()
    except Exception as e:
        print("[{0}] [MySQL] Database Connect Error:\n{1}".format(NOW(), e))
    sql = '''
        SELECT * FROM PocketDragonRace WHERE raceID='{0}'
    '''.format(raceID)
    try:
        cursor.execute(sql)
    except Exception as e:
        print("[{0}] [MySQL] Database INSERT Error:\n{1}".format(NOW(), e))

    data = cursor.fetchone()
    if DEBUG:
        print("[{0}] [MySQL] Database SELECT Success.".format(NOW()))
        print(data)
    '''Example:
    (1, 'Dog1', '哭哭狗', 
    15.0, 2.5, 10.0, 1.2, 
    5.0, 1.8, 3.0, 1.2, 3.0, 1.2, 2.0, 0.8, 
    'Wind', None, 0, 0, 0, 0, 0, 0, 'Guardian', None, None, 4.0, 1, None, 2, 2, 2)
    '''
    # TODO//生成实例
    return Monster()


def getMonster(pid, mid):
    # pid =  PlayerID
    # mid = MonsterID
    pass


# TEST
# createMaster(1, "Zy3", 1)