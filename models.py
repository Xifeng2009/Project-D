# -*- coding: utf-8 -*-

'''
ALL Monsters Base On Monster Class
ALL Skills   Base On Skill Json
'''

import random
import pymysql
from core.skills import *
from settings import Exps, GENDER, CHARACTER, EVOLUTION, SKILL, PASSIVE, NOW, dbConfig

'''仆从类'''
class Monster:

    id       = None
    nickname = None
    Alive    = True
    aStatus1, aStatus2, aStatus3 = [None, None, None]
    pStatus1, pStatus2, pStatus3 = [None, None, None]

    def __init__(self, raceID, level, item=None):

        self.raceID    = raceID
        self.level     = level
        self.talent    = random.uniform(0.5, 1.5)
        self.item      = item
        data = self.db2init()
        self.HP, self.MP, self.Attack, self.Magic, self.Defence, self.Resistence = data[3], data[5]*level*self.talent, data[7]*level*self.talent, data[9]*level*self.talent, data[11]*level*self.talent, data[13]*level*self.talent
        self.character = [k for k in CHARACTER.keys()][random.randint(0, 1)]
        self.fAttribution, self.sAttribution = data[15], data[16]
        self.Flight, self.Under, self.Stealth, self.Machine, self.Ghost, self.God = data[17], data[18], data[19], data[20], data[21], data[22]
        self.fFeature, self.sFeature, self.hFeature, self.Speed = data[23], data[24], data[25], data[26]
        self.Evolution = EVOLUTION[raceID][0]
        self.evo_method, self.evo_level, self.evo_direction = EVOLUTION[raceID][1], EVOLUTION[raceID][2], EVOLUTION[raceID][3]
        self.Size, self.Weight = data[27], data[28]
        self.deathPoint = level * 5
        passives = PASSIVE[raceID]
        if len(passives) == 3:
            self.passive = PASSIVE[raceID][random.randint(0, 2)]
        elif len(passives) == 2:
            self.passive = PASSIVE[raceID][random.randint(0, 1)]
        elif len(passives) == 1:
            self.passive = PASSIVE[raceID][0]
        else:
            self.passive = None
        self.skills = [s for s in SKILL[raceID].keys()]

    def db2init(self): # 从数据库中查询Race表,用于init
        try:
            db = pymysql.connect(**dbConfig)
            cursor = db.cursor()
        except Exception as e:
            print("[{0}] [MySQL] Database Connect Error:\n{1}".format(NOW(), e))
        sql = '''
            SELECT * FROM PocketDragonRace WHERE raceID='{0}'
        '''.format(self.raceID)
        try:
            cursor.execute(sql)
        except Exception as e:
            print("[{0}] [MySQL] Database INSERT Error:\n{1}".format(NOW(), e))
        return cursor.fetchone()

    def itemEquip(self, item):
        self.item = item
        print("[{0}] 装备了道具 [{1}]!".format(self.nickname, item))

    def attack(self, target):
        self.target = target
        print("[{0}] 对 [{1}] 发动攻击".format(self.nickname, target.name))
        if random.randint(1, 100) >= 85: # 暴击
            target.healthPoint = target.healthPoint - self.Attack*2
        else:
            target.healthPoint = target.healthPoint - self.Attack
        if target.healthPoint <= 0:
            target.death()

    def death(self):
        self.Alive = False
        print("[{0}] 倒下, 丧失战斗能力!".format(self.nickname))

    def drop(self):
        # TODO: Class Player
        print("[{0}] 掉落了道具 [{1}]".format(self.nickname, self.item))
        self.item = None

    def getExp(self, target):
        self.exp += target.deathPoint
        if self.exp >= Exps[self.level]:
            self.levelUp()
            self.exp = self.exp - Exps[self.level]

    def levelUp(self):
        self.level += 1
        if self.level >= self.evo_level:
            self.evolution()

    def levelDown(self, n):
        self.level -= n

    def evolution(self): #TODO
        pass

    def learnSkill(self, skill):
        if None in self.skills:
            self.skills[self.skills.index(None)] = skill
            print("[{0}] 学会了技能 [{1}]".format(self.nickname, skill))
        else:
            forget = input("想忘记哪一个技能? 0:{0}, 1:{1}, 2:{2}, 3:{3}".format(self.skills[0], self.skills[1], self.skills[2], self.skills[3]))
            self.skills[forget] = skill
            print("[{0}] 已经学会了新技能 [{1}]".format(self.nickname, skill))

    def castSkill(self, index, target):
        print("[{0}] 对 [{1}] 发动技能 [{2}]".format(self.nickname, target.name, self.skills[index]))
        # TODO//
    def showSkills(self):
        print("[{0}]: []\n[{1}]: []\n[{2}]: []\n[{3}]: []".format(
            self.skills[0], self.skills[1], self.skills[2], self.skills[3]
            )
        )

    def showPassives(self):
        print("[{0}]: {1}".format(self.nickname, self.passive))

    def showMyPower(self):
        print("ID    : {:>9}".format(self.id))
        print("HP    : {:>9}".format(self.HP))
        print("MP    : {:>9}".format(self.MP))
        print("Attack: {:>9}".format(self.Attack))
        print("Magic : {:>9}".format(self.Magic))
        print("LEVEL : {:>9}".format(self.level))
        print("EXP   : {:>9}".format(self.exp))

    def __str__(self):
        return self.nickname

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