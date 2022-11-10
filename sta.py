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
        self.defense = 1
        self.attack = 1
        self.Hp = 10
        self.maxHp = 10
        self.mana = 0
        self.luck = 0
        self.name = ''
class Enemy(object):
  def __init__(self):
        super().__init__()
        self.image = (hmmm)
        self.x = 209
        self.y = 300
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.defense = 1
        self.attack = 1
        self.Hp = 0
        self.maxHp = 0
        self.mana = 0
        self.luck = 0
        self.name = 0
hmmm=im.temp
#[defense,attack,maxhp,hp,mana]
enemy={
  0:im.temp,
}
enem=Enemy()
mc = Player()
Enemystats={
  im.temp:[0,1,5,5,0],
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
mcstats=[1,1,10,0,0]