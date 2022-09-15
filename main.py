#net dmg = attack dmg - def × factor , where factor is 0.5 in Classic Mode, 0.75 in Expert Mode, and 1 in Master Mode.
import pygame as p
p.font.init()
ds = p.display.set_mode((500, 300))  # create display
white = (255, 255, 255)
Empty= p.image.load('box.png')
x = 0
y = 0
s=0
black = (0,0,0)
Stick = p.image.load('stick.png')
Wsword = p.image.load('woodsword.png')
inv=[Empty,Empty,Empty,Empty,Empty,Empty,Empty,Empty]
pressed = p.key.get_pressed()
value = 0
tryhard = 0
P = 0
S = 0
wi = 87
T = 1
L=50
var = [[0,Stick],[0,Wsword],0]
color2 = (255,255.255)
itemid=[[0,Empty],[1,Stick],[2,Wsword]]
mx,my = p.mouse.get_pos()
Eq = ["Armor", "Weapon", "Potion"]
ES = p.image.load("box.png")
selectedSlot = None
selectedSlot2 = None
def collision(x,y,x2,y2,w):
    if x + w > x2 > x and y+w > y2 > y:
        return True
    else:
        return False
class Slots(object):
  def __init__(self,x,y):
    self.tx = x + 20
    self.ty = y + 50
  def draw(self,ds):
        #Draws the slots using the x and y values 
        p.draw.rect(ds,(color2),   (self.tx,self.ty,50,50))
        if collision(self.tx,self.ty,mx,my,60): 
            global selectedSlot
            p.draw.rect(ds,(128,0,0),(self.tx,self.ty,50,50))
class Slots2(object):
  def __init__(self,x,y):
    self.X = x + 20
    self.Y = y + 150
  def draw2(self,ds):
        #Draws the slots using the x and y values 
        p.draw.rect(ds,(color2),   (self.X,self.Y,50,50))
        if collision(self.X,self.Y,mx,my,60): 
            global selectedSlot2
            p.draw.rect(ds,(128,0,0),(self.X,self.Y,50,50))
    
slotArray = []
#Slot information
slotCount = 4
while len(slotArray) != slotCount:
  slotArray.append(Slots(30+len(slotArray)*100,50))
slotArray2 = []
#Slot information
slotCount2 = 4
while len(slotArray2) != slotCount2:
  slotArray2.append(Slots2(30+len(slotArray2)*100,50))
color = black
clock = p.time.Clock()
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
g5 = Di
P1 =  p.transform.scale(g5, (wi, 100))


# make charecter
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


mc = Player()
drawGrid = False
class items(object):
    def __init__(self,x,y):
      self.image1 = (Stick)
      self.image2 = (Wsword)
      self.x = 50
      self.y = 50
      self.x2 = self.x + 50
      self.y2 = self.y + 50
      self.rect1 = self.image1.get_rect()
      self.rect1.center = (self.x,self.y)
      self.rect2 = self.image2.get_rect()
      self.rect2.center = (self.x2,self.y2)
Items= items(50,50)

def drawG():
    blockSize = 50  #Set the size of the grid block
    for x in range(0, 500, blockSize):
        for y in range(0, 300, blockSize):
            rect = p.Rect(x, y, blockSize, blockSize)
            p.draw.rect(ds, black, rect, 1)


font = p.font.Font('freesansbold.ttf', 32)
font2 = p.font.Font('freesansbold.ttf', 20)
text = font.render('Pause', True, color, white)
text2 = font2.render('Party (press 1)', True, color, white)
text3 = font2.render('Settings (press 2)', True, color, white)
text4 = font2.render('Back (press esc)', True, color, white)
text5 = font.render('There Are No Settings', True, color, white)
text6 = font2.render('Inventory full', True, color, white)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect.center = (250, 50)
textRect2.center = (250, 75)
textRect3.center = (250, 100)
textRect4.center = (250, 125)
textRect5.center = (250, 75)
def additem(object):
  if inv[0] == Empty:
    inv[0]=(object)
    return True
  elif inv[1] == Empty:
    inv[1]=(object)
    return True
  elif inv[2] == Empty:
    inv[2]=(object)
    return True
  elif inv[3] == Empty:
    inv[3]=(object)
    return True
  elif inv[4] == Empty:
    inv[4]=(object)
    return True
  elif inv[5] == Empty:
    inv[5]=(object)
    return True
  elif inv[6] == Empty:
    inv[6]=(object)
    return True
  elif inv[7] == Empty:
    inv[7]=(object)
    return True
  else:
    ds.blit(text6, textRect)
    return False
def colI(obj):
  C = obj.colliderect(mc.rect) 
  if C:
      return True
