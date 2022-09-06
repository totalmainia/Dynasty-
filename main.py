import pygame as p
ds=p.display.set_mode((500,300))# create display
white = (255,255,255)
x=0
y=0
value = 0
tryhard = 0
black = (0,0,0)
color=black
clock = p.time.Clock()
# idle and animations for main charecter 
Di = p.image.load('I/downi.png')
Da = [p.image.load('I/down2.png'),p.image.load('I/down3.png')]
Ui = p.image.load('I/upi.png')
Ua = [p.image.load('I/up2.png'),p.image.load('I/up3.png')]
Li = p.image.load('I/lefti.png')
La = [p.image.load('I/left2.png'),p.image.load('I/lefti.png'),p.image.load('I/left3.png')]
Ri = p.image.load('I/righti.png')
Ra = [p.image.load('I/right2.png'),p.image.load('I/righti.png'),p.image.load('I/right3.png')]
g5 = Di
P1 = p.transform.scale(g5,(75,100))
# make charecter 
class Player(object):
 def __init__(self):
  super().__init__()
  self.image = (P1)
  self.x = 212
  self.y = 100
  self.rect = self.image.get_rect()
  self.rect.center = (250,150)
mc = Player()
drawGrid = False
def drawG():
    blockSize = 50 #Set the size of the grid block
    for x in range(0, 500, blockSize):
        for y in range(0, 300, blockSize):
            rect = p.Rect(x, y, blockSize, blockSize)
            p.draw.rect(ds, black, rect, 1)
r= True
# when the game is active
while r:
  clock.tick(60)
  ds.fill(white)
  ds.blit(mc.image,(mc.x,mc.y))
  P1 = p.transform.scale(g5,(75,100))
  rect1 = p.draw.rect(ds, color, p.Rect(x,y,50,50))
  collideU = rect1.collidepoint(mc.rect.topleft) or rect1.collidepoint(mc.rect.topright) or rect1.collidepoint(mc.rect.midtop)
  collideD = rect1.collidepoint(mc.rect.midbottom) or rect1.collidepoint(mc.rect.bottomleft) or rect1.collidepoint(mc.rect.bottomright)
  collideR = rect1.collidepoint(mc.rect.midright) or rect1.collidepoint(mc.rect.topright) or rect1.collidepoint(mc.rect.bottomright)
  collideL = rect1.collidepoint(mc.rect.midleft) or rect1.collidepoint(mc.rect.topleft) or rect1.collidepoint(mc.rect.bottomleft)
  color = (255,0,0) if collideU else (black)
  mc.image = P1
  if drawGrid:
     drawG()
  if value >= len(Ua):
      value = 0
  for event in p.event.get() :
      if event.type == p.QUIT:
          p.quit()
  #movement for the player
  if event.type == p.KEYDOWN:
        if event.key == p.K_LEFT:
          g5 = La[value]
          x+=5
        if event.key == p.K_RIGHT and d<=0:
          g5 = Ra[value]
          x-=5
        if event.key == p.K_UP and d<=0:
          g5 = Ua[value]
          y+=5
        if event.key == p.K_DOWN and d<=0:
          g5 = Da[value]
          y-=5
  if event.type == p.KEYUP:
     if event.key == p.K_LEFT and d<=0:
       g5 = Li
     if event.key == p.K_RIGHT and d<=0:
       g5 = Ri
     if event.key == p.K_UP and d<=0:
       g5 = Ui
     if event.key == p.K_DOWN and d<=0:
       g5 = Di
     if event.key == p.K_EQUALS:
       if drawGrid == False:
         drawGrid= True
  if event.type == p.KEYUP:
      if event.key == p.K_MINUS and drawGrid:
       drawGrid= False
  if collideL:
      x-=10
  if collideR:
      x+=10
  if collideU:
      y-=10
  if collideD:
      y+=10
  p.display.flip()# update display
  tryhard += 1
  if tryhard == 10:
    value += 1
    tryhard = 0
  