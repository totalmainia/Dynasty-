
#net dmg = attack dmg - def × 0.5
#a,b = b,a
#array[0][1],array[1][1] = arrray[1][1],array[0][1]
import pygame as p
import os, json, sta, im, In, Xp,text, s,battle,random
texttracker = 0
textamount = 0
direction = 1
textbox = False
collideU= False
collideR = False
collideL = False
collideD = False
room = 0
password=''
clock = p. time.Clock()
Trash = p.image.load('icons/trash-2.svg')
Trash_rect1= Trash.get_rect()
Trash_rect1.center = (400,50)
Trash_rect2= Trash.get_rect()
Trash_rect2.center = (400,120)
Trash_rect3= Trash.get_rect()
Trash_rect3.center = (400,190)
Trash_rect4= Trash.get_rect()
Trash_rect4.center = (400,260)
white = (255, 255,255,255)
green = (0,255,0,255)
red = (255,0,0,255)
grey = (10,10,10,255)
black = (0,0,0,255)
black_faded = (0,0,0,128)
color2 = (255,255.255,255)
color = black
savefile=0
ahhhhhhhh = []
p.font.init() #create display
x = 0
y = 0
trrr=0
var2 = 0
test = p.mouse.get_pressed()[0]
t = 0
SelectedSlot = False
clicked = 0
pressed = p.key.get_pressed()
value = 0
tryhard = 0
P = 0
T = 1
#THE THING GO TING THE THIGN THERE YES YUP 
L=50
#AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
ahh = 0
var = [[0],[0],[0]]
#[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
mx,my = p.mouse.get_pos()
slotItem = None
selectedSlot2 = None
def collision(x,y,x2,y2,w):
    if x + w > x2 > x and y+w > y2 > y:
        return True
    else:
        return False

drawGrid = False

def drawG():
    blockSize = 50  #Set the size of the grid block
    for x in range(0, 500, blockSize):
        for y in range(0, 300, blockSize):
            rect = p.Rect(x, y, blockSize, blockSize)
            p.draw.rect(s.ds, black, rect, 1)
ahhh = sta.mc.Hp
mx,my=p.mouse.get_pos()
def item(num,id,X,Y,width,height):
  global x,y
  global var
  picture = p.transform.scale(id,(width,height))
  if var[num][0]==0:
    name=s.ds.blit(picture, (x+X, y+Y))
    if In.colI(name):
      if In.additem(id):
        var[num][0]=1
enemy=None
def ENEMY(num,ammount,image1,image2,image3,X,Y,width,height):
  global S,hmmm,ahhhhhhhh,testdeath,enemy
  picture = p.transform.scale(image1,(width,height))
  if len(ahhhhhhhh)<=num:
    ahhhhhhhh.append(1)
  if ahhhhhhhh[num]==1:
    name=s.ds.blit(picture, (x+X, y+Y))
    if In.colI(name):
      sta.enemammount = ammount
      sta.hmmm = image1
      sta.hmmm2 = image2
      sta.hmmm3 = image3
      sta.S=21
      ahhhhhhhh[num]=0
#def ENEMYA(num,ammount,image1,image2,image3,X,Y,width,height):
def collide(obje):
  if (obje).collidepoint(sta.mc.rect.topleft) or (obje).collidepoint(sta.mc.rect.topright) or (obje).collidepoint(sta.mc.rect.midtop):
          return True
  if (obje).collidepoint(sta.mc.rect.midbottom) or (obje).collidepoint(sta.mc.rect.bottomleft) or (obje).collidepoint(sta.mc.rect.bottomright):
          return True
  if (obje).collidepoint(sta.mc.rect.midright) or (obje).collidepoint(sta.mc.rect.topright) or (obje).collidepoint(sta.mc.rect.bottomright):
          return True
  if (obje).collidepoint(sta.mc.rect.midleft) or (obje).collidepoint(sta.mc.rect.topleft) or (obje).collidepoint(sta.mc.rect.bottomleft):
          return True
#walls
def collidewall(walls):
  global collideU,collideD,collideL,collideR,wallist
  if (walls).collidepoint(sta.mc.rect.topleft) or (walls).collidepoint(sta.mc.rect.topright) or (walls).collidepoint(sta.mc.rect.midtop):
      collideU= True
  if (walls).collidepoint(sta.mc.rect.midbottom) or (walls).collidepoint(sta.mc.rect.bottomleft) or (walls).collidepoint(sta.mc.rect.bottomright):
      collideD = True
  if (walls).collidepoint(sta.mc.rect.midright) or (walls).collidepoint(sta.mc.rect.topright) or (walls).collidepoint(sta.mc.rect.bottomright):
      collideR = True
  if (walls).collidepoint(sta.mc.rect.midleft) or (walls).collidepoint(sta.mc.rect.topleft) or (walls).collidepoint(sta.mc.rect.bottomleft):
      collideL= True
def mouseover(rect):
  global my,mx
  mx,my=p.mouse.get_pos()
  test = p.mouse.get_pressed()[0]
  if rect.collidepoint(mx,my):
    if test:
      return True
os.system('clear')
en=sta.Enemy()
#DAMAGE
#CALCULATION
#AND
#GAME
def savegame():
  global savefile,savedata
  In.checkslot()
  savedata=[x,y,direction,sta.mc.level,Xp.gxp,Xp.xpn,sta.mcstats,In.slotItem,ahhhhhhhh,sta.mc.Hp,var,room,sta.pm1.level,Xp.pm1gxp,Xp.pm1xpn,sta.pm1stats,In.pm1slotitem,In.pm2slotitem,In.playerslotitem,sta.pm2.level,Xp.pm2gxp,Xp.pm2xpn,sta.pm2stats,sta.pm1.Hp,sta.pm2.Hp,sta.pm1.maxHp,sta.pm2.maxHp,sta.mc.clas]
  print(savedata[27])
  if savefile == 1:
    with open('SaveFiles/Savefile1.txt','w') as saved:
      json.dump(savedata,saved)
  if savefile == 2:
    with open('SaveFiles/Savefile2.txt','w') as saved:
      json.dump(savedata,saved)
  if savefile == 3:
    with open('SaveFiles/Savefile3.txt','w') as saved:
      json.dump(savedata,saved)
  if savefile == 4:
    with open('SaveFiles/Savefile4.txt','w') as saved:
      json.dump(savedata,saved)
  print('Game Saved')
once=0
r = False
begin=False
Startscreen=True
out = [0]
once2=0
playerminiy=20
pm1miniy=20
pm2miniy=20
def textboxcreate():
  global textbox,itemtext,texttracker,textamount,out,once2
  textamount = len(out)
  if textbox:
    p.draw.rect(s.ds,(93,93,93),p.Rect(0,200,500,100))
    p.draw.rect(s.ds,black,p.Rect(0,200,500,3))
    n = 30
    out = [(itemtext[i:i+n]) for i in range(0, len(itemtext), n)]
    Text = text.font.render(out[texttracker], True, black)
    TextR = p.Rect(0,200,500,100)
    TextR.topleft = (5,205)
    s.ds.blit(Text,TextR)
    if len(itemtext) > 30:
      Text2 = text.font.render(out[texttracker+1], True, black)
      TextR2 = p.Rect(0,250,500,50)
      TextR2.topleft = (5,255)
      s.ds.blit(Text2,TextR2)
    elif not len(itemtext) > 30:
      TextR2 = p.Rect(0,200,500,100)
    if (mouseover(TextR) or mouseover(TextR2)) and once2 ==0:
      texttracker +=1
      once2 = 1
      if texttracker+1 >= textamount:
        texttracker = 0
        out = [0]
        textbox = False
    elif not mouseover(TextR) and not mouseover(TextR2):
      once2 = 0
        
  elif not textbox:
    out = [0]
