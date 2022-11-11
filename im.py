import pygame as p
import s
clock = p.time.Clock()
wi = 87
temp = p.image.load('temp.png')
ES = p.image.load("box.png")
Empty= p.image.load('box.png')
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
dt = 0
timer = 0
image_bright =0

party1 = battleP1
party2 = battleP1

#def blink(image_normal,color,x,y,width,length,lengthofblink):
 # global once,image_bright,timer,dt,clock
  #if once == 0:
   # clock = p.time.Clock()
    #image_normal = p.Surface((width, length))
    #image_normal.fill(p.Color(color))
    #image_bright = image_normal.copy()
    #image_bright.fill((0, 200, 0, 128),           special_flags=p.BLEND_RGBA_ADD)
    #image = image_normal  # The currently selected image.
    #once = 1
  #for event in p.event.get():
    #if event.type == p.MOUSEBUTTONDOWN:
            #image = image_bright  # Swap the image.
            #timer = .5  # 0.5 seconds.

    #timer -= dt
    #if timer <= 0:
        #image = image_normal  # Set the image back to the normal version.
        #timer = 0

    #ds.blit(image, (x, y))
    #p.display.flip()
    #dt = clock.tick(60) / 100
