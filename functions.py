# -*- coding: utf-8 -*-

import pymysql
from settings import dbConfig, NOW, DEBUG
from models import Master, Monster, Item, NPC

def createMaster(uid, name, gender):
    # 创建玩家并写入数据库, 返回id
    try:
        db = pymysql.connect(**dbConfig)
        cursor = db.cursor()
    except Exception as e:
        print("[{0}] [MySQL] Database Connect Error:\n{1}".format(NOW(), e))
        return
    sql = '''
        INSERT INTO 
        PocketDragonMaster(uid, name, gender) 
        VALUES ('{0}', '{1}', '{2}')
    '''.format(uid, name, gender)
    try:
        cursor.execute(sql)
        db.commit() # delete when select
        if DEBUG:
            print("[{0}] [MySQL] Create Master Success.".format(NOW()))
        return cursor.lastrowid
    except Exception as e:
        if DEBUG:
            print("[{0}] [MySQL] Database INSERT Error:\n{1}".format(NOW(), e))
    cursor.close()
    db.close()
    return

def createMonster(m):
    # 根据生成的实例把怪兽数据写入数据库, 返回id
    try:
        db = pymysql.connect(**dbConfig)
        cursor = db.cursor()
    except Exception as e:
        print("[{0}] [MySQL] Database Connect Error:\n{1}".format(NOW(), e))
        return
    sql = '''
        INSERT INTO PocketDragonMonsters(
        raceID, nickname, `level`, talent, gender, `character`, 
        HP, MP, Attack, Magic, Defence, Resistence, fAttribution, sAttribution, 
        Flight, Under, Stealth, Machine, Ghost, God, fFeature, sFeature, hFeature, 
        Evolution, evo_method, evo_level, evo_direction, Size, Weight) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', 
        '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', 
        '{21}', '{22}',  '{23}', '{24}', '{25}', '{26}', '{27}', '{28}');
    '''.format(m.raceID, m.nickname, m.level, m.talent, m.gender, m.character,
               m.HP, m.MP, m.Attack, m.Magic, m.Defence, m.Resistence, m.fAttribution, m.sAttribution,
               m.Flight, m.Under, m.Stealth, m.Machine, m.Ghost, m.God, m.fFeature, m.sFeature, m.hFeature,
               m.Evolution, m.evo_method, m.evo_level, m.evo_direction, m.Size, m.Weight)
    try:
        cursor.execute(sql)
        db.commit() # delete when select
        if DEBUG:
            print("[{0}] [MySQL] Create Monster Success.".format(NOW()))
        return cursor.lastrowid
    except Exception as e:
        if DEBUG:
            print("[{0}] [MySQL] Database INSERT Error:\n{1}".format(NOW(), e))
    cursor.close()
    db.close()
    return

# TEST