interactbo=p.draw.rect(s.ds,black,p.Rect(200,200,100,50))
interactest = False
itemtext = ''
def interitem(item,X,Y,width,height,wall,text):
  global x,y,interactbo,interactest,itemtext
  picture = p.transform.scale(item,(width,height))
  name=s.ds.blit(picture, (x+X, y+Y))
  if name.colliderect(interactbo) and not interactest:
    interactest = True
    itemtext = text
  elif not name.colliderect(interactbo):
    interactest = False
    itemtext = ''
  if wall:
    collidewall(name)
def interactbox():
  global direction,interactbo,interactest,textbox
  if direction == 1:
      interactbo=p.draw.rect(s.ds,black,p.Rect(200,200,100,50))
  elif direction == 2:
      interactbo=p.draw.rect(s.ds,black,p.Rect(290,100,50,100))
  elif direction == 3:
    interactbo=p.draw.rect(s.ds,black,p.Rect(200,50,100,50))
  elif direction == 4:
    interactbo=p.draw.rect(s.ds,black,p.Rect(170,100,50,100))
while Startscreen:
  s.ds.fill(white)
  s.ds.blit(text.textscreen,text.textRectscreen)
  s.ds.blit(text.textscreen1,text.textRectscreen1)
  s.ds.blit(text.textscreen2,text.textRectscreen2)
  s.ds.blit(text.textscreen3,text.textRectscreen3)
  for event in p.event.get():
    if mouseover(text.textRectscreen1):
      Startscreen = False
      begin = True
  s.screen.blit(s.ds,(0,0))
  p.display.flip()
ahhhahhh=0
yn=0
while begin:
  s.ds.fill(white)
  clock.tick(60)
  s.ds.blit(text.textsave1,text.textRectsave1)
  s.ds.blit(Trash, Trash_rect1)
  s.ds.blit(text.textsave2,text.textRectsave2)
  s.ds.blit(Trash, Trash_rect2)
  s.ds.blit(text.textsave3,text.textRectsave3)
  s.ds.blit(Trash, Trash_rect3)
  s.ds.blit(text.textsave4,text.textRectsave4)
  s.ds.blit(Trash, Trash_rect4)
  if ahhhahhh==0:
    for event in p.event.get():
      if mouseover(text.textRectsave1):
        with open('SaveFiles/Savefile1.txt') as saved:
          savedata =json.load(saved)
        savefile=1
        checkpass = os.environ['password1']
        pass1= checkpass
        if pass1=='None':
          begin = False
          r = True
        else:
          ahhhahhh=1
      if mouseover(text.textRectsave2):
        with open('SaveFiles/Savefile2.txt') as saved:
          savedata =json.load(saved)
        savefile=2
        checkpass = os.environ['password2']
        pass1= checkpass
        if pass1=='None':
          begin = False
          r = True
        else:
          ahhhahhh=1
      if mouseover(text.textRectsave3):
        with open('SaveFiles/Savefile3.txt') as saved:
          savedata =json.load(saved)
        savefile=3
        checkpass = os.environ['password3']
        pass1= checkpass
        if pass1=='None':
          begin = False
          r = True
        else:
          ahhhahhh=1
      if mouseover(text.textRectsave4):
        with open('SaveFiles/Savefile1.txt') as saved:
          savedata =json.load(saved)
        savefile=4
        checkpass = os.environ['password4']
        pass1= checkpass
        if pass1=='None':
          begin = False
          r = True
        else:
          ahhhahhh=1
      if mouseover(Trash_rect1) and once == 0:
        savefile=1
        checkpass = os.environ['password1']
        if checkpass == 'None' or '':
          with open('SaveFiles/Start_save.txt') as saved:
            savedata =json.load(saved)
          with open('SaveFiles/Savefile1.txt','w') as saved:
            json.dump(savedata,saved)
          os.environ['password1'] = 'nothing'
          print('save1 Deleted')
          once = 1
        elif not checkpass== 'None' or 'nothing': 
            ahhhahhh=2
      elif mouseover(Trash_rect2) and once == 0:
        savefile=2
        checkpass = os.environ['password2']
        if checkpass == 'None' or '':
          with open('SaveFiles/Start_save.txt') as saved:
            savedata =json.load(saved)
          with open('SaveFiles/Savefile2.txt','w') as saved:
            json.dump(savedata,saved)
          os.environ['password2'] = 'nothing'
          print('save2 Deleted')
          once = 1
        elif not checkpass== 'None' or 'nothing': 
            ahhhahhh=2
      elif mouseover(Trash_rect3) and once == 0:
        savefile=3
        checkpass = os.environ['password3']
        if checkpass == 'None' or '':
          with open('SaveFiles/Start_save.txt') as saved:
            savedata =json.load(saved)
          with open('SaveFiles/Savefile3.txt','w') as saved:
            json.dump(savedata,saved)
          os.environ['password3'] = 'nothing'
          print('save3 Deleted')
          once = 1
        elif not checkpass== 'None' or 'nothing': 
            ahhhahhh=2
      elif mouseover(Trash_rect4) and once == 0:
        savefile=4
        checkpass = os.environ['password4']
        if checkpass == 'None' or '':
          with open('SaveFiles/Start_save.txt') as saved:
            savedata =json.load(saved)
          with open('SaveFiles/Savefile4.txt','w') as saved:
            json.dump(savedata,saved)
          os.environ['password4'] = 'nothing'
          print('save4 Deleted')
          once = 1
        elif not checkpass== 'None' or 'nothing': 
            ahhhahhh=2
      elif not mouseover(Trash_rect1 or Trash_rect2 or Trash_rect3 or Trash_rect4):
        once = 0
  if ahhhahhh==1:
    #150,50,200,150
    p.draw.rect(s.ds,(0,0,0),p.Rect(0,0,1000,1000))
    p.draw.rect(s.ds,white,p.Rect(150,50,200,200))
    s.ds.blit(text.texts,text.textsRect)
    if pass1 == 'nothing' and yn == 0:
      s.ds.blit(text.texts2,text.texts2Rect)
      s.ds.blit(text.texts3,text.texts3Rect)
      if mouseover(text.texts3Rect):
        os.environ[('password'+str(savefile))]= 'None'
      elif mouseover(text.texts2Rect):
        yn = 1
    if yn == 1:
      for event in p.event.get():
        if event.type == p.KEYDOWN:
          if event.key == p.K_BACKSPACE:
            text.Passwordtext = text.Passwordtext[:-1]
          elif event.key == p.K_ENTER:
            os.environ[('password'+str(savefile))]=text.Passwordtext
            text.Passwordtext = ''
            ahhhahhh=0
          else:
            text.Passwordtext += event.unicode
      Password = text.font.render(text.Passwordtext,True,black)
      s.ds.blit(Password,text.texts4Rect)
    elif not pass1 =='nothing':
      for event in p.event.get():
        if event.type == p.KEYDOWN:
          if event.key == p.K_BACKSPACE:
            text.Passwordtext = text.Passwordtext[:-1]
          else:
            text.Passwordtext += event.unicode
      Password = text.font.render(text.Passwordtext,True,black)
      s.ds.blit(Password,text.texts4Rect)
    if text.Passwordtext == pass1:
      begin = False
      r = True
  elif ahhhahhh == 2:
    p.draw.rect(s.ds,(0,0,0),p.Rect(0,0,1000,1000))
    p.draw.rect(s.ds,white,p.Rect(150,50,200,200))
    s.ds.blit(text.texts,text.textsRect)
    pass1 = os.environ[('password'+str(savefile))]
    for event in p.event.get():
        if event.type == p.KEYDOWN:
          if event.key == p.K_BACKSPACE:
            text.Passwordtext = text.Passwordtext[:-1]
          else:
            text.Passwordtext += event.unicode
    Password = text.font.render(text.Passwordtext,True,black)
    s.ds.blit(Password,text.texts4Rect)
    if text.Passwordtext == pass1:
      with open('SaveFiles/Start_save.txt') as saved:
            savedata =json.load(saved)
      with open('SaveFiles/Savefile'+str(savefile)+'.txt','w') as saved:
            json.dump(savedata,saved)
      print('save' + str(savefile)+ ' Deleted')
      ahhhahhh=0
  s.screen.blit(s.ds,(0,0))
  p.display.flip()

