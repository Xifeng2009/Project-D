# -*- coding: utf-8 -*-

from models import Monster


class MonkeyKing(Monster):
    '''爆怒猴王'''
    attibution   = None # 属性: 地水火风光暗 TODO//第一属性,第二属性,附加属性
    # 特性 TODO
    healthPoint  = 1    # HP
    magicPoint   = 1    # MP
    damagePoint  = 1    # 攻击力
    skillPpower  = 1    # 技能强度
    HP_increase  = 1    # HP成长
    MP_increase  = 1    # MP成长
    ATK_increase = 1    # 攻击力成长
    level        = 5    # 等级
    exp          = 1    # 经验值
    expReward    = 1    # 对方经验值收益
    skills       = [None, None, None, None] # 技能表(4)
    passives     = []   # 被动效果
    item         = None # 装备道具
    Alive        = True # 是否死亡
    aStatus      = []   # 正面状态
    pStatus      = []   # 负面状态
    Wild         = True # 是否野生
    OwnerID      = None # 所有者ID
    raceID       = '001'# 种族编号
    eLevel       = [1, 2, 3]    # 进化等级
    ePhase       = 1    # 进化阶段
    image        = 'static/images/001_1_head.png' # 图片
    eMethod      = 'lvl'# 进化方式: lvl:升级 stone:触媒

class Pigsy(Monster):
    '''饕餮豪猪'''
    pass

class ShaMonk(Monster):
    '''嗜血魔僧'''
    pass