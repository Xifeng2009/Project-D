# -*- coding: utf-8 -*-

import sys
import pymysql
import datetime

# MySQL
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
dbConfig = {
          'host'    : '127.0.0.1',
          'port'    : 3306,
          'user'    : 'root',
          'password': 'n1nja!!!',
          'db'      : 'mysql',
          'charset' : 'utf8',
}

DEBUG = True # 调试模式
NOW   = lambda : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
EXP_MASTER = [100*i for i in range(31)] # 0-30级角色升级所需经验
Exps  = [ # 0-99级怪兽升级所需经验
    0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676,
    729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209,
    2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489,
    4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569,
    7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801
]
GENDER = { 0: 'Male', 1: 'Female' }
GENDER_CN = { 0: '女', 1: '男' }
ATTRIBUTION = { # 属性表

}
CHARACTER = { # 性格表
    '固执': ['ATK', 1.1, 'eng'],
    '急躁': ['SP',  1.1, 'hurry'],
    # TODO//
}
EVOLUTION = { # 进化表
    # RACE: [BOOL, METHOD, LEVEL, DIRECTION, AREA, NAME]
    # BOOL: 0:不进化 1: 进化
    # METHOD: 0: 不进化 1: 升级 1: 触媒 2: 交换 3: 亲密度 4: 场景
    # LEVEL : 进化需要等级(浮动2)
    # DIRECTION: 进化目标RACE列表 [2, 3]
    # AREA  : 进化所在地区, 默认None
    1: [1, 1, 17, 2, None, '鼻涕狗'],
    2: [1, 1, 36, 3, None, '追风狗'],
    3: [0, 0,  0, 0, None, '战风狗'],
    4: [1, 1, 19, 5, None, '玩偶喵'],
    5: [1, 1, 38, 6, None, '魔力猫'],
    6: [0, 0,  0, 0, None, '魅影猫'],
    7: [1, 1, 13, 2, None, '囤囤鼠'],
    8: [1, 1, 37, 3, None, '屯仓鼠'],
    9: [0, 0,  0, 0, None, '掘地兽'],
}
SKILL = { # 技能表
    # RACE: {LV: Skill, Lv: Skill}
    1: {1:'哭闹',5:'冲撞'},
    4: {1:'撒娇',5:'爪击'},
    7: {1:'打滚',5:'咬咬'},
}
PASSIVE = { # 被动技能
    # RACE: [SKILL1, SKILL2] 函数将会在生成实例时二者择一
    1: ['守护者'],
    2: ['守护者'],
    3: ['守护者'],
    4: ['巫师'],
    5: ['巫师'],
    6: ['巫师'],
    7: ['窃贼'],
    8: ['窃贼'],
    9: ['窃贼'],
}