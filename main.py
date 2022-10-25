#net dmg = attack dmg - def × factor , where factor is 0.5 in Classic Mode, 0.75 in Expert Mode, and 1 in Master Mode.
#a,b = b,a
#array[0][1],array[1][1] = arrray[1][1],array[0][1]
import pygame as p
import os 
import random
import json
import sta
import im
import In
import Xp
clock = p. time. Clock()
Trash = p.image.load('trash-2.svg')
Trash_rect1= Trash.get_rect()
Trash_rect1.center = (400,50)
Trash_rect2= Trash.get_rect()
Trash_rect2.center = (400,120)
Trash_rect3= Trash.get_rect()
Trash_rect3.center = (400,190)
Trash_rect4= Trash.get_rect()
Trash_rect4.center = (400,260)
white = (255, 255, 255)
green = (0,255,0)
red = (255,0,0)
grey = (10,10,10)
black = (0,0,0)
color2 = (255,255.255)
color = black
savefile=0
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
S = 0
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
            p.draw.rect(ds, black, rect, 1)
ahhh = sta.mc.Hp
font999 = p.font.Font('freesansbold.ttf', 50)
text999 = font999.render('YOU DIED', True, red, black)
textRect999 = text999.get_rect()
textRect999.center = (250,150)
fonthp = p.font.Font('freesansbold.ttf', 10)
textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
textRectHp = textHp.get_rect()
textRectHp.center = (50,220)

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
mx,my=p.mouse.get_pos()
def item(num,id,X,Y,width,height):
  global x,y
  global var
  picture = p.transform.scale(id,(width,height))
  if var[num][0]==0:
    name=ds.blit(picture, (x+X, y+Y))
    if In.colI(name):
      if In.additem(id):
        var[num][0]=1
def ENEMY(num,image,X,Y,width,height):
  global S,hmmm,ahhhhhhhh,testdeath
  picture = p.transform.scale(image,(width,height))
  if len(ahhhhhhhh)<=num:
    ahhhhhhhh.append(1)
  if ahhhhhhhh[num]==1:
    name=ds.blit(picture, (x+X, y+Y))
    if In.colI(name):
      hmmm = image
      S=21
      ahhhhhhhh[num]=0
def collide(obje):
  if (obje).collidepoint(sta.mc.rect.topleft) or (obje).collidepoint(sta.mc.rect.topright) or (obje).collidepoint(sta.mc.rect.midtop):
          return True
  if (obje).collidepoint(sta.mc.rect.midbottom) or (obje).collidepoint(sta.mc.rect.bottomleft) or rect1.collidepoint(sta.mc.rect.bottomright):
          return True
  if (obje).collidepoint(sta.mc.rect.midright) or (obje).collidepoint(sta.mc.rect.topright) or (obje).collidepoint(sta.mc.rect.bottomright):
          return True
  if (obje).collidepoint(sta.mc.rect.midleft) or (obje).collidepoint(sta.mc.rect.topleft) or (obje).collidepoint(sta.mc.rect.bottomleft):
          return True
def mouseover(rect):
  global my,mx
  mx,my=p.mouse.get_pos()
  test = p.mouse.get_pressed()[0]
  if rect.collidepoint(mx,my):
    if test:
      return True
      print('rect')

os.system('clear')
s=sta.Enemy()
at=0
de=0
#DAMAGE
#CALCULATION
#AND
#GAME
def damage(wih,wht):
  dam = wht.attack+(random.randrange(1,3))-wih.defense
  if dam<=0:
    pass
  if dam>0:
    wih.Hp -= dam