yesxy=0
#wall1 = p.draw.rect(ds, color, p.Rect(x, y-50, 500, 100))
rect1 = p.draw.rect(s.ds, color, p.Rect(x, y-50, 500, 100))
wall2 = p.draw.rect(s.ds, color, p.Rect(x-100, y,100, 1000))
wall3 = p.draw.rect(s.ds, color, p.Rect(x, y+500,1000, 100))
wall4 =p.draw.rect(s.ds, color, p.Rect(x+500, y,100, 1000))
de=1
onceinv=0
forscor = 0
wcw = 150
wcx = 10
rcw = 150
rcx = 175
rcy = 10
mcw = 150
mcx = 340
mcy = 10
numtes = 0
classonce = 0
yesno= 0
plen = 230
oncest = 0
oncest1 = 0
oncest2 = 0
spllist = False
minspell = 0
spellistmonce  = 0
testmouse = False
spellover = 0
while r:
  #[x,y,image,level,gxp,xpn,stats,inv,enemies]
    if once== 0:
      os.system('clear')
      x=savedata[0]
      y=savedata[1]
      if savedata[2]== 1:
        im.g5=im.Di
      elif savedata[2]== 2:
        im.g5=im.Ri
      elif savedata[2]== 3:
        im.g5=im.Ui
      elif savedata[2]== 4:
        im.g5=im.Li
      Xp.level=savedata[3]
      Xp.gxp=savedata[4]
      Xp.xpn=savedata[5]
      sta.mcstats=savedata[6]
      while yesxy<10:
        In.inv[yesxy]=In.itemid[savedata[7][yesxy]]
        yesxy+=1
      ahhhhhhhh= savedata[8]
      sta.mc.Hp=savedata[9]
      var=savedata[10]
      room = savedata[11]
      sta.pm1.level = savedata[12]
      Xp.pm1gxp = savedata[13]
      Xp.pm1xpn = savedata[14]
      sta.pm1stats =savedata[15]
      yesxy=0
      while yesxy<2:
        In.pm1inv[yesxy] = In.itemid[savedata[16][yesxy]]
        yesxy+=1
      yesxy=0
      while yesxy<2:
        In.pm2inv[yesxy] = In.itemid[savedata[17][yesxy]]
        yesxy+=1
      yesxy=0
      while yesxy<2:
        In.playerinv[yesxy] = In.itemid[savedata[18][yesxy]]
        yesxy+=1
      sta.pm2.level = savedata[19]
      Xp.pm2gxp = savedata[20]
      Xp.pm2xpn = savedata[21]
      sta.pm2stats = savedata[22]
      sta.pm1.Hp = savedata[23]
      sta.pm2.Hp = savedata[24]
      sta.pm1.maxHp = savedata[25]
      sta.pm2.maxHp = savedata[26]
      sta.mc.clas = savedata[27]
      sta.mc.defense = sta.mcstats[0]+sta.itemstats[In.slotitemid[In.playerinv[0]]][0] +sta.itemstats[In.slotitemid[In.playerinv[1]]][0]
      sta.mc.attack = sta.mcstats[1]+sta.itemstats[In.slotitemid[In.playerinv[0]]][1] +sta.itemstats[In.slotitemid[In.playerinv[1]]][1]
      sta.mc.maxHp = sta.mcstats[2]+sta.itemstats[In.slotitemid[In.playerinv[0]]][2] +sta.itemstats[In.slotitemid[In.playerinv[1]]][2]
      sta.mc.mana = sta.mcstats[3]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
      sta.mc.luck = sta.mcstats[4]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
      if not sta.mc.clas == None:
        classonce = 1
      once = 1
    mx,my = p.mouse.get_pos()
    clock.tick(60)
    while sta.mc.clas == None:
      for event in p.event.get():
        wclass = p.transform.scale(im.stawarrior,(wcw,wcw))
        rclass = p.transform.scale(im.staranger,(rcw,rcw))
        mclass = p.transform.scale(im.stamage,(mcw,mcw))
        mx,my = p.mouse.get_pos()
        clock.tick(60)
        s.ds.fill(white)
        wclasss = s.ds.blit(wclass,(wcx,wcx))
        if collision(10,10,mx,my,150) and yesno == 0:
          wcw = 170
          wcx = 0
          itemtext = ('A good attack and high health class that can not use magic')
          textbox = True
        elif not wclasss.collidepoint((mx,my)) and yesno == 0:
          wcw =150
          wcx = 10
        rclasss = s.ds.blit(rclass,(rcx,rcy))
        if collision(175,10,mx,my,150) and yesno == 0:
          rcw = 170
          rcx = 165
          rcy = 0
          itemtext = ('A well rounded class that can use magic and melee')
          textbox = True
        elif not rclasss.collidepoint((mx,my)) and yesno == 0:
          rcw =150
          rcx =175
          rcy = 10
        mclasss = s.ds.blit(mclass,(mcx,mcy))
        if collision(340,10,mx,my,150) and yesno == 0:
          mcw = 170
          mcx = 330
          mcy = 0
          itemtext = ('A very magic based class that can not use melee weapons')
          textbox = True
        elif not mclasss.collidepoint((mx,my)) and yesno == 0:
          mcw =150
          mcx =340
          mcy = 10
        if not wclasss.collidepoint((mx,my)) and not rclasss.collidepoint((mx,my)) and not mclasss.collidepoint((mx,my)) and yesno ==0:
          textbox = False
        textboxcreate()
        if mouseover(wclasss) or yesno == 1:
          p.draw.rect(s.ds, white, p.Rect(133, 130, 234, 90))
          s.ds.blit(text.textsh,text.textshRect)
          s.ds.blit(text.texts2,text.texts2Rect)
          s.ds.blit(text.texts3,text.texts3Rect)
          yesno = 1
        if mouseover(rclasss) or yesno == 2:
          p.draw.rect(s.ds, white, p.Rect(133, 130, 234, 90))
          s.ds.blit(text.textsh,text.textshRect)
          s.ds.blit(text.texts2,text.texts2Rect)
          s.ds.blit(text.texts3,text.texts3Rect)
          yesno = 2
        if mouseover(mclasss) or yesno == 3:
          p.draw.rect(s.ds, white, p.Rect(133, 130, 234, 90))
          s.ds.blit(text.textsh,text.textshRect)
          s.ds.blit(text.texts2,text.texts2Rect)
          s.ds.blit(text.texts3,text.texts3Rect)
          yesno = 3
        if mouseover(text.texts2Rect) and not yesno == 0:
          sta.mc.clas = yesno
          textbox = False
        elif mouseover(text.texts3Rect) and not yesno == 0:
          yesno = 0
            
        s.screen.blit(s.ds,(0,0))
        p.display.flip()
    if classonce == 0:
      if sta.mc.clas == 1:
        sta.mcstats[0] = 2
        sta.mcstats[1] = 5
        sta.mcstats[2] = 15
        sta.mcstats[3] = 10
        sta.mcstats[4] = (random.randrange(1,15))
        Xp.pam = 3
        Xp.pdm = 2
        Xp.phm = 5
        Xp.pmm = 5
        Xp.pStr = 10
        Xp.pDex = 10
        Xp.pCon = 9
        Xp.pInt = 7
        In.playerinv[0] = im.Stick
        In.playerinv[1] = im.Empty
        In.playerinv[2] = im.Empty
      if sta.mc.clas == 2:
        sta.mcstats[0] = 1
        sta.mcstats[1] = 3
        sta.mcstats[2] = 10
        sta.mcstats[3] = 10
        sta.mcstats[4] = (random.randrange(1,15))
        Xp.pam = 3
        Xp.pdm = 3
        Xp.phm = 4
        Xp.pmm = 5
        Xp.pStr = 9
        Xp.pDex = 10
        Xp.pCon = 10
        Xp.pInt = 7
        In.playerinv[0] = im.Stick
        In.playerinv[1] = im.Empty
        In.playerinv[2] = im.Empty
      if sta.mc.clas == 3:
        sta.mcstats[0] = 0
        sta.mcstats[1] = 0
        sta.mcstats[2] = 5
        sta.mcstats[3] = 20
        sta.mcstats[4] = (random.randrange(1,15))
        Xp.pam = 0
        Xp.pdm = 2
        Xp.phm = 3
        Xp.pmm = 10
        Xp.pStr = 7
        Xp.pDex = 9
        Xp.pCon = 10
        Xp.pInt = 10
        In.playerinv[0] = im.Stick
        In.playerinv[1] = im.Empty
        In.playerinv[2] = im.Empty
      sta.mc.defense = sta.mcstats[0]+sta.itemstats[In.slotitemid[In.playerinv[0]]][0] +sta.itemstats[In.slotitemid[In.playerinv[1]]][0]
      sta.mc.attack = sta.mcstats[1]+sta.itemstats[In.slotitemid[In.playerinv[0]]][1] +sta.itemstats[In.slotitemid[In.playerinv[1]]][1]
      sta.mc.maxHp = sta.mcstats[2]+sta.itemstats[In.slotitemid[In.playerinv[0]]][2] +sta.itemstats[In.slotitemid[In.playerinv[1]]][2]
      sta.mc.mana = sta.mcstats[3]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
      sta.mc.luck = sta.mcstats[4]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
      sta.mc.Hp = sta.mc.maxHp
      classonce=1
    for event in p.event.get():
        if event.type == p.KEYUP:
            if event.key == p.K_e:
                if sta.S == 0:
                    sta.S = 1
                    event.key = p.K_p
                elif event.key == p.K_e and sta.S==1:
                  if spllist:
                    spllist = False
                  else:
                    sta.S = 0
                    if In.currentinv == 1:
                      In.playerinv[0]=In.inv[8]
                      In.playerinv[1]=In.inv[9]
                      In.playerinv[2]=In.inv[10]
                    elif In.currentinv == 2:
                      In.pm1inv[0]=In.inv[8]
                      In.pm1inv[1]=In.inv[9]
                      In.pm1inv[2]=In.inv[10]
                    elif In.currentinv == 3:
                      In.pm2inv[0]=In.inv[8]
                      In.pm2inv[1]=In.inv[9]
                      In.pm2inv[2]=In.inv[10]
                  event.key = p.K_p
            elif event.key == p.K_ESCAPE:
                if sta.S == 0:
                    sta.S = 2
                    event.key = p.K_p
                    P = 1
                elif sta.S == 1:
                    sta.S = 2
                    event.key = p.K_p
                    P = 2
                elif sta.S == 2 and P == 1:
                    sta.S = 0
                    event.key = p.K_p
                elif sta.S == 2 and P == 2:
                    sta.S = 1
                    event.key = p.K_p
                elif sta.S == 5:
                    if forscor == 0:
                      sta.S = 2
                    else:
                      forscor = 0
                    event.key = p.K_p
                  
            if event.key == p.K_v:
                    savegame()
                    event.key = p.K_p
            if event.key == p.K_EQUALS:
                if drawGrid == False:
                    drawGrid = True
                    event.key = p.K_p
                else:
                    drawGrid = False
                    event.key = p.K_p
            if interactest and event.key == p.K_f:
              if not textbox:
                textbox = True
              else:
                texttracker +=1
                if texttracker+1 >= textamount:
                  texttracker = 0
                  textbox = False
                  out = [0] 
              event.key = p.K_p 
            if sta.S==1 and event.key ==p.K_RIGHT and not spllist:
              if In.currentinv == 1:
                In.playerinv[0]=In.inv[8]
                In.playerinv[1]=In.inv[9]
                In.playerinv[2]=In.inv[10]
              elif In.currentinv == 2:
                In.pm1inv[0]=In.inv[8]
                In.pm1inv[1]=In.inv[9]
                In.pm1inv[2]=In.inv[10]
              elif In.currentinv == 3:
                In.pm2inv[0]=In.inv[8]
                In.pm2inv[1]=In.inv[9]
                In.pm2inv[2]=In.inv[10]
              onceinv=0
              In.currentinv+=1
              de=1
              if In.currentinv >sta.partyamount:
                In.currentinv=1
            if sta.S==1 and event.key ==p.K_LEFT and not spllist:
              if In.currentinv == 1:
                In.playerinv[0]=In.inv[8]
                In.playerinv[1]=In.inv[9]
                In.playerinv[2]=In.inv[10]
              elif In.currentinv == 2:
                In.pm1inv[0]=In.inv[8]
                In.pm1inv[1]=In.inv[9]
                In.pm1inv[2]=In.inv[10]
              elif In.currentinv == 3:
                In.pm2inv[0]=In.inv[8]
                In.pm2inv[1]=In.inv[9]
                In.pm2inv[2]=In.inv[10]
              onceinv=0
              In.currentinv-=1
              de=1
              if In.currentinv <=0:
                In.currentinv=sta.partyamount
            if sta.S==21 and battle.battleselec==0 and event.key == p.K_RIGHT:
              battle.oncet1=0
              battle.oncet2=0
              battle.oncet3=0
              battle.onceanim=0
              battle.selectorover+=1
              if battle.selectorover>sta.partyamount:
                battle.selectorover=1
            if sta.S==21 and battle.battleselec==0 and event.key == p.K_LEFT:
              battle.oncet1=0
              battle.oncet2=0
              battle.oncet3=0
              battle.onceanim=0
              battle.selectorover-=1
              if battle.selectorover<=0:
                battle.selectorover=sta.partyamount
            if sta.S==21 and battle.battleselec==0 and event.key == p.K_RETURN:
              if battle.selectorover == 1 and not sta.mc.hasattacked:
                battle.battleselec=1
              elif battle.selectorover == 2 and not sta.pm1.hasattacked:
                battle.battleselec=1
              elif battle.selectorover == 3 and not sta.pm2.hasattacked:
                battle.battleselec=1
              event.key = p.K_p
            if sta.S==21 and not battle.battleselec ==0 and event.key == p.K_RIGHT:
              battle.battleselec +=1
              battle.battleonce=0
              if battle.battleselec>4:
                battle.battleselec = 1
            if sta.S==21 and not battle.battleselec ==0 and event.key == p.K_LEFT:
              battle.battleselec -=1
              battle.battleonce=0
              if battle.battleselec<=0:
                battle.battleselec = 4
            if sta.S==21 and not battle.battleselec ==0 and event.key == p.K_DOWN:
              battle.battleselec +=2
              battle.battleonce=0
              if battle.battleselec>4:
                if battle.battleselec == 6:
                  battle.battleselec = 2
                else:
                  battle.battleselec = 1
            if sta.S==21 and not battle.battleselec ==0 and event.key == p.K_UP:
              battle.battleselec -=2
              battle.battleonce=0
              if battle.battleselec<=0:
                if battle.battleselec == -1:
                  battle.battleselec = 3
                else:
                  battle.battleselec = 4
            if sta.S==21 and not battle.battleselec==0 and event.key == p.K_RETURN:
              if battle.battleselec==1:
                if battle.selectorover == 1 and not sta.mc.hasattacked:
                  battle.attacktest = True
                if battle.selectorover == 2 and not sta.pm1.hasattacked:
                  battle.attacktest = True
                if battle.selectorover == 3 and not sta.pm2.hasattacked:
                  battle.attacktest = True
                battle.battleselec=0
              elif battle.battleselec==2:
                if battle.selectorover == 1 and not sta.mc.hasattacked:
                  sta.mc.defend = True
                  sta.mc.hasattacked = True
                elif battle.selectorover == 2 and not sta.pm1.hasattacked:
                  sta.pm1.defend = True
                  sta.pm1.hasattacked = True
                elif battle.selectorover == 3 and not sta.pm2.hasattacked:
                  sta.pm2.defend = True
                  sta.pm2.hasattacked = True
                battle.currentturn+=1
                battle.battleselec = 0
              elif battle.battleselec ==3:
                if battle.selectorover == 1 and not sta.mc.hasattacked:
                  battle.magictest = True
                if battle.selectorover == 2 and not sta.pm1.hasattacked:
                  battle.magictest = True
                if battle.selectorover == 3 and not sta.pm2.hasattacked:
                  battle.magictest = True
                battle.battleselec=0
            if sta.S==21 and event.key == p.K_ESCAPE:
              if battle.attacktest:
                battle.attacktest = False
              elif battle.magictest:
                battle.magictest = False
            if sta.S==21 and battle.attacktest and battle.enemieshp[0] >0  and event.key == p.K_1:
              battle.attacktest = False
              battle.enemyattacking =1
              if battle.pmattacking==1:
                battle.playerattack()
              if battle.pmattacking==2:
                battle.p1attack()
              if battle.pmattacking==3:
                battle.p2attack()
            if sta.S==21 and battle.attacktest and battle.enemieshp[1] >0  and event.key == p.K_2:
              battle.attacktest = False
              battle.enemyattacking =2
              if battle.pmattacking==1:
                battle.playerattack()
              if battle.pmattacking==2:
                battle.p1attack()
              if battle.pmattacking==3:
                battle.p2attack()
            if sta.S==21 and battle.attacktest and battle.enemieshp[2] >0  and event.key == p.K_3:
              battle.attacktest = False
              battle.enemyattacking =3
              if battle.pmattacking==1:
                battle.playerattack()
              if battle.pmattacking==2:
                battle.p1attack()
              if battle.pmattacking==3:
                battle.p2attack()
          
    if mouseover(text.textRect3) and sta.S == 2:
      sta.S=3
      ahh = 1
    if mouseover(text.textRect2) and sta.S == 2:
      sta.S=5
      ahh = 2
    if trrr==0 and forscor ==0:
      if  mouseover(text.textRect4) and ahh==1:
        sta.S=2
        ahh = 0
        trrr=1
      elif mouseover(text.textRect4) and P==1 and not sta.S == 5:
        sta.S=0
        trrr=1
      elif mouseover(text.textRect4) and P==2:
        sta.S=1
        trrr=1
    if not mouseover(text.textRect4):
      trrr=0
    rect1 = p.draw.rect(s.ds, color, p.Rect(x, y-50, 500, 100))
    if drawGrid:
            drawG()
