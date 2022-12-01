import pygame as p
import s
clock = p.time.Clock()
wi = 87
temp = p.image.load('enemies/temp.png')
ES = p.image.load("misc/box.png")
Empty= p.image.load('misc/box.png')
selector= p.image.load('misc/selector.png')
Stick = p.image.load('Items/stick.png')
Wsword = p.image.load('Items/woodsword.png')
Isword = p.image.load('Items/ironsword.png')
# idle and animations for main charecter
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
sign = p.image.load('Items/sign.png')
Rei = p.image.load('NPC/ReiA.png')
darkP1 = p.image.load('I/battledark.png')
battleP1 = p.image.load('I/battle.png')
door = p.image.load('apy/DOOR.png')
g5 = Di
P1 =  p.transform.scale(g5, (wi, 100))
def changecolor(image,color,x,y):
  colorImage = p.Surface(image.get_size()).convert_alpha()
  colorImage.fill(color)
  image.blit(colorImage, (0,0), special_flags = p.BLEND_RGBA_MULT)
  s.ds.blit(image,(x,y))
once = 0
originalimage = 0
timer = 0
image_bright =0

party1 = battleP1
party2 = battleP1
blinkp = p.image.load('I/blinkp.png')
enemselector = p.image.load('misc/enemselector.png')
turtle = p.image.load('enemies/turt.png')
rat = p.image.load('misc/rat.png')
stawarrior = p.image.load('icons/winged-sword.png')
stamage = p.image.load('icons/winged-scepter.png')
staranger = p.image.load('icons/winged-arrow.png')