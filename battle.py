import pygame as p
import sta
import im
import In
import Xp
import text
import random
import s
enemyattacking = 0
enemieshp=[0,0,0]
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (10, 10, 10)
black = (0, 0, 0)
color2 = (255, 255.255)
color = black
clock = p.time.Clock()
pm1w = 200
pm1h = 225
pm1x=130
pm1y=120
pm2w = 200
pm2h = 225
pm2x=0
pm2y=90
yes = 0
pbw = 200
pbh = 225
pbx = 80
pby = 80
ebw = 50
ebh = 50
ebx = 350
eby = 50
e2bw = 50
e2bh = 50
e2bx = 400
e2by = 30
e3bw = 50
e3bh = 50
e3bx = 300
e3by = 30
at = 0
de = 0
mx, my = p.mouse.get_pos()
defend = False
turns = 1
currentturn=1
selecx=125
selecy=40
minselecy=30
maxselecy=50
oncet1=0
oncet2=0
oncet3=0
def damage(wih, wht):
    dam = wht.attack + (random.randrange(1, (wht.attack+1))) - wih.defense
    if dam <= 0:
        pass
    if defend:
        wih.Hp -= round(dam / 2)
    elif dam > 0:
        wih.Hp -= dam


def mouseover(rect):
    global my, mx
    mx, my = p.mouse.get_pos()
    test = p.mouse.get_pressed()[0]
    if rect.collidepoint(mx, my):
        if test:
            return True


