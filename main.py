#net dmg = attack dmg - def × factor , where factor is 0.5 in Classic Mode, 0.75 in Expert Mode, and 1 in Master Mode.
#a,b = b,a
#array[0][1],array[1][1] = arrray[1][1],array[0][1]
import pygame as p
import os
import random
ahhhhhhhh = []
yes = 0
pbw = 200
pbh = 225
pbx = 80
pby = 80
ebw = 50
ebh = 50
ebx = 350
eby = 50
p.font.init()
ds = p.display.set_mode((500, 300))  # create display
white = (255, 255, 255)
Empty= p.image.load('box.png')
temp = p.image.load('temp.png')
green = (0,255,0)
red = (255,0,0)
x = 0
y = 0
trrr=0
var2 = 0
grey = (10,10,10)
test = p.mouse.get_pressed()[0]
array=[[0,0],[0,0]]
t = 0
SelectedSlot = False
clicked = 0
Slot1=0
Slot2=0
Slot3=0
Slot4=0
Slot5=0
Slot6=0
Slot7=0
Slot8 =0
black = (0,0,0)
Stick = p.image.load('Items/stick.png')
Wsword = p.image.load('Items/woodsword.png')
Isword = p.image.load('Items/ironsword.png')
inv=[Empty,Empty,Empty,Empty,Empty,Empty,Empty,Empty,Stick,Empty,Empty]
pressed = p.key.get_pressed()
value = 0
tryhard = 0
P = 0
S = 0
wi = 87
T = 1
#THE THING GO TING THE THIGN THERE YES YUP 
L=50
#AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
ahh = 0
var = [[0,Stick],[0,Wsword],[0,Isword]]
color2 = (255,255.255)
slotitemid ={
  Empty:0,
  Stick:1,
  Wsword:2,
  Isword:3,
}
itemid = {
  0:Empty,
  1:Stick,
  2:Wsword,
  3:Isword,
}
#[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
itemstats={
  0:[0,0,0,0,0,0,0],
  #Stick
  1:[0,1,0,0,0,1,1],
  #Wsword
  2:[0,2,0,0,0,1,1],
  #Isword
  3:[0,3,0,0,0,1,1],
}
#[defense,attack,maxhp,hp,mana]
Enemystats={
  temp:[0,1,5,5,0],
}
varEn=[[0,temp],[0,temp]]
enemy={
  0:temp,
}
class Player(object):
    def __init__(self):
        super().__init__()
        self.image = (P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)
        self.defense = 1
        self.attack = 1
        self.Hp = 20
        self.maxHp = 20
        self.mana = 0
        self.luck = 0
        self.name = 0
hmmm=temp
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
enem=Enemy()
mx,my = p.mouse.get_pos()
Eq = ["Armor", "Weapon", "Potion"]
ES = p.image.load("box.png")
slotItem = None
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
    global slotItem
        #Draws the slots using the x and y values 
    p.draw.rect(ds,(color2),   (self.tx,self.ty,50,50))
    if collision(self.tx,self.ty,mx,my,60): 
      p.draw.rect(ds,(128,0,0),(self.tx,self.ty,50,50))
          
class Slots2(object):
  def __init__(self,x,y):
    self.X = x + 20
    self.Y = y + 150
  def draw2(self,ds):
        #Draws the slots using the x and y values 
        p.draw.rect(ds,(color2),   (self.X,self.Y,50,50))
        if collision(self.X,self.Y,mx,my,60): 
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
battleP1 = p.image.load('I/battle.png')
g5 = Di
P1 =  p.transform.scale(g5, (wi, 100))
def checkslot():
  global slotItem
  global mx,my
  if collision(50,100,mx,my,60):
    slotItem = slotitemid[inv[0]]
  elif collision(150,100,mx,my,60):
    slotItem = slotitemid[inv[1]]
  elif collision(250,100,mx,my,60):
    slotItem = slotitemid[inv[2]]
  elif collision(350,100,mx,my,60):
    slotItem = slotitemid[inv[3]]
  elif collision(50,200,mx,my,60):
    slotItem = slotitemid[inv[4]]
  elif collision(150,200,mx,my,60):
    slotItem = slotitemid[inv[5]]
  elif collision(250,200,mx,my,60):
    slotItem = slotitemid[inv[6]]
  elif collision(350,200,mx,my,60):
    slotItem = slotitemid[inv[7]]
  else:
    slotItem = None
