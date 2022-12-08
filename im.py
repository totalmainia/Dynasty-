import pygame as p
import s
clock = p.time.Clock()
wi = 87
temp = p.image.load('enemies/temp.png')
ES = p.image.load("misc/box.png")
Empty= p.image.load('misc/box.png')
add= p.image.load('misc/box.png')
magc = p.image.load('icons/book.png')
mago = p.image.load('icons/book(open).png')
magcl = p.transform.scale(magc,(40,40))
magop = p.transform.scale(mago,(40,40))
magclR = magcl.get_rect()
magclR.topleft = (420,50)
magopR = magop.get_rect()
magopR.topleft = (420,50)
selectorup = p.image.load('misc/selectorup.png')
ups = p.transform.scale(selectorup,(25,25))
upsR = ups.get_rect()
upsR.topleft = (200,140)
add1 = p.transform.scale(add,(20,20))
add1R = add1.get_rect()
add1R.topleft = (250,100)
add2 = p.transform.scale(add,(20,20))
add2R = add2.get_rect()
add2R.topleft = (250,150)
add3 = p.transform.scale(add,(20,20))
add3R = add3.get_rect()
add3R.topleft = (250,200)
add4 = p.transform.scale(add,(20,20))
add4R = add4.get_rect()
add4R.topleft = (250,250)
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
downs = p.transform.scale(selector,(25,25))
downsR = downs.get_rect()
downsR.topleft = (200,40)
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
stats = p.image.load('icons/sta.png')
stat = p.transform.scale(stats,(20,20))