    #net dmg = attack dmg - def × 0.5
#a,b = b,a
#array[0][1],array[1][1] = arrray[1][1],array[0][1]
import pygame as p
import os, random, json, sta, im, In, Xp, battle, text, s
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
Trash = p.image.load('trash-2.svg')
Trash_rect1= Trash.get_rect()
Trash_rect1.center = (400,50)
Trash_rect2= Trash.get_rect()
Trash_rect2.center = (400,120)
Trash_rect3= Trash.get_rect()
Trash_rect3.center = (400,190)
Trash_rect4= Trash.get_rect()
Trash_rect4.center = (400,260)
white = (255, 255, 255,255)
green = (0,255,0,255)
red = (255,0,0,255)
grey = (10,10,10,255)
black = (0,0,0,255)
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
  savedata=[x,y,direction,Xp.level,Xp.gxp,Xp.xpn,sta.mcstats,In.slotItem,ahhhhhhhh,sta.mc.Hp,var,room]
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
      sta.mc.defense = sta.mcstats[0]+sta.itemstats[In.slotitemid[In.inv[8]]][0] +sta.itemstats[In.slotitemid[In.inv[9]]][0]
      sta.mc.attack = sta.mcstats[1]+sta.itemstats[In.slotitemid[In.inv[8]]][1] +sta.itemstats[In.slotitemid[In.inv[9]]][1]
      sta.mc.maxHp = sta.mcstats[2]+sta.itemstats[In.slotitemid[In.inv[8]]][2] +sta.itemstats[In.slotitemid[In.inv[9]]][2]
      sta.mc.mana = sta.mcstats[3]+sta.itemstats[In.slotitemid[In.inv[8]]][3] +sta.itemstats[In.slotitemid[In.inv[9]]][3]
      sta.mc.luck = sta.mcstats[4]+sta.itemstats[In.slotitemid[In.inv[8]]][3] +sta.itemstats[In.slotitemid[In.inv[9]]][3]
      room = savedata[11]
      once = 1
    mx,my = p.mouse.get_pos()
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.KEYUP:
            if event.key == p.K_e:
                if sta.S == 0:
                    sta.S = 1
                    event.key = p.K_p
                elif event.key == p.K_e and sta.S==1:
                    sta.S = 0
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
    if mouseover(text.textRect3) and sta.S == 2:
      sta.S=3
      ahh = 1
    if trrr==0:
      if  mouseover(text.textRect4) and ahh==1:
        sta.S=2
        ahh = 0
        trrr=1
      elif mouseover(text.textRect4) and P==1:
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
          ENEMY(4,1,sta.enemy[0],None,None,20,50,50,50)
          ENEMY(5,2,sta.enemy[0],sta.enemy[0],None,-290,120,50,50)
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
          ENEMY(6,3,sta.enemy[0],sta.enemy[0],sta.enemy[0],100,200,50,50)
          if collide(door):
            room = 0
            y+=350
            x+=100
        s.ds.blit(sta.mc.image, (sta.mc.x, sta.mc.y))
        im.P1 = p.transform.scale(im.g5, (im.wi, 100))
        sta.mc.image = im.P1
        textlv2 = text.font2.render('Lv:' + str(Xp.level),True,black,white)
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
        s.ds.blit(textlv2, textRectlv2)
      
        In.slotselect()
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