def item(num,id,X,Y,width,height):
  global x,y
  global var
  picture = p.transform.scale(id,(width,height))
  if var[num][0]==0:
    name=ds.blit(picture, (x+X, y+Y))
    if colI(name):
      if additem(id):
        var[num][0]=1
r = True
# when the game is active
while r:
    mx,my = p.mouse.get_pos()
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.KEYUP:
            if event.key == p.K_e:
                if S == 0:
                    S = 1
                    event.key = p.K_p
                elif event.key == p.K_e:
                    S = 0
                    event.key = p.K_p
            elif event.key == p.K_ESCAPE:
                if S == 0:
                    S = 2
                    event.key = p.K_p
                    P = 1
                elif S == 1:
                    S = 2
                    event.key = p.K_p
                    P = 2
                elif S == 2 and P == 1:
                    S = 0
                    event.key = p.K_p
                elif S == 2 and P == 2:
                    S = 1
                    event.key = p.K_p
                elif S == 3:
                    S = 2
                    event.key = p.K_p
            elif event.key == p.K_2:
                if S == 2:
                    S = 3
                    event.key = p.K_p
            if event.key == p.K_EQUALS:
                if drawGrid == False:
                    drawGrid = True
                    event.key = p.K_p
                else:
                    drawGrid = False
                    event.key = p.K_p
    rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
    if drawGrid:
            drawG()
    #overworld
    if S == 0:
        ds.fill(white)
        ds.blit(mc.image, (mc.x, mc.y))
        rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
        P1 = p.transform.scale(g5, (wi, 100))
        mc.image = P1
        item(s,itemid[1][1],-50,-100,75,100)
        if drawGrid:
            drawG()
        if value >= len(Ua):
            value = 0
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
#movement for the player
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                g5 = La[value]
                x += 5
                wi = 77
            if event.key == p.K_RIGHT:
                g5 = Ra[value]
                x -= 5
                wi = 77
            if event.key == p.K_UP:
                g5 = Ua[value]
                y += 5
                wi = 77
            if event.key == p.K_DOWN:
                g5 = Da[value]
                y -= 5
                wi = 87
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                g5 = Li
            if event.key == p.K_RIGHT:
                g5 = Ri
            if event.key == p.K_UP:
                g5 = Ui
            if event.key == p.K_DOWN:
                g5 = Di
#inventory screen
    elif S == 1:
        Slot1 = p.transform.scale(inv[0], (50, 50))
        Slot2 = p.transform.scale(inv[1], (50, 50))
        Slot3 = p.transform.scale(inv[2], (50, 50))
        Slot4 = p.transform.scale(inv[3], (50, 50))
        Slot5 = p.transform.scale(inv[4], (50, 50))
        Slot6 = p.transform.scale(inv[5], (50, 50))
        Slot7 = p.transform.scale(inv[6], (50, 50))
        Slot8 = p.transform.scale(inv[7], (50, 50))
        if not drawGrid:
          ds.fill(color)
          color2 = (255,255,255)
        else:
          ds.fill(white)
          color2 = (0,0,0)
        for i in slotArray:
          i.draw(ds)
        for i in slotArray2:
          i.draw2(ds)
        if drawGrid:
            drawG()
        ds.blit(Slot1,(50,100))
        ds.blit(Slot2,(150,100))
        ds.blit(Slot3,(250,100))
        ds.blit(Slot4,(350,100))
        ds.blit(Slot5,(50,200))
        ds.blit(Slot6,(150,200))
        ds.blit(Slot7,(250,200))
        ds.blit(Slot8,(350,200))

        
        
#menu screen
    elif S == 2:
        ds.fill(white)
        ds.blit(text, textRect)
        ds.blit(text2, textRect2)
        ds.blit(text3, textRect3)
        ds.blit(text4, textRect4)
    elif S == 3:
        ds.fill(white)
        ds.blit(text5, textRect5)
        ds.blit(text4, textRect4)

    collideU = rect1.collidepoint(mc.rect.topleft) or rect1.collidepoint(
        mc.rect.topright) or rect1.collidepoint(mc.rect.midtop)
    collideD = rect1.collidepoint(mc.rect.midbottom) or rect1.collidepoint(
        mc.rect.bottomleft) or rect1.collidepoint(mc.rect.bottomright)
    collideR = rect1.collidepoint(mc.rect.midright) or rect1.collidepoint(
        mc.rect.topright) or rect1.collidepoint(mc.rect.bottomright)
    collideL = rect1.collidepoint(mc.rect.midleft) or rect1.collidepoint(
        mc.rect.topleft) or rect1.collidepoint(mc.rect.bottomleft)
    if collideL:
        x -= 10
    if collideR:
        x += 10
    if collideU:
        y -= 10
    if collideD:
        y += 10
    p.display.flip()  # update display
    tryhard += 1
    if drawGrid:
            drawG()
    if tryhard == 10:
        value += 1
        tryhard = 0
