# -*- coding: utf-8 -*-

from settings import NOW, GENDER_CN
from functions import createMaster, genMonsterInstance, getMonster
from models import Monster, Master, Item, NPC


def main():

    # 创建人物
    print("[{0}] [GAME] 你好, 欢迎来到新心镇, 我姓王, 是你的新邻居, 也是口袋研究所的博士, 你叫什么名字? ")
    while True:
        name = input("输入你的名字: ")
        if len(name) > 0:
            break
    print("[{0}] [GAME] 啊, [{1}], 多么好听的名字, 那么, 请告诉你的性别?".format(NOW(), name))
    while True:
        gender = input("输入你的性别(0: 女孩, 1: 男孩): ")
        if gender == '0' or gender == '1':
            break
    print("[{0}] [GAME] 原来是个{1}孩子!".format(NOW(), GENDER_CN[int(gender)]))
    createMaster(1, name, int(gender))
    # 场景: 家
    print("[{0}] [家] 妈妈: [{1}], 这里就是你的新家了, 有空去镇子上跟大家打个招呼吧".format(NOW(), name))
    # 场景: 新心镇
    print("[{0}] [新心镇]".format(NOW()))
    # 场景: 野外
    print("[{0}] [野外]".format(NOW()))
    print("[{0}] [野外] 选择你的初始怪兽!".format(NOW()))
    print("[{0}] [野外] 1: 鼻涕狗; 2: 玩偶喵; 3: 囤囤鼠".format(NOW()))
    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3]:
                break
        except: pass
    GIFT = { 1: '哭哭狗', 2: '玩偶喵', 3: '囤囤鼠' }
    print("[{0}] [野外] [{1}]选择了[{2}]".format(NOW(), name, GIFT[choice]))
    # 生成实例
    race = { 1: 1, 2: 4, 3: 7 }
    raceC = race[choice]
    print("race: ", raceC)

    monster = genMonsterInstance(raceC)
    print("[{0}] [野外] 你想给它取个名字吗?".format(NOW()))
    mName = input("输入名字: ")
    # 加入队伍


if __name__ == '__main__':
    main()