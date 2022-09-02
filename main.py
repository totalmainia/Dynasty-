import pygame as p
ds=p.display.set_mode((500,300))# create display
white = (255,255,255)
d = 1
x=0
y=0
value = 0
tryhard = 0
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
black = (0,0,0)
drawGrid = False
def drawG():
    blockSize = 50 #Set the size of the grid block
    for x in range(0, 500, blockSize):
        for y in range(0, 300, blockSize):
            rect = p.Rect(x, y, blockSize, blockSize)
            p.draw.rect(ds, black, rect, 1)
r= True
rect1 =p.draw.rect(ds,black,p.Rect(x, y, 50, 50))
# when the game is active
while r:
  clock.tick(60)
  ds.fill(white)
  ds.blit(mc.image,(mc.x,mc.y))
  P1 = p.transform.scale(g5,(75,100))
  collide = rect1.colliderect(mc.rect)
  color = (255, 0, 0) if collide else (black)
  rect1 =p.draw.rect(ds,color,p.Rect(x, y, 50, 50))
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
          if not d==2:
           x+=5
          if  collide:
            x-=10
            d = 2
        if event.key == p.K_RIGHT:
          g5 = Ra[value]
          if not d==4:
           x-=5
          if  collide:
            x+=10
            d = 4
        if event.key == p.K_UP:
          g5 = Ua[value]
          if not d == 3:
           y+=5
          if  collide:
            y-=10
            d = 3
        if event.key == p.K_DOWN:
         g5 = Da[value]
         if not d == 1:
           y-=5
         if  collide:
           y+=10
           d = 1
  if event.type == p.KEYUP:
     if event.key == p.K_LEFT:
       g5 = Li
     if event.key == p.K_RIGHT:
       g5 = Ri
     if event.key == p.K_UP:
       g5 = Ui
     if event.key == p.K_DOWN:
       g5 = Di
     if event.key == p.K_EQUALS:
       if drawGrid == False:
         drawGrid= True
  if event.type == p.KEYUP:
      if event.key == p.K_MINUS and drawGrid:
       drawGrid= False
  if collide and d == 3:
   y-=10
  elif collide and d == 1:
    y+=10
  elif collide and d == 4:
    x+=10
  elif collide and d == 2:
    x-=10
  p.display.flip()# update display
  tryhard += 1
  if tryhard == 10:
    value += 1
    tryhard = 0