#overworld
    if sta.S == 0:
        interactbox()
        yes =0
        P=0
        array = [[0,0],[0,0]]
        im.P1 = p.transform.scale(im.g5, (im.wi, 100))
        if room == 0:
          s.ds.fill(white)
          rect1 = p.draw.rect(s.ds, color, p.Rect(x, y-50, 500, 100))
          item(1,In.itemid[2],-50,100,50,50)
          item(2,In.itemid[3],500,150,50,50)
          ENEMY(0,1,sta.enemy[0],None,None,100,200,50,50)
          ENEMY(1,1,sta.enemy[0],None,None,200,400,50,50)
          ENEMY(2,1,sta.enemy[0],None,None,250,490,50,50)
          ENEMY(3,1,sta.enemy[0],None,None,20,490,50,50)
          ENEMY(4,2,sta.enemy[0],sta.enemy[2],None,20,50,50,50)
          ENEMY(5,2,sta.enemy[0],sta.enemy[0],None,-290,120,50,50)
          ENEMY(6,3,sta.enemy[0],sta.enemy[1],sta.enemy[1],900,-200,50,50)
          interitem(im.Rei,900,150,100,120,True,'yo, how you doing?')
          door=s.ds.blit(p.transform.scale(im.door,(50,75)),(x+150,y-25))
          if collide(door):
            room = 1
            y-=350
            x-=100
        if room == 1:
          s.ds.fill(white)
          rect1 = p.draw.rect(s.ds, color, p.Rect(x, y-90, 500, 140))
          wall2 = p.draw.rect(s.ds, color, p.Rect(x-1000, y-100,1000, 1000))
          wall3 = p.draw.rect(s.ds, color, p.Rect(x, y+500,1000, 100))
          wall4 =p.draw.rect(s.ds, color, p.Rect(x+500, y-100,500, 1000))
          door=s.ds.blit(p.transform.scale(im.door,(50,75)),(x+230,y+490))
          interitem(im.sign,400,50,50,50,True,'this is a sign, how bout that, a sign here, who couldve      guessed, its almost like it  was put here as a way to test how the textbox in this game  was to work, nah who would     be dumb enough to do that?')
          item(1,In.itemid[2],50,100,50,50)
          item(2,In.itemid[3],50,150,50,50)
          ENEMY(7,3,sta.enemy[0],sta.enemy[0],sta.enemy[0],100,200,50,50)
          if collide(door):
            room = 0
            y+=350
            x+=100
        s.ds.blit(sta.mc.image, (sta.mc.x, sta.mc.y))
        im.P1 = p.transform.scale(im.g5, (im.wi, 100))
        sta.mc.image = im.P1
        textlv2 = text.font2.render('Lv:' + str(sta.mc.level),True,black,white)
        textRectlv2 = textlv2.get_rect()
        textRectlv2.topright = (500,0)
        s.ds.blit(textlv2, textRectlv2)
        if drawGrid:
            drawG()
        if value >= len(im.Ua):
            value = 0
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        testdeath=0
        textboxcreate()