textHp = text.fonthp.render(
    str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
selector = p.transform.scale(im.selector,(25,25))
updown=1
pmattacking = 1
def battledraw():
    global textHp, pbx, pby, pbh,selecx,selecy, pbw,attacktest,de,enemyattacking,enemy1health,enemy2health,enemy3health,enemy1maxhealth,enemy2maxhealth,enemy3maxhealth,updown,minselecy,maxselecy,selector,currentturn,oncet1,oncet2,oncet3,pmattacking
    textHp = text.fonthp.render(
        str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
    textXp = text.fonthp.render(
        str(Xp.gxp) + '/' + str(round(Xp.xpn)), True, black)
    if not currentturn > sta.partyamount:
      selector = p.transform.scale(im.selector,(25,25))
    im.P1 = p.transform.scale(im.g5, (pbw, pbh))
    playerhp = (sta.mc.Hp / sta.mc.maxHp) * 100
    enem1hp = (enemy1health / enemy1maxhealth) * 100
    if not sta.hmmm2 == None:
      enem2hp = (enemy2health / enemy2maxhealth) * 100
    if not sta.hmmm3 == None:
      enem3hp = (enemy3health / enemy3maxhealth) * 100
    s.ds.fill(white)
    if not enemieshp[1]<=0 and sta.enemammount >= 2:
      enemy2hpbar = p.draw.rect(s.ds, red,p.Rect(390, 5, 100, 15)), p.draw.rect(s.ds, green, p.Rect(390, 5, enem2hp, 15))
      enem2 = p.transform.scale(sta.enem.image2, (e2bw, e2bh))
      s.ds.blit(enem2, (e2bx, e2by))
    if not enemieshp[2]<=0 and sta.enemammount == 3: 
      enemy3hpbar = p.draw.rect(s.ds, red,p.Rect(270, 5, 100, 15)), p.draw.rect(s.ds, green, p.Rect(270, 5, enem3hp, 15))
      enem3 = p.transform.scale(sta.enem.image3, (e3bw, e3bh))
      s.ds.blit(enem3, (e3bx, e3by))
    if not enemieshp[0]<=0:
      enem1 = p.transform.scale(sta.enem.image, (ebw, ebh))
      s.ds.blit(enem1, (ebx, eby))
      enemy1hpbar = p.draw.rect(s.ds, red,p.Rect(330, 30, 100, 15)), p.draw.rect(s.ds, green, p.Rect(330, 30, enem1hp, 15))
    s.ds.blit(im.P1, (pbx, pby))
    pm2 = p.transform.scale(im.party2, (pm2w, pm2h))
    pm1 = p.transform.scale(im.party1, (pm1w, pm1h))
    s.ds.blit(pm2, (pm2x, pm2y))
    s.ds.blit(pm1, (pm1x, pm1y))
    p.draw.rect(s.ds, grey, p.Rect(0, 225, 500, 90))
    playerhpbar = p.draw.rect(s.ds, red, p.Rect(0, 215, 100, 10)), p.draw.rect(
        s.ds, green, p.Rect(0, 215, playerhp, 10))
    s.ds.blit(textHp, text.textRectHp)
    playerxp = 100 - ((Xp.gxp / Xp.xpn) * 100)
    playerxpbar = p.draw.rect(s.ds, (0, 101, 255),
                              p.Rect(375, 215, 100, 10)), p.draw.rect(
                                  s.ds, (135, 206, 250),
                                  p.Rect(375, 215, 100 - (playerxp + 1), 10))
    if not currentturn > sta.partyamount:
      s.ds.blit(selector,(selecx,selecy))
      if currentturn ==1:
        selecx = 125
        minselecy = 40
        maxselecy = 60
        if oncet1 ==0:
          selecy = 40
          updown = 1
          pmattacking=1
          oncet1 = 1
      if sta.partyamount >=2:
        if currentturn ==2:
          selecx = 175
          minselecy = 70
          maxselecy = 90
          if oncet2 ==0:
            selecy = 70
            updown = 1
            pmattacking=2
            oncet2 = 1
      if sta.partyamount ==3:
        if currentturn ==3:
          selecx = 45
          minselecy = 30
          maxselecy = 50
          if oncet3 ==0:
            selecy = 30
            updown = 1
            pmattacking=3
            oncet3 = 1
    else:
      oncet1=0
      oncet2=0
      oncet3=0
    if updown ==1:
      if selecy >minselecy:
        selecy-=1
      elif selecy ==minselecy:
        updown=2
    elif updown ==2:
      if selecy <maxselecy:
        selecy+=1
      elif selecy ==maxselecy:
        updown=1
    s.ds.blit(textXp, text.textRectXp)
    if not attacktest:
      s.ds.blit(text.text7, text.textRect7)
      s.ds.blit(text.text8, text.textRect8)
      s.ds.blit(text.text9, text.textRect9)
      s.ds.blit(text.text10, text.textRect10)
    elif attacktest:
      if not enemieshp[0]<=0:
        enem1_ = p.transform.scale(sta.enem.image, (15, 15))
        enem1_5=s.ds.blit(enem1_, (30, 230))
        enemy1hpbarred = p.draw.rect(s.ds,red,p.Rect(70,230,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 230, enem1hp, 15))
        if mouseover(enemy1hpbarred) or mouseover(enem1_5):
          attacktest = False
          enemyattacking =1
          if pmattacking==1:
            playerattack()
          if pmattacking==2:
            p1attack()
          if pmattacking==3:
            p2attack()
          de = 0
      if not enemieshp[1]<=0 and sta.enemammount >=2:
        enem2_ = p.transform.scale(sta.enem.image2, (15, 15))
        enem2_5=s.ds.blit(enem2_, (30, 250))
        enemy2hpbarred = p.draw.rect(s.ds,red,p.Rect(70,250,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 250, enem2hp, 15))
        if mouseover(enemy2hpbarred) or mouseover(enem2_5):
          attacktest = False
          enemyattacking =2
          if pmattacking==1:
            playerattack()
          if pmattacking==2:
            p1attack()
          if pmattacking==3:
            p2attack()
          de = 0
      if not enemieshp[2]<=0 and sta.enemammount ==3:
        enem3_ = p.transform.scale(sta.enem.image3, (15, 15))
        enem3_5=s.ds.blit(enem3_, (30, 270))
        enemy3hpbarred = p.draw.rect(s.ds,red,p.Rect(70,270,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 270, enem3hp, 15))
        if mouseover(enemy3hpbarred) or mouseover(enem3_5):
          attacktest = False
          enemyattacking =3
          if pmattacking==1:
            playerattack()
          if pmattacking==2:
            p1attack()
          if pmattacking==3:
            p2attack()
          de = 0

      
    s.screen.blit(s.ds, (0, 0))
    p.display.flip()

enemy1health=0
enemy2health=0
enemy3health=0
enemy1maxhealth=0
enemy2maxhealth=0
enemy3maxhealth=0

c11=0
c12=0
c13=0
oncet4=0
oncet5=0
oncet6=0
def battlesequence():
    global yes, pbw, pbh, pbx, pby, ebw, ebh, ebx, eby, de, at, clock, save,attacktest,enemy1health,enemy2health,enemy3health,enemy1maxhealth,enemy2maxhealth,enemy3maxhealth,c11,c12,c13,turns,currentturn,oncet4,oncet5,oncet6
    clock.tick(60)
    if yes == 0:
        save = im.g5
        im.g5 = im.battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]      
        sta.enem.image = sta.hmmm
        sta.enem.image2 = sta.hmmm2
        sta.enem.image3 = sta.hmmm3
        sta.enem.defense = sta.Enemystats[sta.enem.image][0]
        sta.enem.attack = sta.Enemystats[sta.enem.image][1]
        enemy1maxhealth = sta.Enemystats[sta.enem.image][2]
        if not sta.hmmm2 == None:
          enemy2maxhealth = sta.Enemystats[sta.enem.image2][2]
        if not sta.hmmm3 == None:
          enemy3maxhealth = sta.Enemystats[sta.enem.image3][2]
        enemy1health = sta.Enemystats[sta.enem.image][3]
        if not sta.hmmm2 == None:
          enemy2health = sta.Enemystats[sta.enem.image2][3]
        if not sta.hmmm3 == None:
          enemy3health = sta.Enemystats[sta.enem.image3][3]
        sta.enem.mana = sta.Enemystats[sta.enem.image][4]
        turns = sta.enemammount + sta.partyamount
        yes = 1
    battledraw()
    enemieshp[0] = enemy1health
    enemieshp[1] = enemy2health
    enemieshp[2] = enemy3health
    if not currentturn > sta.partyamount:
      if not attacktest:
        Defend()
      attackcheck()
    if currentturn > sta.partyamount:
      if currentturn == sta.partyamount+1:
        if oncet4==0 and not enemieshp[0]<=0:
          enemyattack1()
          currentturn+=1
          oncet4=1
      if sta.enemammount >=2:
        if currentturn == sta.partyamount+2:
          if oncet5==0 and not enemieshp[1]<=0:
            enemyattack2()
            currentturn+=1
            oncet5=1
      if sta.enemammount ==3:
        if currentturn == sta.partyamount+3:
          if oncet6==0 and not enemieshp[2]<=0:
            enemyattack3()
            currentturn+=1
            oncet6=1
    if currentturn > turns:
      currentturn=1
    if enemieshp[0]<=0 and c11==0:
      Xp.gainedxp(sta.hmmm)
      c11=1
    if sta.enemammount >=2:  
      if enemieshp[1]<=0 and c12==0:
        Xp.gainedxp(sta.hmmm2)
        c12=1
    if sta.enemammount == 3:
      if enemieshp[2]<=0 and c13==0:
        Xp.gainedxp(sta.hmmm3)
        c13=1
    if enemieshp[0]<=0:
      if enemieshp[1]<=0 or sta.enemammount<2:
        if enemieshp[2]<=0 or sta.enemammount<3:
          c11=0
          c12=0
          c13=0
          im.g5 = save
          sta.S = 0
          yes = 0

  
def Defend():
    global defend, de
    if mouseover(text.textRect8) and de == 0:
        defend = True
        enemyattack()
        de = 1

attacktest=False
def attackcheck():
  global attacktest
  if mouseover(text.textRect7):
    attacktest = True
    


def playerattack():
    global pbw, pbh, pbx, pby, de, at, save, yes,enemyattacking,enemy1health,enemy2health,enemy3health,currentturn
    if enemyattacking==1:
      sta.enem.Hp=  enemy1health
      _x=11
      _y=5
    elif enemyattacking==2:
      sta.enem.Hp=  enemy2health
      _x=14
      _y=5.5
    elif enemyattacking==3:
      sta.enem.Hp=  enemy3health
      _x=9
      _y=5.5
    if de == 0:
            while at <= 21:
                clock.tick(60)
                at += 1
                pbx += _x
                pby -= _y
                pbh -= 4
                pbw -= 4
                battledraw()
            damage(sta.enem, sta.mc)
            if enemyattacking==1:
              enemy1health=  sta.enem.Hp
            elif enemyattacking==2:
              enemy2health=  sta.enem.Hp
            elif enemyattacking==3:
              enemy3health=  sta.enem.Hp
            battledraw()
            while at >= 1:
                clock.tick(60)
                at -= 1
                pbx -= _x
                pby += _y
                pbh += 4
                pbw += 4
                battledraw()
            currentturn += 1
            de = 1

def p1attack():
    global pm1w, pm1h, pm1x, pm1y, de, at, save, yes,enemyattacking,enemy1health,enemy2health,enemy3health,currentturn
    if enemyattacking==1:
      sta.enem.Hp=  enemy1health
      _x=9
      _y=5.5
    elif enemyattacking==2:
      sta.enem.Hp=  enemy2health
      _x=12
      _y=6
    elif enemyattacking==3:
      sta.enem.Hp=  enemy3health
      _x=7
      _y=6
    if de == 0:
            while at <= 21:
                clock.tick(60)
                at += 1
                pm1x += _x
                pm1y -= _y
                pm1h -= 4
                pm1w -= 4
                battledraw()
            damage(sta.enem, sta.mc)
            if enemyattacking==1:
              enemy1health=  sta.enem.Hp
            elif enemyattacking==2:
              enemy2health=  sta.enem.Hp
            elif enemyattacking==3:
              enemy3health=  sta.enem.Hp
            battledraw()
            while at >= 1:
                clock.tick(60)
                at -= 1
                pm1x -= _x
                pm1y += _y
                pm1h += 4
                pm1w += 4
                battledraw()
            currentturn+=1
            de = 1

def p2attack():
    global pm2w, pm2h, pm2x, pm2y, de, at, save, yes,enemyattacking,enemy1health,enemy2health,enemy3health,currentturn
    if enemyattacking==1:
      sta.enem.Hp=  enemy1health
      _x=15
      _y=5
    elif enemyattacking==2:
      sta.enem.Hp=  enemy2health
      _x=18
      _y=5.5
    elif enemyattacking==3:
      sta.enem.Hp=  enemy3health
      _x=13
      _y=5.5
    if de == 0:
            while at <= 21:
                clock.tick(60)
                at += 1
                pm2x += _x
                pm2y -= _y
                pm2h -= 4
                pm2w -= 4
                battledraw()
            damage(sta.enem, sta.mc)
            if enemyattacking==1:
              enemy1health=  sta.enem.Hp
            elif enemyattacking==2:
              enemy2health=  sta.enem.Hp
            elif enemyattacking==3:
              enemy3health=  sta.enem.Hp
            battledraw()
            while at >= 1:
                clock.tick(60)
                at -= 1
                pm2x -= _x
                pm2y += _y
                pm2h += 4
                pm2w += 4
                battledraw()
            currentturn+=1
            de = 1


def enemyattack1():
    global at, ebx, eby, ebh, ebw, de, save
    pmattacking = random.randrange(1,sta.partyamount+1)
    if pmattacking==1:
      _x=11
      _y=5
    elif pmattacking==2:
     _x=14
     _y=5.5
    elif pmattacking==3:
      _x=9
      _y=5.5
    while at <= 21:
        clock.tick(6)
        at += 1
        ebx -= _x
        eby += _y
        ebh += 2
        ebw += 2
        battledraw()
    damage(sta.mc, sta.enem)
    battledraw()
    while at >= 1:
        clock.tick(6)
        at -= 1
        ebx += _x
        eby -= _y
        ebh -= 2
        ebw -= 2
        battledraw()
    if sta.mc.Hp <= 0:
        sta.S = None

def enemyattack2():
    global at, e2bx, e2by, e2bh, e2bw, de, save
    pmattacking = random.randrange(1,sta.partyamount+1)
    if pmattacking==1:
      _x=9
      _y=5
    elif pmattacking==2:
      _x=12
      _y=5.5
    elif pmattacking==3:
      _x=7
      _y=5.5
    while at <= 21:
        clock.tick(6)
        at += 1
        e2bx -= _x
        e2by += _y
        e2bh += 2
        e2bw += 2
        battledraw()
    damage(sta.mc, sta.enem)
    battledraw()
    while at >= 1:
        clock.tick(6)
        at -= 1
        e2bx += _x
        e2by -= _y
        e2bh -= 2
        e2bw -= 2
        battledraw()
    if sta.mc.Hp <= 0:
        sta.S = None

def enemyattack3():
    global at, e3bx, e3by, e3bh, e3bw, de, save
    pmattacking = random.randrange(1,sta.partyamount+1)
    if pmattacking==1:
      _x=9
      _y=5
    elif pmattacking==2:
      _x=12
      _y=5.5
    elif pmattacking==3:
      _x=7
      _y=5.5
    while at <= 21:
        clock.tick(6)
        at += 1
        e3bx -= _x
        e3by += _y
        e3bh += 2
        e3bw += 2
        battledraw()
    damage(sta.mc, sta.enem)
    battledraw()
    while at >= 1:
        clock.tick(6)
        at -= 1
        e3bx += _x
        e3by -= _y
        e3bh -= 2
        e3bw -= 2
        battledraw()
    if sta.mc.Hp <= 0:
        sta.S = None
