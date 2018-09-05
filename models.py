# -*- coding: utf-8 -*-

'''
ALL Monsters Base On Monster Class
ALL Skills   Base On Skill Json
'''

import random
from core.skills import *
from settings import Exps, GENDER, NOW

'''仆从基类'''
class Monster:

    # -----基准值-----
    attibution   = None # 属性: 地水火风光暗 TODO//第一属性,第二属性,附加属性
    # 特性 TODO
    healthPoint  = 1    # HP
    magicPoint   = 1    # MP
    damagePoint  = 1    # 攻击力
    skillPower   = 1    # 技能强度
    exp          = 1    # 经验值
    expReward    = 1    # 对方经验值收益
    skills       = [None, None, None, None] # 技能表(4)
    passives     = []   # 被动效果
    item         = None # 装备道具
    Wild         = True # 是否野生
    OwnerID      = None # 所有者ID
    raceID       = 1    # 种族编号
    eLevel       = [1, 2, 3]    # 进化等级
    ePhase       = 1    # 进化阶段
    eMethod      = 'lvl'# 进化方式: lvl:升级 stone:触媒
    HP_increase  = 1    # HP成长
    MP_increase  = 1    # MP成长
    ATK_increase = 1    # 攻击力成长
    # image        = 'static/images/001_1_head.png' # 图片
    Alive        = True # 是否死亡
    aStatus      = []   # 正面状态
    pStatus      = []   # 负面状态

    def __init__(self, name, level):
        self.name  = name
        self.level = level
        # 属性与等级的关系
        # TODO//

    def itemEquip(self, item):
        self.item = item
        print("[{0}] 装备了道具 [{1}]!".format(self.name, item))

    def attack(self, target):
        self.target = target
        print("[{0}] 对 [{1}] 发动攻击".format(self.name, target.name))
        if random.randint(1, 100) >= 85: # 暴击
            target.healthPoint = target.healthPoint - self.damagePoint*2
        else:
            target.healthPoint = target.healthPoint - self.damagePoint
        if target.healthPoint <= 0:
            target.death()

    def death(self):
        self.Alive = False
        print("[{0}] 倒下, 丧失战斗能力!".format(self.name))
        if self.Wild: self.drop()

    def drop(self): #TODO: Class Player
        print("[{0}] 掉落了道具 [{1}]".format(self.name, self.item))
        self.item = None

    def getExp(self, target):
        self.exp += target.expReward
        if self.exp >= Exps[self.level]:
            self.levelUp()
            self.exp = self.exp - Exps[self.level]

    def levelUp(self):
        self.level += 1
        if self.level >= self.eLevel[self.ePhase-1]:
            self.evolution()

    def levelDown(self, n):
        self.level -= n

    def evolution(self):
        self.ePhase += 1

    def learnSkill(self, skill):
        if None in self.skills:
            self.skills[self.skills.index(None)] = skill
            print("[{0}] 学会了技能 [{1}]".format(self.name, skill))
        else:
            forget = input("想忘记哪一个技能? 0:{0}, 1:{1}, 2:{2}, 3:{3}".format(self.skills[0], self.skills[1], self.skills[2], self.skills[3]))
            self.skills[forget] = skill
            print("[{0}] 已经学会了新技能 [{1}]".format(self.name, skill))

    def castSkill(self, index, target):
        print("[{0}] 对 [{1}] 发动技能 [{2}]".format(self.name, target.name, self.skills[index]))
        # TODO//
    def showSkills(self):
        print("[{0}]: []\n[{1}]: []\n[{2}]: []\n[{3}]: []".format(
            self.skills[0], self.skills[1], self.skills[2], self.skills[3]
            )
        )

    def showPassives(self):
        print("[{0}]: {1}".format(self.name, self.passives))

    def showMyPower(self):
        print("ID   : {:>9}".format(self.id))
        print("HP   : {:>9}".format(self.id))
        print("MP   : {:>9}".format(self.id))
        print("ATK  : {:>9}".format(self.id))
        print("SP   : {:>9}".format(self.skillPower))
        print("HPi  : {:>9}".format(self.id))
        print("MPi  : {:>9}".format(self.id))
        print("ATKi : {:>9}".format(self.id))
        print("LEVEL: {:>9}".format(self.id))
        print("EXP  : {:>9}".format(self.id))

    def __str__(self):
        return self.name