#movement for the player
        if not textbox:
          if event.type == p.KEYDOWN:
              if event.key == p.K_LEFT:
                im.g5 = im.La[value]
                x += 5
                wi = 77
                direction = 4
              if event.key ==p.K_RIGHT:
                im.g5 = im.Ra[value]
                x -= 5
                wi = 77
                direction = 2
              if event.key == p.K_UP:
                im.g5 = im.Ua[value]
                y += 5
                wi = 77
                direction = 3
              if event.key ==  p.K_DOWN:
                im.g5 = im.Da[value]
                y -= 5
                wi = 87
                direction = 1
          if event.type == p.KEYUP:
              if event.key == p.K_LEFT:
                im.g5 = im.Li
                direction = 4
              if event.key == p.K_RIGHT:
                im.g5 = im.Ri
                direction = 2
              if event.key == p.K_UP:
                im.g5 = im.Ui
                direction = 3
              if event.key == p.K_DOWN:
                im.g5 = im.Di
                direction = 1
#inventory screen
    elif sta.S == 1:
      if not spllist:
        Slot1 = p.transform.scale(In.inv[0], (50, 50))
        Slot2 = p.transform.scale(In.inv[1], (50, 50))
        Slot3 = p.transform.scale(In.inv[2], (50, 50))
        Slot4 = p.transform.scale(In.inv[3], (50, 50))
        Slot5 = p.transform.scale(In.inv[4], (50, 50))
        Slot6 = p.transform.scale(In.inv[5], (50, 50))
        Slot7 = p.transform.scale(In.inv[6], (50, 50))
        Slot8 = p.transform.scale(In.inv[7], (50, 50))
        ESlotA = p.transform.scale(In.inv[8], (50,50))
        ESlotW = p.transform.scale(In.inv[9], (50,50))
        ESlotP = p.transform.scale(In.inv[10], (50,50))
        if not drawGrid:
          s.ds.fill(color)
          color2 = (255,255,255)
        else:
          s.ds.fill(white)
          color2 = (0,0,0)
        for i in In.slotArray:
          i.draw(s.ds)
        for i in In.slotArray2:
          i.draw2(s.ds)
        if drawGrid:
            drawG()
        EquipArm=p.draw.rect(s.ds,color2,p.Rect(50,0,50,50))
        EquipWeap=p.draw.rect(s.ds,color2,p.Rect(150,0,50,50))
        EquipPot=p.draw.rect(s.ds,color2,p.Rect(250,0,50,50))
        S1=s.ds.blit(Slot1,(50,100))
        s.ds.blit(Slot2,(150,100))
        s.ds.blit(Slot3,(250,100))
        s.ds.blit(Slot4,(350,100))
        s.ds.blit(Slot5,(50,200))
        s.ds.blit(Slot6,(150,200))
        s.ds.blit(Slot7,(250,200))
        s.ds.blit(Slot8,(350,200))
        s.ds.blit(ESlotA,(50,0))
        s.ds.blit(ESlotW,(150,0))
        s.ds.blit(ESlotP,(250,0))
        playermini =  p.transform.scale(sta.mc.mini,(75,80))
        pm1mini = p.transform.scale(sta.pm1.mini,(75,80))
        pm2mini = p.transform.scale(sta.pm2.mini,(75,80))
        if In.currentinv ==1:
          if de <=20:
            if de<10:
              playerminiy-=1
            elif de<20:
              playerminiy+=1
            de+=1
          if not sta.mc.clas == 1:
            if collision(420,50,mx,my,40):
              s.ds.blit(im.magop,im.magopR)
            else:
              s.ds.blit(im.magcl,im.magclR)
            if mouseover(im.magopR):
              spllist = True
          s.ds.blit(playermini,(340,playerminiy))
          if onceinv==0:
            In.inv[8]=In.playerinv[0]
            In.inv[9]=In.playerinv[1]
            In.inv[10]=In.playerinv[2]
            onceinv=1
        elif In.currentinv ==2:
          if de <=20:
            if de<10:
              pm1miniy-=1
            elif de<20:
              pm1miniy+=1
            de+=1
          s.ds.blit(pm1mini,(340,pm1miniy))
          if onceinv==0:
            In.inv[8]=In.pm1inv[0]
            In.inv[9]=In.pm1inv[1]
            In.inv[10]=In.pm1inv[2]
            onceinv=1
        elif In.currentinv ==3:
          if de <=20:
            if de<10:
              pm2miniy-=1
            elif de<20:
              pm2miniy+=1
            de+=1
          s.ds.blit(pm2mini,(340,pm2miniy))
          if onceinv==0:
            In.inv[8]=In.pm2inv[0]
            In.inv[9]=In.pm2inv[1]
            In.inv[10]=In.pm2inv[2]
            onceinv=1
            In.slotselect()
      elif spllist:
        equipsl = text.font.render('Equiped Spells:',True,black)
        equipslR = equipsl.get_rect()
        equipslR.topleft = (250,50)
        slo1 = text.font2.render('Slot1:'+str(sta.spell[In.eqspells[0]]),True,black)
        slo1R = slo1.get_rect()
        slo1R.topleft = (250,100)
        slo2 = text.font2.render('Slot2:'+str(sta.spell[In.eqspells[1]]),True,black)
        slo2R = slo2.get_rect()
        slo2R.topleft = (250,125)
        slo3 = text.font2.render('Slot3:'+str(sta.spell[In.eqspells[2]]),True,black)
        slo3R = slo3.get_rect()
        slo3R.topleft = (250,150)
        slo4 = text.font2.render('Slot4:'+str(sta.spell[In.eqspells[3]]),True,black)
        slo4R = slo4.get_rect()
        slo4R.topleft = (250,175)
        s.ds.fill(white)
        if len(In.learnedspells) >=minspell+1:
          one = text.font2.render(str(minspell+1)+':'+str(sta.spell[In.learnedspells[minspell]]),True,black)
          oneR = one.get_rect()
          oneR.topleft = (5,40)
          s.ds.blit(one,oneR)
          if mouseover(oneR) and not testmouse:
            testmouse = True
            spellover = minspell
        if len(In.learnedspells) >=minspell+2:
          two = text.font2.render(str(minspell+2)+':'+str(sta.spell[In.learnedspells[minspell+1]]),True,black)
          twoR = two.get_rect()
          twoR.topleft = (5,65)
          s.ds.blit(two,twoR)
          if mouseover(twoR) and not testmouse:
            testmouse = True
            spellover = minspell+1
        if len(In.learnedspells) >=minspell+3:
          three = text.font2.render(str(minspell+3)+':'+str(sta.spell[In.learnedspells[minspell+2]]),True,black)
          threeR = three.get_rect()
          threeR.topleft = (5,90)
          s.ds.blit(three,threeR)
          if mouseover(threeR) and not testmouse:
            testmouse = True
            spellover = minspell+2
        if len(In.learnedspells) >=minspell+4:
          four = text.font2.render(str(minspell+4)+':'+str(sta.spell[In.learnedspells[minspell+3]]),True,black)
          fourR = four.get_rect()
          fourR.topleft = (5,115)
          s.ds.blit(four,fourR)
          if mouseover(fourR) and not testmouse:
            testmouse = True
            spellover = minspell+3
        if len(In.learnedspells) >=minspell+5:
          five = text.font2.render(str(minspell+5)+':'+str(sta.spell[In.learnedspells[minspell+4]]),True,black)
          fiveR = five.get_rect()
          fiveR.topleft = (5,140)
          s.ds.blit(five,fiveR)
          if mouseover(fiveR) and not testmouse:
            testmouse = True
            spellover = minspell+4
        if len(In.learnedspells) >=minspell+6:
          s.ds.blit(im.downs,im.upsR)
          if mouseover(im.upsR) and spellistmonce == 0:
            minspell +=5
            spellistmonce = 1
        if not minspell == 0:
          s.ds.blit(im.ups,im.downsR)
          if mouseover(im.downsR) and spellistmonce == 0:
            minspell -=5
            spellistmonce = 1
        s.ds.blit(text.spells,text.spellsR)
        s.ds.blit(equipsl,equipslR)
        s.ds.blit(slo1,slo1R)
        s.ds.blit(slo2,slo2R)
        s.ds.blit(slo3,slo3R)
        s.ds.blit(slo4,slo4R)
        if not mouseover(im.downsR) and not mouseover(im.upsR):
            spellistmonce = 0
        if testmouse:
          mousetext = text.font2.render(str(spellover+1)+':'+str(sta.spell[In.learnedspells[spellover]]),True,black_faded)
          testingtesting = p.mouse.get_pressed()[0]
          s.ds.blit(mousetext,(mx-50,my-10))
          if not testingtesting:
            testmouse = False
            if slo1R.collidepoint((mx,my)):
              if not In.eqspells[1] == In.learnedspells[spellover]:
                if not In.eqspells[2] == In.learnedspells[spellover]:
                  if not In.eqspells[3] == In.learnedspells[spellover]:
                    In.eqspells[0] = In.learnedspells[spellover]
            if slo2R.collidepoint((mx,my)):
              if not In.eqspells[0] == In.learnedspells[spellover]:
                if not In.eqspells[2] == In.learnedspells[spellover]:
                  if not In.eqspells[3] == In.learnedspells[spellover]:
                    In.eqspells[1] = In.learnedspells[spellover]
            if slo3R.collidepoint((mx,my)):
              if not In.eqspells[1] == In.learnedspells[spellover]:
                if not In.eqspells[0] == In.learnedspells[spellover]:
                  if not In.eqspells[3] == In.learnedspells[spellover]:
                    In.eqspells[2] = In.learnedspells[spellover]
            if slo4R.collidepoint((mx,my)):
              if not In.eqspells[1] == In.learnedspells[spellover]:
                if not In.eqspells[0] == In.learnedspells[spellover]:
                  if not In.eqspells[2] == In.learnedspells[spellover]:
                    In.eqspells[3] = In.learnedspells[spellover]
              
          
      
