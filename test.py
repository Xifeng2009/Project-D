# -*- coding: utf-8 -*-
ID = 0
'''
PocketDragonRace
PocketDragonMonsters
'''
from models import Monster, Master, NPC
import pymysql
from settings import dbConfig

def main():
    hero = Monster(0, "Hero")
    darkhero = Monster(2, "DarkHero")
    zhero    = Monster(3, "Z-Hero")
    enemy = Monster(1, "Shadow")

    hero.attack(enemy)
    hero.itemEquip("圣剑")

    player1 = Master(0, "Zy")
    player2 = Master(1, "Shadow")

    # player1.showMyEquipments()
    # player1.showMyMainBag()
    # player1.showMyPower()

    # npc1 = NPC(0, "Magerita")
    # npc1.Talkto(player1)
    # npc1.Buyfrom(player1)
    # npc1.Sellto(player1)
    # npc1.QuitSession()
    # npc1.Fightto(player1)

    hero.showSkills()
    hero.learnSkill("死从天降")
    hero.showSkills()

    player1.showMyTeam()
    player1.addTeamMember(hero)
    player1.addTeamMember(darkhero)
    player1.addTeamMember(darkhero)
    player1.addTeamMember(darkhero)
    player1.addTeamMember(darkhero)
    player1.addTeamMember(darkhero)
    player1.addTeamMember(zhero)
    player1.showMyTeam()
    player1.showMonsterRepo()
    player1.showItemRepo()

def main2():
    db = pymysql.connect(**dbConfig)
    cursor = db.cursor()
    sql = "SELECT * FROM PocketDragonRace WHERE raceID='1'"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    # TODO// 取数据库数据生成实例


if __name__ == '__main__':
    main()
    main2()