'''玩家类'''
class Master:

    Money        = 100 # 金钱,用于购买道具,恢复体力,交易仆从
    Strength     = 100 # 体力,0-200,归零时丢失金钱被送回医院
    StrengthTopLimit = 100 # 体力上限
    Courage      = 100 # 勇气,影响收服部分危险Monster的难度
    Intelligence = 90  # 智力,影响环境交互(智力越高,越容易看到隐藏的道具)
    Persistence  = 100 # 耐力,影响跑步时间
    Speed        = 100 # 走路速度
    Gender       = 1   # 0 = 女; 1 = 男
    Level        = 1   # 等级
    # PlayerTeamID = '0000000'
    PocketTeam   = [None, None, None, None, None, None] # 队伍中的Monster
    mRepository  = []                                   # 怪兽仓库
    iRepository  = []                                   # 道具仓库
    # ---------背包系统----------
    MainBag = []           # 主背包中的道具
    MainBagGrid = 10       # 背包格子
    # ---------装备系统----------
    Equipments = {         # 穿着装备
        "Head"     : None, # 帽子
        "Glasses"  : None, # 眼镜
        "Clothes"  : None, # 衣服
        "Gloves"   : None, # 手套
        "Belt"     : None, # 皮带
        "Thousers" : None, # 裤子
        "Shoes"    : None, # 鞋子
        "Ornaments": None, # 饰品
    }

    def __init__(self, id, name):
        self.name = name
        self.id   = id

    def showMyPower(self):
        print("姓名: {:>9}".format(self.name))
        print("金钱: {:>9}".format(self.Money))
        print("体力: {:>9}".format(self.Strength))
        print("勇气: {:>9}".format(self.Courage))
        print("智力: {:>9}".format(self.Intelligence))
        print("耐力: {:>9}".format(self.Persistence))
        print("速度: {:>9}".format(self.Speed))
        print("性别: {:>9}".format(GENDER[self.Gender]))
        print("等级: {:>9}".format(self.Level))

    def showMyTeam(self):
        print("[{0}] Team: ".format(self.name) + "|".join(i.name if i != None else 'Empty' for i in self.PocketTeam))

    def showMonsterRepo(self):
        print("[{0}] MonsterRepo: ".format(self.name) + "|".join(i.name if i != None else 'Empty' for i in self.mRepository))

    def showItemRepo(self):
        print("[{0}] ItemRepo: ".format(self.name) + "|".join(i.name for i in self.iRepository))

    def showMyEquipments(self):

        print(self.Equipments)

    def showMyMainBag(self):
        print("Total: {0}/{1}".format(len(self.MainBag), self.MainBagGrid))
        print("MainBag: {0}".format(self.MainBag))

    def getItem(self, item): # 得到道具, [在循环内调用]

        if len(self.MainBag) < self.MainBagGrid:
            self.MainBag.append(item)
        else:
            choice = input("背包已满,是否舍弃道具?(y/n)")
            if choice == 'y':
                print("[{0}]放弃了道具[{1}]".format(self.name, item))
            else:
                print("[{0}]选择整理背包:")
                print(self.MainBag)
                # 待处理道具堆叠

    def addTeamMember(self, monster):
        if None in self.PocketTeam:
            self.PocketTeam[self.PocketTeam.index(None)] = monster
        else:
            print("队伍已满, 请选择要换下的队员!")
            print([str(idx)+':'+str(i) for idx, i in enumerate(self.PocketTeam)])
            while True:
                try:
                    mChoice = int(input("输入队员编号"))
                    break
                except:
                    print("请重新提交编号!")
            self.mRepository.append(self.PocketTeam[mChoice]) # 加入仓库
            self.PocketTeam[mChoice] = monster
        print("[{0}]加入队伍!".format(monster))

    def trade(self, target): # 交易
        pass

    def fight2Npc(self, target): # 战斗
        print("[{0}]决斗开始了! 对手是来自[{1}]的[{2}]!".format(self.name, target.BirthPlace, target.name))
        BattleCound = 0
        while True:
            if BattleCound == 0:
                if self.PocketTeam[0].speed > target.PocketTeam[0].speed:
                    print("[Battle] [{0}]获得先手!".format(self.name))
                elif self.PocketTeam[0].speed == target.PocketTeam[0].speed:
                    if random.randint(1, 100) > 50:
                        print("[Battle] [{0}]获得先手!".format(self.name))
                    else:
                        print("[Battle] [{0}]获得先手!".format(target.name))
                else:
                    print("[Battle] [{0}]获得先手!".format(target.name))
                currentMonsterP1 = self.PocketTeam[0]
                currentMonsterP2 = target.PocketTeam[0]
            print("[Battle] START!")
            BattleCound += 1
            print("[{0}] 1: 攻击 2: 道具 3: 交换 4: 逃跑")
            choice = input("[{0}] 选择你的行动!(1/2/3/4)")
            if choice == '1':
                print("[Battle] [{0}]正在准备攻击!".format(self.name))
                fChoice = input("[Battle] [0: {0}] [1: {1}] [0: {2}] [3: {3}]".format(
                    currentMonsterP1.skills[0],
                    currentMonsterP1.skills[1],
                    currentMonsterP1.skills[2],
                    currentMonsterP1.skills[3]
                    )
                )
                print("[Battle] [{0}]选择了[{1}]".format(self.name, currentMonsterP1.skills[fChoice]))
                currentMonsterP1.castSkill(fChoice, currentMonsterP2)
            elif choice == '2':
                print("[{0}]选择使用道具!".format(self.name))
            elif choice == '3':
                print("[{0}]选择交换怪兽!".format(self.name))
            else:
                if random.randint(1, 100) > 25:
                    print("逃跑成功!")
                else:
                    print("逃跑失败!")

    def fight2Others(self, target):
        pass

    def research(self): # 调查:弹出对话框
        pass

    def talk2Npc(self, target): # 开启NPC对话
        pass

    def __str__(self):
        return self.name

'''NPC类'''
class NPC:

    PocketTeam = [None, None, None, None, None, None]
    BirthPlace = '关中'
    Level = 5

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def Talkto(self, master):
        print("[{0}]: 很高兴见到你, Master {1}".format(self.name, master.name))

    def Tradeto(self, master):
        print("[{0}]: 你想交易什么 {1}".format(self.name, master.name))

    def Sellto(self, master):
        print("[{0}]: 你想买什么?".format(self.name))

    def Buyfrom(self, master):
        print("[{0}]: 你想卖什么? 大师!".format(self.name))

    def QuitSession(self):
        print("[{0}]: 再见!".format(self.name))

    def Fightto(self, master):
        print("[{0}]: 我看到你就不爽!".format(self.name))
        master.fight2Npc(self)

    def __str__(self):
        return self.name

'''道具'''
class Item:
    pass