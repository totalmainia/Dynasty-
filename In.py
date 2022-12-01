import pygame as p
import im
import sta
ds = p.display.set_mode((500, 300))
mx,my=p.mouse.get_pos()
array=[[0,0],[0,0]]
black = (0,0,0)
color2 = (255,255,255)
white = (255,255,255)
color = black
p.font.init()
font = p.font.Font('freesansbold.ttf', 32)
font2 = p.font.Font('freesansbold.ttf', 20)
text = font.render('Pause', True, color, white)
text6 = font2.render('Inventory full', True, color, white)
textRect = text.get_rect()
textRect.center = (250, 50)
inv=[im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty,im.Empty]
playerinv=[im.Stick,im.Empty,im.Empty]
pm1inv=[im.Wsword,im.Empty,im.Empty]
pm2inv=[im.Wsword,im.Empty,im.Empty]
currentinv=1
Slot1=0
Slot2=0
Slot3=0
Slot4=0
Slot5=0
Slot6=0
Slot7=0
Slot8 =0
slotitemid ={
  im.Empty:0,
  im.Stick:1,
  im.Wsword:2,
  im.Isword:3,
}
itemid = {
  0:im.Empty,
  1:im.Stick,
  2:im.Wsword,
  3:im.Isword,
}
playerslotitem = [slotitemid[playerinv[0]],slotitemid[playerinv[1]],slotitemid[playerinv[2]]]
pm1slotitem = [slotitemid[pm1inv[0]],slotitemid[pm1inv[1]],slotitemid[pm1inv[2]]]
pm2slotitem = [slotitemid[pm2inv[0]],slotitemid[pm2inv[1]],slotitemid[pm2inv[2]]]
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
direction = 1
def checkslot():
  global slotItem,playerslotitem,pm1slotitem,pm2slotitem
  playerslotitem = [slotitemid[playerinv[0]],slotitemid[playerinv[1]],slotitemid[playerinv[2]]]
  pm1slotitem = [slotitemid[pm1inv[0]],slotitemid[pm1inv[1]],slotitemid[pm1inv[2]]]
  pm2slotitem = [slotitemid[pm2inv[0]],slotitemid[pm2inv[1]],slotitemid[pm2inv[2]]]
  slotItem = [slotitemid[inv[0]],slotitemid[inv[1]],slotitemid[inv[2]],slotitemid[inv[3]],slotitemid[inv[4]],slotitemid[inv[5]],slotitemid[inv[6]],slotitemid[inv[7]],slotitemid[inv[8]],slotitemid[inv[9]],slotitemid[inv[10]]]
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
    sta.mc.defense = sta.mcstats[0]+sta.itemstats[slotitemid[inv[8]]][0] +sta.itemstats[slotitemid[inv[9]]][0]
    sta.mc.attack = sta.mcstats[1]+sta.itemstats[slotitemid[inv[8]]][1] +sta.itemstats[slotitemid[inv[9]]][1]
    sta.mc.maxHp = sta.mcstats[2]+sta.itemstats[slotitemid[inv[8]]][2] +sta.itemstats[slotitemid[inv[9]]][2]
    sta.mc.mana = sta.mcstats[3]+sta.itemstats[slotitemid[inv[8]]][3] +sta.itemstats[slotitemid[inv[9]]][3]
    sta.mc.luck = sta.mcstats[4]+sta.itemstats[slotitemid[inv[8]]][3] +sta.itemstats[slotitemid[inv[9]]][3]
def additem(object):
  if inv[0] == im.Empty:
    inv[0]=(object)
    return True
  elif inv[1] == im.Empty:
    inv[1]=(object)
    return True
  elif inv[2] == im.Empty:
    inv[2]=(object)
    return True
  elif inv[3] == im.Empty:
    inv[3]=(object)
    return True
  elif inv[4] == im.Empty:
    inv[4]=(object)
    return True
  elif inv[5] == im.Empty:
    inv[5]=(object)
    return True
  elif inv[6] == im.Empty:
    inv[6]=(object)
    return True
  elif inv[7] == im.Empty:
    inv[7]=(object)
    return True
  else:
    ds.blit(text6, textRect)
    return False
def colI(obj):
  C = obj.colliderect(sta.mc.rect) 
  if C:
      return True