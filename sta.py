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
        self.mana = 0
        self.luck = 0
        self.level=1
        self.clas = None
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
        self.mana = 0
        self.luck = 0
        self.level=1
        self.clas = None
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
  im.temp:[0,1,5,5,0],
  im.turtle:[2,1,25,25,0],
  im.rat:[0,99,1,1,0]
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
#[defense,attack,maxhp,mana,luck]
mcmini=p.transform.scale(mc.mini,(45,45))
pm1mini = p.transform.scale(pm1.mini,(45,45))
pm2mini = p.transform.scale(pm2.mini,(45,45))
mcstats=[1,1,10,0,0]
pm1stats=[1,1,10,0,0]
pm2stats=[1,1,10,0,0]
enemamount=0
partyamount=3