savefont= p.font.Font('freesansbold.ttf', 40)
textsave1 = savefont.render('Save file 1', True, black,white)
textRectsave1 = textsave1.get_rect()
textRectsave1.center = (250,50)
textsave2 = savefont.render('Save file 2', True, black,white)
textRectsave2 = textsave2.get_rect()
textRectsave2.center = (250,120)
textsave3 = savefont.render('Save file 3', True, black,white)
textRectsave3 = textsave3.get_rect()
textRectsave3.center = (250,190)
textsave4 = savefont.render('Save file 4', True, black,white)
textRectsave4 = textsave4.get_rect()
textRectsave4.center = (250,260)
#[x,y,image,level,gxp,xpn,stats,inv,enemies]
def savegame():
  global savefile,savedata
  In.checkslot()
  savedata=[x,y,direction,Xp.level,Xp.gxp,Xp.xpn,sta.mcstats,In.slotItem,ahhhhhhhh,sta.mc.Hp,var]
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
textscreen = font999.render('Dynasty', True, black,white)
textRectscreen = textscreen.get_rect()
textRectscreen.center = (250,50)
textscreen1 = font.render('Start', True, black,white)
textRectscreen1 = textscreen1.get_rect()
textRectscreen1.center = (250,100)
textscreen2 = font.render('Settings', True, black,white)
textRectscreen2 = textscreen2.get_rect()
textRectscreen2.center = (250,150)
textscreen3 = font.render('Quit', True, black,white)
textRectscreen3 = textscreen3.get_rect()
textRectscreen3.center = (250,200)
user_text = ''
while Startscreen:
  ds.fill(white)
  ds.blit(textscreen,textRectscreen)
  ds.blit(textscreen1,textRectscreen1)
  ds.blit(textscreen2,textRectscreen2)
  ds.blit(textscreen3,textRectscreen3)
  for event in p.event.get():
    if mouseover(textRectscreen1):
      Startscreen = False
      begin = True
    if event.type == p.KEYDOWN:
      if event.key == p.K_BACKSPACE:
        user_text = user_text[:-1]
      else:
        user_text += event.unicode
  testext= font.render(user_text, True, black)
  testRect = testext.get_rect()
  testRect.center = (250,250)
  ds.blit(testext,testRect)
  p.display.flip()
while begin:
  ds.fill(white)
  clock.tick(60)
  ds.blit(textsave1,textRectsave1)
  ds.blit(Trash, Trash_rect1)
  ds.blit(textsave2,textRectsave2)
  ds.blit(Trash, Trash_rect2)
  ds.blit(textsave3,textRectsave3)
  ds.blit(Trash, Trash_rect3)
  ds.blit(textsave4,textRectsave4)
  ds.blit(Trash, Trash_rect4)
  for event in p.event.get():
    if mouseover(textRectsave1):
      savefile=1
      begin = False
      r = True
      with open('SaveFiles/Savefile1.txt') as saved:
        savedata =json.load(saved)
    if mouseover(textRectsave2):
      savefile=2
      begin = False
      r = True
      with open('SaveFiles/Savefile2.txt') as saved:
        savedata =json.load(saved)
    if mouseover(textRectsave3):
      savefile=3
      begin = False
      r = True
      with open('SaveFiles/Savefile3.txt') as saved:
        savedata =json.load(saved)
    if mouseover(textRectsave4):
      savefile=4
      begin = False
      r = True
      with open('SaveFiles/Savefile4.txt') as saved:
        savedata =json.load(saved)
    if mouseover(Trash_rect1) and once == 0:
        with open('SaveFiles/Start_save.txt') as saved:
          savedata =json.load(saved)
        with open('SaveFiles/Savefile1.txt','w') as saved:
          json.dump(savedata,saved)
        print('save1 Deleted')
        once = 1
          
    elif mouseover(Trash_rect2) and once == 0:
        with open('SaveFiles/Start_save.txt') as saved:
          savedata =json.load(saved)
        with open('SaveFiles/Savefile2.txt','w') as saved:
          json.dump(savedata,saved)
        print('save2 Deleted')
        once = 1
    elif mouseover(Trash_rect3) and once == 0:
        with open('SaveFiles/Start_save.txt') as saved:
          savedata =json.load(saved)
        with open('SaveFiles/Savefile3.txt','w') as saved:
          json.dump(savedata,saved)
        print('save3 Deleted')
        once = 1
    elif mouseover(Trash_rect4) and once == 0:
        with open('SaveFiles/Start_save.txt') as saved:
          savedata =json.load(saved)
        with open('SaveFiles/Savefile4.txt','w') as saved:
          json.dump(savedata,saved)
        print('save4 Deleted')
        once = 1
    elif not mouseover(Trash_rect1 or Trash_rect2 or Trash_rect3 or Trash_rect4):
      once = 0
  p.display.flip()
  