def slotselect():
  global SelectedSlot, t,array
  mx,my=p.mouse.get_pos()
  test = p.mouse.get_pressed()[0]
  if test and collision(50,100,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 1
      array[0][1]= slotitemid[inv[0]]
    elif array[1][0]==0:
      array[1][0] = 1
      array[1][1]= slotitemid[inv[0]]
    t=1
  if test and collision(150,100,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 2
      array[0][1]= slotitemid[inv[1]]
    elif array[1][0]==0:
      array[1][0] = 2
      array[1][1]= slotitemid[inv[1]]
    t=1
  if test and collision(250,100,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 3
      array[0][1]= slotitemid[inv[2]]
    elif array[1][0]==0:
      array[1][0] = 3
      array[1][1]= slotitemid[inv[2]]
    t=1
    SelectedSlot = 3
  if test and collision(350,100,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 4
      array[0][1]= slotitemid[inv[3]]
    elif array[1][0]==0:
      array[1][0] = 4
      array[1][1]= slotitemid[inv[3]]
    t=1
  if test and collision(50,200,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 5
      array[0][1]= slotitemid[inv[4]]
    elif array[1][0]==0:
      array[1][0] = 5
      array[1][1]= slotitemid[inv[4]]
    t=1
  if test and collision(150,200,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 6
      array[0][1]= slotitemid[inv[5]]
    elif array[1][0]==0:
      array[1][0] = 6
      array[1][1]= slotitemid[inv[5]]
    t=1
  if test and collision(250,200,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 7
      array[0][1]= slotitemid[inv[6]]
    elif array[1][0]==0:
      array[1][0] = 7
      array[1][1]= slotitemid[inv[6]]
    t=1
  if test and collision(350,200,mx,my,50) and t==0:
    if array[0][0]==0:
      array[0][0] = 8
      array[0][1]= slotitemid[inv[7]]
    elif array[1][0]==0:
      array[1][0] = 8
      array[1][1]= slotitemid[inv[7]]
    t=1
  if test and collision(50,0,mx,my,50) and t==0:
    if array[1][0]==0 and 0<array[0][1]<=3:
      array[1][0] = 9
      array[1][1]= slotitemid[inv[8]]
    t=1
  if test and collision(150,0,mx,my,50) and t==0:
    if array[1][0]==0 and 3<array[0][1]<=10:
      array[1][0] = 10
      array[1][1]= slotitemid[inv[9]]
    t=1
  if test and collision(250,0,mx,my,50) and t==0:
    if array[1][0]==0 and 10<array[0][1]<=13:
      array[1][0] = 10
      array[1][1]= slotitemid[inv[10]]
    t=1
  if not test:
    t=0
  if not array[1][0]==0:
    array[0][1],array[1][1]=array[1][1],array[0][1]
    inv[(array[0][0]-1)] = itemid[array[0][1]]
    inv[(array[1][0]-1)] = itemid[array[1][1]]
    array = [[0,0],[0,0]]
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
ahhh = mc.Hp
font999 = p.font.Font('freesansbold.ttf', 50)
text999 = font999.render('YOU DIED', True, red, black)
textRect999 = text999.get_rect()
textRect999.center = (250,150)
fonthp = p.font.Font('freesansbold.ttf', 10)
textHp = fonthp.render(str(mc.Hp), True, black)
textt = fonthp.render('/', True, black)
textmaxHp = fonthp.render(str(mc.maxHp), True, black)
textRectHp = textHp.get_rect()
textRectHp.center = (30,220)
textRectt = textt.get_rect()
textRectt.center = (50,220)
textRectmaxHp = textmaxHp.get_rect()
textRectmaxHp.center = (60,220)



font = p.font.Font('freesansbold.ttf', 32)
font2 = p.font.Font('freesansbold.ttf', 20)
font3 = p.font.Font('freesansbold.ttf', 18)
text = font.render('Pause', True, color, white)
text2 = font2.render('Party', True, color, white)
text3 = font2.render('Settings', True, color, white)
text4 = font2.render('Back', True, color, white)
text5 = font.render('There Are No Settings', True, color, white)
text6 = font2.render('Inventory full', True, color, white)
text7 = font3.render('Attack',True, white,grey)
text8 = font3.render('Defend',True, white,grey)
text9 = font3.render('Magic',True, white,grey)
text10 = font3.render('Potion',True, white,grey)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect7 = text7.get_rect()
textRect8 = text8.get_rect()
textRect9 = text9.get_rect()
textRect10 = text10.get_rect()
textRect.center = (250, 50)
textRect2.center = (250, 75)
textRect3.center = (250, 100)
textRect4.center = (250, 125)
textRect5.center = (250, 75)
textRect7.center = (360, 250)
textRect8.center = (440, 250)
textRect9.center = (360, 290)
textRect10.center = (440, 290)
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
def ENEMY(num,image,X,Y,width,height):
  global varEn,S,hmmm,ahhhhhhhh
  picture = p.transform.scale(image,(width,height))
  if len(ahhhhhhhh)<=num:
    name=ds.blit(picture, (x+X, y+Y))
    if colI(name):
      hmmm = image
      S=21
      ahhhhhhhh.append(0)
r = True
def collide(obje):
  if (obje).collidepoint(mc.rect.topleft) or (obje).collidepoint(
        mc.rect.topright) or (obje).collidepoint(mc.rect.midtop):
          return True
  if (obje).collidepoint(mc.rect.midbottom) or (obje).collidepoint(
        mc.rect.bottomleft) or rect1.collidepoint(mc.rect.bottomright):
          return True
  if (obje).collidepoint(mc.rect.midright) or (obje).collidepoint(
        mc.rect.topright) or (obje).collidepoint(mc.rect.bottomright):
          return True
  if (obje).collidepoint(mc.rect.midleft) or (obje).collidepoint(
        mc.rect.topleft) or (obje).collidepoint(mc.rect.bottomleft):
          return True
def mouseover(rect):
  global my,mx
  mx,my=p.mouse.get_pos()
  test = p.mouse.get_pressed()[0]
  if rect.collidepoint(mx,my):
    if test:
      return True
      print(rect)
# when the game is active
os.system('clear')
s=Enemy()
at=0
de=0
#DAMAGE
#CALCULATION
#AND
#GAME
def damage(wih,wht):
  wih.Hp -= wht.attack+(random.randrange(1,3,1))-wih.defense
  
while r:
    mx,my = p.mouse.get_pos()
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.KEYUP:
            if event.key == p.K_e:
                if S == 0:
                    S = 1
                    event.key = p.K_p
                elif event.key == p.K_e and S==1:
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
            if event.key == p.K_EQUALS:
                if drawGrid == False:
                    drawGrid = True
                    event.key = p.K_p
                else:
                    drawGrid = False
                    event.key = p.K_p
    if mouseover(textRect3) and S == 2:
      S=3
      ahh = 1
    if trrr==0:
      if  mouseover(textRect4) and ahh==1:
        S=2
        ahh = 0
        trrr=1
      elif mouseover(textRect4) and P==1:
        S=0
        trrr=1
      elif mouseover(textRect4) and P==2:
        S=1
        trrr=1
    if not mouseover(textRect4):
      trrr=0
    rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
    if drawGrid:
            drawG()
    #overworld
    if S == 0:
        yes =0
        P=0
        array = [[0,0],[0,0]]
        ds.fill(white)
        ds.blit(mc.image, (mc.x, mc.y))
        rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
        P1 = p.transform.scale(g5, (wi, 100))
        mc.image = P1
        item(1,itemid[2],-50,100,50,50)
        item(2,itemid[3],500,150,50,50)
        ENEMY(0,enemy[0],100,200,50,50)
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
        ESlotA = p.transform.scale(inv[8], (50,50))
        ESlotW = p.transform.scale(inv[9], (50,50))
        ESlotP = p.transform.scale(inv[10], (50,50))
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
        EquipArm=p.draw.rect(ds,color2,p.Rect(50,0,50,50))
        EquipWeap=p.draw.rect(ds,color2,p.Rect(150,0,50,50))
        EquipPot=p.draw.rect(ds,color2,p.Rect(250,0,50,50))
        S1=ds.blit(Slot1,(50,100))
        ds.blit(Slot2,(150,100))
        ds.blit(Slot3,(250,100))
        ds.blit(Slot4,(350,100))
        ds.blit(Slot5,(50,200))
        ds.blit(Slot6,(150,200))
        ds.blit(Slot7,(250,200))
        ds.blit(Slot8,(350,200))
        ds.blit(ESlotA,(50,0))
        ds.blit(ESlotW,(150,0))
        ds.blit(ESlotP,(250,0))
      
        slotselect()
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
    elif S == 21:
      textHp = fonthp.render(str(mc.Hp), True, black)
      textt = fonthp.render('/', True, black)
      textmaxHp = fonthp.render(str(mc.maxHp), True, black)
      if yes==0:
        save = g5
        g5 = battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
        mc.defense += itemstats[slotitemid[inv[8]]][0]
        mc.defense += itemstats[slotitemid[inv[9]]][0]
        mc.attack += itemstats[slotitemid[inv[8]]][1]
        mc.attack += itemstats[slotitemid[inv[9]]][1]
        enem.defense += Enemystats[enem.image][0]
        enem.attack += Enemystats[enem.image][1]
        enem.maxHp += Enemystats[enem.image][2]
        enem.Hp += Enemystats[enem.image][3]
        enem.mana += Enemystats[enem.image][4]
        yes = 1
      P1 = p.transform.scale(g5,(pbw,pbh))
      playerhp = (mc.Hp/mc.maxHp)*100
      enemhp = (enem.Hp/enem.maxHp)*100
      ds.fill(white)
      enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
      playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
      eh=p.transform.scale(enem.image,(50,50))
      ds.blit(eh,(350,50))
      ds.blit(P1,(pbx,pby))
      p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
      ds.blit(textHp,textRectHp)
      ds.blit(textt,textRectt)
      ds.blit(textmaxHp,textRectmaxHp)
      ds.blit(text7, textRect7)
      ds.blit(text8, textRect8)
      ds.blit(text9, textRect9)
      ds.blit(text10, textRect10)
      if mouseover(textRect7):
        if de == 0:
          while at<=21:
              clock.tick(60)
              at+=1
              pbx +=11
              pby -=5
              pbh -=4
              pbw-=4
              print(at)
              P1 = p.transform.scale(g5,(pbw,pbh))
              playerhp = (mc.Hp/mc.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(enem.image,(ebw,ebh))
              ds.blit(eh,(ebx,eby))
              ds.blit(P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              ds.blit(textt,textRectt)
              ds.blit(textmaxHp,textRectmaxHp)
              p.display.flip()
          damage(enem,mc)
          ds.fill(white)
          enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
          playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
          eh=p.transform.scale(enem.image,(50,50))
          ds.blit(eh,(350,50))
          ds.blit(P1,(pbx,pby))
          p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
          ds.blit(textHp,textRectHp)
          ds.blit(textt,textRectt)
          ds.blit(textmaxHp,textRectmaxHp)
          while at>=1:
              clock.tick(60)
              at-=1
              pbx -=11
              pby +=5
              pbh +=4
              pbw+=4
              print(at)
              P1 = p.transform.scale(g5,(pbw,pbh))
              playerhp = (mc.Hp/mc.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(enem.image,(50,50))
              ds.blit(eh,(350,50))
              ds.blit(P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              ds.blit(textt,textRectt)
              ds.blit(textmaxHp,textRectmaxHp)
              p.display.flip()
          while at<=21:
              clock.tick(60)
              at+=1
              ebx -=11
              eby +=5
              ebh +=2
              ebw+=2
              print(at)
              P1 = p.transform.scale(g5,(pbw,pbh))
              playerhp = (mc.Hp/mc.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(enem.image,(ebw,ebh))
              ds.blit(eh,(ebx,eby))
              ds.blit(P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              ds.blit(textt,textRectt)
              ds.blit(textmaxHp,textRectmaxHp)
              p.display.flip()
          damage(mc,enem)
          ds.fill(white)
          enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
          playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
          eh=p.transform.scale(enem.image,(ebw,ebh))
          ds.blit(eh,(ebx,eby))
          ds.blit(P1,(pbx,pby))
          p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
          ds.blit(textHp,textRectHp)
          ds.blit(textt,textRectt)
          ds.blit(textmaxHp,textRectmaxHp)
          p.display.flip()
          while at>=1:
              clock.tick(60)
              at-=1
              ebx +=11
              eby -=5
              ebh -=2
              ebw-=2
              print(at)
              P1 = p.transform.scale(g5,(pbw,pbh))
              playerhp = (mc.Hp/mc.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(enem.image,(ebw,ebh))
              ds.blit(eh,(ebx,eby))
              ds.blit(P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              ds.blit(textt,textRectt)
              ds.blit(textmaxHp,textRectmaxHp)
              p.display.flip()
          de=1
      elif not mouseover(textRect7):
        de=0
      if mouseover(textRect8):
        pbx-=20
        pby+=15
        print(de)
      if enem.Hp<=0:
        g5=save
        S=0
        
    elif S == None:
      ds.fill(black)
      ds.blit(text999,textRect999)
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
    if mc.Hp<= 0:
      S=None
