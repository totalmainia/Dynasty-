import pygame as p
import main as m

Di = p.image.load('I/downi.png')
Da = [p.image.load('I/down2.png'), p.image.load('I/down3.png')]
Ui = p.image.load('I/upi.png')
Ua = [p.image.load('I/up2.png'), p.image.load('I/up3.png')]
Li = p.image.load('I/lefti.png')
La = [
    p.image.load('I/left2.png'),
    p.image.load('I/lefti.png'),
    p.image.load('I/left3.png')
]
Ri = p.image.load('I/righti.png')
Ra = [
    p.image.load('I/right2.png'),
    p.image.load('I/righti.png'),
    p.image.load('I/right3.png')
]
g5 = Di
P1 =  p.transform.scale(g5, (m.wi, 100))
class Player(object):
    def __init__(self):
        super().__init__()
        self.image = (P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.defense = 0
        self.attack = 0
        self.Hp = 10
        self.maxHp = 10
        self.mana = 0
        self.luck = 0
        self.name = 0
class Enemy(object):
  def __init__(self):
        super().__init__()
        self.image = (P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.defense = 0
        self.attack = 0
        self.Hp = 10
        self.maxHp = 10
        self.mana = 0
        self.luck = 0
        self.name = 0