#menu screen
    elif sta.S == 2:
        s.ds.fill(white)
        s.ds.blit(text.text, text.textRect)
        s.ds.blit(text.text2, text.textRect2)
        s.ds.blit(text.text3, text.textRect3)
        s.ds.blit(text.text4, text.textRect4)
    elif sta.S == 3:
        s.ds.fill(white)
        s.ds.blit(text.text5, text.textRect5)
        s.ds.blit(text.text4, text.textRect4)
    elif sta.S == 5:
        s.ds.fill(white)
        if forscor == 0:
          plen = ((sta.partyamount*70) + 20)
          text.stat1 = text.font2.render('Atk:'+str(sta.mc.attack),True,black)
          text.stat2 = text.font2.render('Def:'+str(sta.mc.defense),True,black)
          text.stat3 = text.font2.render('Mana:'+str(sta.mc.mana),True,black)
          text.stat4 = text.font2.render('MaxHp:'+str(sta.mc.maxHp),True,black)
          text.stat5 = text.font2.render('CurrentHp:'+str(sta.mc.Hp),True,black)
          s.ds.blit(text.stat1,text.stat1R)
          s.ds.blit(text.stat2,text.stat2R)
          s.ds.blit(text.stat3,text.stat3R)
          s.ds.blit(text.stat4,text.stat4R)
          s.ds.blit(text.stat5,text.stat5R)
          p.draw.rect(s.ds,black,p.Rect(100,70,plen,5))
          p.draw.rect(s.ds,black,p.Rect(100,100,plen,5))
          p.draw.rect(s.ds,black,p.Rect(100,130,plen,5))
          p.draw.rect(s.ds,black,p.Rect(100,160,plen,5))
          p.draw.rect(s.ds,black,p.Rect(100,190,plen,5))
          p.draw.rect(s.ds,black,p.Rect(185,0,5,195))
          player = s.ds.blit(sta.mcmini,(130,0))
          if mouseover(player):
            forscor = 1
          if sta.partyamount >=2:
            p.draw.rect(s.ds,black,p.Rect(255,0,5,195))
            s.ds.blit(text.p1st1,text.p1st1R)
            s.ds.blit(text.p1st2,text.p1st2R)
            s.ds.blit(text.p1st3,text.p1st3R)
            s.ds.blit(text.p1st4,text.p1st4R)
            s.ds.blit(text.p1st5,text.p1st5R)
            pm1 = s.ds.blit(sta.pm1mini,(200,0))
            if mouseover(pm1):
              forscor = 2
          if sta.partyamount == 3:
            p.draw.rect(s.ds,black,p.Rect(325,0,5,195))
            s.ds.blit(text.p2st1,text.p2st1R)
            s.ds.blit(text.p2st2,text.p2st2R)
            s.ds.blit(text.p2st3,text.p2st3R)
            s.ds.blit(text.p2st4,text.p2st4R)
            s.ds.blit(text.p2st5,text.p2st5R)
            pm2 = s.ds.blit(sta.pm2mini,(270,0))
            if mouseover(pm2):
              forscor = 3
        elif forscor == 1:
          
          text.spsta = text.font2.render('Strength:'+str(Xp.pStr),True,black)
          text.spsta1 = text.font2.render('Dexterity:'+str(Xp.pDex),True,black)
          text.spsta2 = text.font2.render('Constitution:'+str(Xp.pCon),True,black)
          text.spsta3 = text.font2.render('Intelligence:'+str(Xp.pInt),True,black)
          text.spstasta = text.font.render('Current stat points:'+str(Xp.pstatpoints),True,black)
          s.ds.blit(text.spstasta,text.staR)
          s.ds.blit(text.spsta,text.strR)
          s.ds.blit(text.spsta1,text.dexR)
          s.ds.blit(text.spsta2,text.conR)
          s.ds.blit(text.spsta3,text.intR)
          s.ds.blit(im.add1,im.add1R)
          s.ds.blit(im.add2,im.add2R)
          s.ds.blit(im.add3,im.add3R)
          s.ds.blit(im.add4,im.add4R)
          if mouseover(im.add1R) and oncest == 0:
            Xp.pStr +=1
            Xp.pstatpoints -=1
            oncest = 1
          elif mouseover(im.add2R) and oncest == 0:
            Xp.pDex +=1
            Xp.pstatpoints -=1
            oncest = 1
          elif mouseover(im.add3R) and oncest == 0:
            Xp.pCon +=1
            Xp.pstatpoints -=1
            oncest = 1
          elif mouseover(im.add4R) and oncest == 0:
            Xp.pInt +=1
            Xp.pstatpoints -=1
            oncest = 1
          elif not mouseover(im.add1R) and not mouseover(im.add2R) and not mouseover(im.add3R) and not mouseover(im.add4R):
            if not Xp.pstatpoints <= 0:
              oncest = 0
          
        elif forscor == 2:
          text.sp1sta = text.font2.render('Strength:'+str(Xp.p1Str),True,black)
          text.sp1sta1 = text.font2.render('Dexterity:'+str(Xp.p1Dex),True,black)
          text.sp1sta2 = text.font2.render('Constitution:'+str(Xp.p1Con),True,black)
          text.sp1sta3 = text.font2.render('Intelligence:'+str(Xp.p1Int),True,black)
          text.sp1stasta = text.font.render('Current stat points:'+str(Xp.p1statpoints),True,black)
          s.ds.blit(text.sp1stasta,text.sta1R)
          s.ds.blit(text.sp1sta,text.str1R)
          s.ds.blit(text.sp1sta1,text.dex1R)
          s.ds.blit(text.sp1sta2,text.con1R)
          s.ds.blit(text.sp1sta3,text.int1R)
          s.ds.blit(im.add1,im.add1R)
          s.ds.blit(im.add2,im.add2R)
          s.ds.blit(im.add3,im.add3R)
          s.ds.blit(im.add4,im.add4R)
          if mouseover(im.add1R) and oncest1 == 0:
            Xp.p1Str +=1
            Xp.p1statpoints -=1
            oncest1 = 1
          elif mouseover(im.add2R) and oncest1 == 0:
            Xp.p1Dex +=1
            Xp.p1statpoints -=1
            oncest1 = 1
          elif mouseover(im.add3R) and oncest1 == 0:
            Xp.p1Con +=1
            Xp.p1statpoints -=1
            oncest1 = 1
          elif mouseover(im.add4R) and oncest1 == 0:
            Xp.p1Int +=1
            Xp.p1statpoints -=1
            oncest1 = 1
          elif not mouseover(im.add1R) and not mouseover(im.add2R) and not mouseover(im.add3R) and not mouseover(im.add4R):
            if not Xp.p1statpoints <= 0:
              oncest1 = 0
        elif forscor == 3:
          text.sp2sta = text.font2.render('Strength:'+str(Xp.p2Str),True,black)
          text.sp2sta1 = text.font2.render('Dexterity:'+str(Xp.p2Dex),True,black)
          text.sp2sta2 = text.font2.render('Constitution:'+str(Xp.p2Con),True,black)
          text.sp2sta3 = text.font2.render('Intelligence:'+str(Xp.p2Int),True,black)
          text.sp2stasta = text.font.render('Current stat points:'+str(Xp.p2statpoints),True,black)
          s.ds.blit(text.sp2stasta,text.sta2R)
          s.ds.blit(text.sp2sta,text.str2R)
          s.ds.blit(text.sp2sta1,text.dex2R)
          s.ds.blit(text.sp2sta2,text.con2R)
          s.ds.blit(text.sp2sta3,text.int2R)
          s.ds.blit(im.add1,im.add1R)
          s.ds.blit(im.add2,im.add2R)
          s.ds.blit(im.add3,im.add3R)
          s.ds.blit(im.add4,im.add4R)
          if mouseover(im.add1R) and oncest2 == 0:
            Xp.p2Str +=1
            Xp.p2statpoints -=1
            oncest2 = 1
          elif mouseover(im.add2R) and oncest2 == 0:
            Xp.p2Dex +=1
            Xp.p2statpoints -=1
            oncest2 = 1
          elif mouseover(im.add3R) and oncest2 == 0:
            Xp.p2Con +=1
            Xp.p2statpoints -=1
            oncest2 = 1
          elif mouseover(im.add4R) and oncest2 == 0:
            Xp.p2Int +=1
            Xp.p2statpoints -=1
            oncest2 = 1
          elif not mouseover(im.add1R) and not mouseover(im.add2R) and not mouseover(im.add3R) and not mouseover(im.add4R):
            if not Xp.p2statpoints <= 0:
              oncest2 = 0

      
    elif sta.S == 21:
      battle.battlesequence()
    elif sta.S == None:
      s.ds.fill(black)
      s.ds.blit(text.text999,text.textRect999)
    collidewall(rect1)
    collidewall(wall2)
    collidewall(wall3)
    collidewall(wall4)
    if collideL:
        x -= 10
        collideL = False
    if collideR:
        x += 10
        collideR = False
    if collideU:
        y -= 10
        collideU = False
    if collideD:
        y += 10
        collideD = False
    s.screen.blit(s.ds,(0,0))
    p.display.flip()  # update display
    tryhard += 1
    if drawGrid:
            drawG()
    if tryhard == 10:
        value += 1
        tryhard = 0

    if sta.mc.Hp<= 0:
        S=None
