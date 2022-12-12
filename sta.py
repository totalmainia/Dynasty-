import pygame as p
import im
S = 0
class Player(object):
    def __init__(self):
        super().__init__()
        self.image = (im.P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.hasattacked = False
        self.defend = False
        self.defense = 1
        self.attack = 1
        self.Hp = 10
        self.maxHp = 10
        self.mana = 0
        self.currentmana = 0
        self.luck = 0
        self.level=1
        self.clas = None
        self.mini = (im.Di)
        self.name = ''
class Pm1(object):
    def __init__(self):
        super().__init__()
        self.image = (im.P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.hasattacked = False
        self.defend = False
        self.defense = 1
        self.attack = 1
        self.Hp = 10
        self.maxHp = 10
        self.mana = 1
        self.currentmana = 1
        self.luck = 0
        self.level=1
        self.clas = 1
        self.mini = (im.Di)
class Pm2(object):
    def __init__(self):
        super().__init__()
        self.image = (im.P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.hasattacked = False
        self.defend = False
        self.defense = 1
        self.attack = 1
        self.Hp = 10
        self.maxHp = 10
        self.mana = 1
        self.currentmana = 1
        self.luck = 0
        self.level=1
        self.clas = 2
        self.mini = (im.Di)
class damagecheck(object):
    def __init__(self):
        super().__init__()
        self.Hp = 0
        self.defense = 0
        self.defend = False
        self.hasattacked = False
class Enemy(object):
  def __init__(self):
        super().__init__()
        self.image = (hmmm)
        self.image2 = (hmmm2)
        self.image3 = (hmmm3)
        self.x = 209
        self.y = 300
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.defense = 1
        self.attack = 1
        self.defend = False
        self.Hp = 0
        self.maxHp = 0
        self.mana = 0
        self.luck = 0
        self.name = 0
hmmm=im.temp
hmmm2= im.temp
hmmm3= im.temp
#[defense,attack,maxhp,hp,mana]
enemy={
  0:im.temp,
  1:im.turtle,
  2:im.rat
}
enem=Enemy()
mc = Player()
pm1 = Pm1()
pm2 = Pm2()
dmc=damagecheck()
Enemystats={
  im.temp:[3,3,20,20,0],
  im.turtle:[4,2,50,50,0],
  im.rat:[2,10,15,15,0]
}
itemstats={
  0:[0,0,0,0,0,0,0],
  #Stick
  1:[0,1,0,0,0,1,1],
  #Wsword
  2:[1,1,0,0,0,1,1],
  #Isword
  3:[0,2,0,0,0,1,1],
}
#[requiredmana,typeofspell,directhit or attack,spash or defense,%forsplash or health ,effect,chance of effect]
spell = {
  None : 'None',
  1: 'Fireball',
  2: 'Thunder Shock',
  3: 'Heal Mist',
  4: 'Summon Clam',
  5: 'Arcane Defense',
}

spellstats = {
  'Fireball':[10,1,10,3,50,None,0], #fireball
  'Thunder Shock':[10,1,35,1,0,None,0], #thunder shock
  'Heal Mist':[20,2,10,3,100,None,0], # heal mist
  'Summon Clam':[10,3,1,10,5,None,0], # summon clam
  'Arcane Defense':[25,4,0,5,0,None,0], # arcane defense
}
swordskills = {
  im.Stick:[1,None,None,None],
  im.Wsword:[2,None,None,None],
  im.Isword:[2,3,None,None],
}
#[energyused,damage%,spash,peirce,effect,chanceofeffect,multiattack,chance per attack]
skillstats = {
  1:[10,110,1,0,None,0,2,50],#bowstaff
  2:[20,60,1,2,None,0,2,100],#Dual slash
  3:[25,30,3,0,None,0,3,33],#tornado slashes
}
mcmini=p.transform.scale(mc.mini,(45,45))
pm1mini = p.transform.scale(pm1.mini,(45,45))
pm2mini = p.transform.scale(pm2.mini,(45,45))
#[defense,attack,maxhp,mana,luck]
mcstats=[1,1,10,0,0]
pm1stats=[1,1,10,0,0]
pm2stats=[1,1,10,0,0]
enemamount=0
partyamount=3