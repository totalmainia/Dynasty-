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
at = 0
de = 0
mx, my = p.mouse.get_pos()

defend = False


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


def battledraw():
    global textHp, pbx, pby, pbh, pbw,attacktest,de,enemyattacking
    textHp = text.fonthp.render(
        str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
    im.P1 = p.transform.scale(im.g5, (pbw, pbh))
    playerhp = (sta.mc.Hp / sta.mc.maxHp) * 100
    enem1hp = (sta.enem.Hp1 / sta.enem.maxHp1) * 100
    enemieshp[0]= sta.enem.Hp1
    s.ds.fill(white)
    enemy1hpbar = p.draw.rect(s.ds, red,
                              p.Rect(350, 10, 100, 15)), p.draw.rect(
                                  s.ds, green, p.Rect(350, 10, enem1hp, 15))
    enem1 = p.transform.scale(sta.enem.image, (ebw, ebh))
    s.ds.blit(enem1, (ebx, eby))
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
    s.ds.blit(textHp, text.textRectHp)
    if not attacktest:
      s.ds.blit(text.text7, text.textRect7)
      s.ds.blit(text.text8, text.textRect8)
      s.ds.blit(text.text9, text.textRect9)
      s.ds.blit(text.text10, text.textRect10)
    elif attacktest:
      if not enemieshp[0]==0:
        enem1_ = p.transform.scale(sta.enem.image, (25, 25))
        enem1_5=s.ds.blit(enem1_, (30, 225))
        enemy1hpbarred = p.draw.rect(s.ds,red,p.Rect(70,230,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 230, enem1hp, 15))
        if mouseover(enemy1hpbarred) or mouseover(enem1_5):
          attacktest = False
          enemyattacking =2
          playerattack()
          de = 0
      if not enemieshp[1]==0:
        enem2_ = p.transform.scale(sta.enem.image, (25, 25))
        enem2_5=s.ds.blit(enem2_, (30, 245))
        enemy2hpbarred = p.draw.rect(s.ds,red,p.Rect(70,275,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 275, enem1hp, 15))
        if mouseover(enemy2hpbarred) or mouseover(enem2_5):
          attacktest = False
          playerattack()
          de = 0
      if not enemieshp[2]==0:
        enem3_ = p.transform.scale(sta.enem.image, (25, 25))
        enem3_5=s.ds.blit(enem3_, (30, 245))
        enemy3hpbarred = p.draw.rect(s.ds,red,p.Rect(70,250,100,15))
        p.draw.rect(s.ds, green, p.Rect(70, 250, enem1hp, 15))
        if mouseover(enemy3hpbarred) or mouseover(enem3_5):
          attacktest = False
          playerattack()
          de = 0

      
    s.screen.blit(s.ds, (0, 0))
    p.display.flip()


def battlesequence():
    global yes, pbw, pbh, pbx, pby, ebw, ebh, ebx, eby, de, at, clock, save,attacktest
    clock.tick(60)
    if yes == 0:
        save = im.g5
        im.g5 = im.battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
        sta.enem.defense1 = sta.Enemystats[sta.enem.image][0]
        sta.enem.attack1 = sta.Enemystats[sta.enem.image][1]
        sta.enem.maxHp1 = sta.Enemystats[sta.enem.image][2]
        sta.enem.Hp1 = sta.Enemystats[sta.enem.image][3]
        sta.enem.mana1 = sta.Enemystats[sta.enem.image][4]
        yes = 1
    battledraw()
    if not attacktest:
      Defend()
    attackcheck()
    if enemieshp[0]<=0:
      if enemieshp[1]<=0:
        if enemieshp[2]<=0:
          im.g5 = save
          Xp.gainedxp(sta.hmmm)
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
    global pbw, pbh, pbx, pby, de, at, save, yes,enemyattacking
    if enemyattacking==1:
      _x=11
      _y=5
    elif enemyattacking==2:
      _x=16
      _y=5.5
    if de == 0:
            while at <= 21:
                clock.tick(6)
                at += 1
                pbx += _x
                pby -= _y
                pbh -= 4
                pbw -= 4
                battledraw()
            damage(sta.enem, sta.mc)
            battledraw()
            while at >= 1:
                clock.tick(60)
                at -= 1
                pbx -= _x
                pby += _y
                pbh += 4
                pbw += 4
                battledraw()
            de = 1


def enemyattack():
    global at, ebx, eby, ebh, ebw, de, save
    if de == 0:
        while at <= 21:
            clock.tick(60)
            at += 1
            ebx -= 11
            eby += 5
            ebh += 2
            ebw += 2
            battledraw()
        damage(sta.mc, sta.enem)
        battledraw()
        while at >= 1:
            clock.tick(60)
            at -= 1
            ebx += 11
            eby -= 5
            ebh -= 2
            ebw -= 2
            battledraw()
        if sta.mc.Hp <= 0:
            sta.S = None
        de = 1