yesxy=0
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
      once = 1
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
        textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
        textlv2 = font2.render('Lv:' + str(Xp.level),True,black,white)
        textRectlv2 = textlv2.get_rect()
        textRectlv2.topright = (500,0)
        yes =0
        P=0
        array = [[0,0],[0,0]]
        ds.fill(white)
        ds.blit(sta.mc.image, (sta.mc.x, sta.mc.y))
        rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
        im.P1 = p.transform.scale(im.g5, (im.wi, 100))
        sta.mc.image = im.P1
        item(1,In.itemid[2],-50,100,50,50)
        item(2,In.itemid[3],500,150,50,50)
        ENEMY(0,sta.enemy[0],100,200,50,50)
        ENEMY(1,sta.enemy[0],200,400,50,50)
        ENEMY(2,sta.enemy[0],250,490,50,50)
        ENEMY(3,sta.enemy[0],20,490,50,50)
        ENEMY(4,sta.enemy[0],20,50,50,50)
        ds.blit(textlv2, textRectlv2)
        if drawGrid:
            drawG()
        if value >= len(im.Ua):
            value = 0
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        testdeath=0
#movement for the player
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                im.g5 = im.La[value]
                x += 5
                wi = 77
            if event.key == p.K_RIGHT:
                im.g5 = im.Ra[value]
                x -= 5
                wi = 77
            if event.key == p.K_UP:
                im.g5 = im.Ua[value]
                y += 5
                wi = 77
            if event.key == p.K_DOWN:
                im.g5 = im.Da[value]
                y -= 5
                wi = 87
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
    elif S == 1:
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
          ds.fill(color)
          color2 = (255,255,255)
        else:
          ds.fill(white)
          color2 = (0,0,0)
        for i in In.slotArray:
          i.draw(ds)
        for i in In.slotArray2:
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
        ds.blit(textlv2, textRectlv2)
      
        In.slotselect()
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
      if yes==0:
        save = im.g5
        im.g5 = im.battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
        sta.enem.defense = sta.Enemystats[sta.enem.image][0]
        sta.enem.attack = sta.Enemystats[sta.enem.image][1]
        sta.enem.maxHp = sta.Enemystats[sta.enem.image][2]
        sta.enem.Hp = sta.Enemystats[sta.enem.image][3]
        sta.enem.mana = sta.Enemystats[sta.enem.image][4]
        yes = 1
      im.P1 = p.transform.scale(im.g5,(pbw,pbh))
      playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
      enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
      ds.fill(white)
      enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
      playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
      eh=p.transform.scale(sta.enem.image,(50,50))
      ds.blit(eh,(350,50))
      ds.blit(im.P1,(pbx,pby))
      p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
      playerxp = 100-((Xp.gxp/Xp.xpn)*100)
      playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
      ds.blit(textHp,textRectHp)
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
              textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
              im.P1 = p.transform.scale(im.g5,(pbw,pbh))
              playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
              enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(sta.enem.image,(ebw,ebh))
              ds.blit(eh,(ebx,eby))
              ds.blit(im.P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              playerxp = 100-((Xp.gxp/Xp.xpn)*100)
              playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
              p.display.flip()
          damage(sta.enem,sta.mc)
          playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
          enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
          ds.fill(white)
          textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
          enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
          playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
          eh=p.transform.scale(sta.enem.image,(50,50))
          ds.blit(eh,(350,50))
          ds.blit(im.P1,(pbx,pby))
          p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
          ds.blit(textHp,textRectHp)
          playerxp = 100-((Xp.gxp/Xp.xpn)*100)
          playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
          p.display.flip()
          while at>=1:
              clock.tick(60)
              at-=1
              pbx -=11
              pby +=5
              pbh +=4
              pbw+=4
              textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
              im.P1 = p.transform.scale(im.g5,(pbw,pbh))
              playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
              enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              eh=p.transform.scale(sta.enem.image,(50,50))
              ds.blit(eh,(350,50))
              ds.blit(im.P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              playerxp = 100-((Xp.gxp/Xp.xpn)*100)
              playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
              p.display.flip()
          if sta.enem.Hp<=0:
            testdeath=1
            im.g5=save
            Xp.gainedxp(sta.hmmm)
            S=0
          else:
              while at<=21:
                  clock.tick(60)
                  at+=1
                  ebx -=11
                  eby +=5
                  ebh +=2
                  ebw+=2
                  textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
                  im.P1 = p.transform.scale(im.g5,(pbw,pbh))
                  playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
                  enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
                  ds.fill(white)
                  enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
                  playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
                  playerxp = 100-((Xp.gxp/Xp.xpn)*100)
                  playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
                  eh=p.transform.scale(sta.enem.image,(ebw,ebh))
                  ds.blit(eh,(ebx,eby))
                  ds.blit(im.P1,(pbx,pby))
                  p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
                  ds.blit(textHp,textRectHp)
                  p.display.flip()
              damage(sta.mc,sta.enem)
              playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
              enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
              ds.fill(white)
              textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
              im.P1 = p.transform.scale(im.g5,(pbw,pbh))
              playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
              enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
              ds.fill(white)
              enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
              playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
              playerxp = 100-((Xp.gxp/Xp.xpn)*100)
              playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
              eh=p.transform.scale(sta.enem.image,(ebw,ebh))
              ds.blit(eh,(ebx,eby))
              ds.blit(im.P1,(pbx,pby))
              p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
              ds.blit(textHp,textRectHp)
              p.display.flip()
              while at>=1:
                  clock.tick(60)
                  at-=1
                  ebx +=11
                  eby -=5
                  ebh -=2
                  ebw-=2
                  textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
                  im.P1 = p.transform.scale(im.g5,(pbw,pbh))
                  playerhp = (sta.mc.Hp/sta.mc.maxHp)*100
                  enemhp = (sta.enem.Hp/sta.enem.maxHp)*100
                  ds.fill(white)
                  enemy1hpbar=p.draw.rect(ds, red, p.Rect(350, 10, 100, 15)),p.draw.rect(ds, green, p.Rect(350, 10, enemhp, 15))
                  playerhpbar=p.draw.rect(ds, red, p.Rect(0, 215, 100, 10)),p.draw.rect(ds, green, p.Rect(0, 215, playerhp, 10))
                  eh=p.transform.scale(sta.enem.image,(ebw,ebh))
                  playerxp = 100-((Xp.gxp/Xp.xpn)*100)
                  playerxpbar=p.draw.rect(ds, (0,101,255), p.Rect(375, 215, 100, 10)),p.draw.rect(ds, (135,206,250), p.Rect(375, 215, 100-(playerxp+1), 10))
                  ds.blit(eh,(ebx,eby))
                  ds.blit(im.P1,(pbx,pby))
                  p.draw.rect(ds, grey, p.Rect(0, 225, 500, 90))
                  ds.blit(textHp,textRectHp)
                  p.display.flip()
          de=1
      elif not mouseover(textRect7):
        de=0
      if mouseover(textRect8):
        pbx-=20
        pby+=15
        print(de)
      if sta.enem.Hp<=0:
        im.g5=save
        testdeath = 1
        Xp.gainedxp(sta.hmmm)
        S=0
    elif S == None:
      ds.fill(black)
      ds.blit(text999,textRect999)
    collideU = rect1.collidepoint(sta.mc.rect.topleft) or rect1.collidepoint(sta.mc.rect.topright) or rect1.collidepoint(sta.mc.rect.midtop)
    collideD = rect1.collidepoint(sta.mc.rect.midbottom) or rect1.collidepoint(sta.mc.rect.bottomleft) or rect1.collidepoint(sta.mc.rect.bottomright)
    collideR = rect1.collidepoint(sta.mc.rect.midright) or rect1.collidepoint(sta.mc.rect.topright) or rect1.collidepoint(sta.mc.rect.bottomright)
    collideL = rect1.collidepoint(sta.mc.rect.midleft) or rect1.collidepoint(sta.mc.rect.topleft) or rect1.collidepoint(sta.mc.rect.bottomleft)
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
    if sta.mc.Hp<= 0:
      S=None
