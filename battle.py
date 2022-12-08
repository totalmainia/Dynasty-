import pygame as p
import sta
import im
import In
import Xp
import text
import random
import s

enemyattacking = 0
enemieshp = [0, 0, 0]
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (150, 150, 150)
black = (0, 0, 0)
color2 = (255, 255.255)
color = black
clock = p.time.Clock()
pm1w = 170
pm1h = 215
pm1x = 130
pm1y = 120
pm2w = 170
pm2h = 215
pm2x = 0
pm2y = 90
yes = 0
pbw = 170
pbh = 215
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
currentturn = 1
selecx = 125
selecy = 40
minselecy = 30
maxselecy = 50
eselecx = 180
eselecy = 230
eminselecx = 180
emaxselecx = 200
oncet1 = 0
oncet2 = 0
oncet3 = 0
leftright = 1
onceanim = 0
playerminix = 35
pm1minix = 35
pm2minix = 35
selecenem = 1
selectorover = 1
battleselec = 0


def damage(wih, wht):
    dam = wht.attack + (random.randrange(1, (wht.attack + 1))) - wih.defense
    if dam <= 0:
        pass
    if wih.defend:
        wih.Hp -= round(dam / 2)
    elif dam > 0:
        wih.Hp -= dam


length = []


def selectanim(num):
    global onceanim, playerminix, pm1minix, pm2minix
    if onceanim == 0:
        if num == 1:
            minix = playerminix
        elif num == 2:
            minix = pm1minix
        elif num == 3:
            minix = pm2minix
        while minix < 40:
            clock.tick(60)
            if num == 1:
                playerminix += 1
            elif num == 2:
                pm1minix += 1
            elif num == 3:
                pm2minix += 1
            minix += 1
            battledraw()
            s.screen.blit(s.ds, (0, 0))
            p.display.flip()
        while minix > 30:
            clock.tick(60)
            if num == 1:
                playerminix -= 1
            elif num == 2:
                pm1minix -= 1
            elif num == 3:
                pm2minix -= 1
            minix -= 1
            battledraw()
            s.screen.blit(s.ds, (0, 0))
            p.display.flip()
        while minix < 40:
            clock.tick(60)
            if num == 1:
                playerminix += 1
            elif num == 2:
                pm1minix += 1
            elif num == 3:
                pm2minix += 1
            minix += 1
            battledraw()
            s.screen.blit(s.ds, (0, 0))
            p.display.flip()
        while minix > 35:
            clock.tick(60)
            if num == 1:
                playerminix -= 1
            elif num == 2:
                pm1minix -= 1
            elif num == 3:
                pm2minix -= 1
            minix -= 1
            battledraw()
            s.screen.blit(s.ds, (0, 0))
            p.display.flip()
        onceanim = 1


def mouseover(rect):
    global my, mx
    mx, my = p.mouse.get_pos()
    test = p.mouse.get_pressed()[0]
    if rect.collidepoint(mx, my):
        if test:
            return True


textHp = text.fonthp.render(
    str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
selector = p.transform.scale(im.selector, (25, 25))
updown = 1
pmattacking = 1
playermini = p.transform.scale(sta.mc.mini, (15, 20))
pm1mini = p.transform.scale(sta.pm1.mini, (15, 20))
pm2mini = p.transform.scale(sta.pm2.mini, (15, 20))

selectorover = 1
pm2 = p.transform.scale(im.party2, (pm2w, pm2h))
pm1 = p.transform.scale(im.party1, (pm1w, pm1h))
battleonce = 0
magictest = False


def battledraw():
    global textHp, pbx, pby, pbh, selecx, selecy, pbw, attacktest, de, enemyattacking, enemy1health, enemy2health, enemy3health, enemy1maxhealth, enemy2maxhealth, enemy3maxhealth, updown, minselecy, maxselecy, selector, currentturn, oncet1, oncet2, oncet3, oncet4, oncet5, oncet6, pmattacking, playerminix, pm1minix, pm2minix, playermini, pm1mini, pm2mini, selectorover, onceanim, pm1, pm2, leftright, eselecx, eselecy, emaxselecx, eminselecx, selectenem, battleselec, battleonce, magictest
    text.playerlv = text.fontahhh.render('Lv:' + str(sta.mc.level), True,
                                         black)
    text.pm1lv = text.fontahhh.render('Lv:' + str(sta.pm1.level), True, black)
    text.pm2lv = text.fontahhh.render('Lv:' + str(sta.pm2.level), True, black)
    if sta.mc.clas <= 2:
        text.text7 = text.font3.render('Attack', True, text.colora, text.grey)
    else:
        text.text7 = text.font3.render('Missle', True, text.colora, text.grey)
    text.text8 = text.font3.render('Defend', True, text.colord, text.grey)
    if sta.mc.clas >= 2:
        text.text9 = text.font3.render('Magic', True, text.colorm, text.grey)
    else:
        text.text9 = text.font3.render('Skills', True, text.colorm, text.grey)
    text.text10 = text.font3.render('Potion', True, text.colorp, text.grey)
    if sta.mc.hasattacked:
        im.g5 = im.darkP1
    elif not sta.mc.hasattacked:
        im.g5 = im.battleP1
    if sta.pm1.hasattacked:
        im.party1 = im.darkP1
    elif not sta.pm1.hasattacked:
        im.party1 = im.battleP1
    if sta.pm2.hasattacked:
        im.party2 = im.darkP1
    elif not sta.pm2.hasattacked:
        im.party2 = im.battleP1
    textHp = text.fonthp.render(
        str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
    if sta.partyamount >= 2:
        textHp1 = text.fonthp.render(
            str(sta.pm1.Hp) + '/' + str(sta.pm1.maxHp), True, black)
    if sta.partyamount == 3:
        textHp2 = text.fonthp.render(
            str(sta.pm2.Hp) + '/' + str(sta.pm2.maxHp), True, black)
    textXp = text.fonthp.render(
        str(Xp.gxp) + '/' + str(round(Xp.xpn)), True, black)
    if sta.partyamount >= 2:
        textXp1 = text.fonthp.render(
            str(Xp.pm1gxp) + '/' + str(round(Xp.pm1xpn)), True, black)
    if sta.partyamount == 3:
        textXp2 = text.fonthp.render(
            str(Xp.pm2gxp) + '/' + str(round(Xp.pm2xpn)), True, black)
    if not currentturn > sta.partyamount:
        selector = p.transform.scale(im.selector, (25, 25))
    im.P1 = p.transform.scale(im.g5, (pbw, pbh))
    playerhp = (sta.mc.Hp / sta.mc.maxHp) * 100
    pm1hp = (sta.pm1.Hp / sta.pm1.maxHp) * 100
    pm2hp = (sta.pm2.Hp / sta.pm2.maxHp) * 100
    enem1hp = (enemy1health / enemy1maxhealth) * 100
    if not sta.hmmm2 == None:
        enem2hp = (enemy2health / enemy2maxhealth) * 100
    if not sta.hmmm3 == None:
        enem3hp = (enemy3health / enemy3maxhealth) * 100
    s.ds.fill(white)
    if not enemieshp[1] <= 0 and sta.enemammount >= 2:
        enemy2hpbar = p.draw.rect(s.ds, red,
                                  p.Rect(390, 5, 100, 15)), p.draw.rect(
                                      s.ds, green, p.Rect(390, 5, enem2hp, 15))
        enem2 = p.transform.scale(sta.enem.image2, (e2bw, e2bh))
        s.ds.blit(enem2, (e2bx, e2by))
    if not enemieshp[2] <= 0 and sta.enemammount == 3:
        enemy3hpbar = p.draw.rect(s.ds, red,
                                  p.Rect(270, 5, 100, 15)), p.draw.rect(
                                      s.ds, green, p.Rect(270, 5, enem3hp, 15))
        enem3 = p.transform.scale(sta.enem.image3, (e3bw, e3bh))
        s.ds.blit(enem3, (e3bx, e3by))
    if not enemieshp[0] <= 0:
        enem1 = p.transform.scale(sta.enem.image, (ebw, ebh))
        s.ds.blit(enem1, (ebx, eby))
        enemy1hpbar = p.draw.rect(s.ds, red, p.Rect(
            330, 30, 100, 15)), p.draw.rect(s.ds, green,
                                            p.Rect(330, 30, enem1hp, 15))
    s.ds.blit(im.P1, (pbx, pby))
    pm2 = p.transform.scale(im.party2, (pm2w, pm2h))
    pm1 = p.transform.scale(im.party1, (pm1w, pm1h))
    if not sta.pm2.Hp <= 0 and sta.partyamount == 3:
        s.ds.blit(pm2, (pm2x, pm2y))
    if not sta.pm1.Hp <= 0 and sta.partyamount >= 2:
        s.ds.blit(pm1, (pm1x, pm1y))
    p.draw.rect(s.ds, grey, p.Rect(0, 225, 500, 90))
    playerxp = 100 - ((Xp.gxp / Xp.xpn) * 100)
    pm1xp = 100 - ((Xp.pm1gxp / Xp.pm1xpn) * 100)
    pm2xp = 100 - ((Xp.pm2gxp / Xp.pm2xpn) * 100)
    if not currentturn > sta.partyamount:
        oncet4 = 0
        oncet5 = 0
        oncet6 = 0
        if not attacktest and not magictest:
            s.ds.blit(selector, (selecx, selecy))
    else:
        oncet1 = 0
        oncet2 = 0
        oncet3 = 0
    if updown == 1:
        if selecy > minselecy:
            selecy -= 1
        elif selecy == minselecy:
            updown = 2
    elif updown == 2:
        if selecy < maxselecy:
            selecy += 1
        elif selecy == maxselecy:
            updown = 1
    if leftright == 1:
        if eselecx > eminselecx:
            eselecx -= 1
        elif eselecx == eminselecx:
            leftright = 2
    elif leftright == 2:
        if eselecx < emaxselecx:
            eselecx += 1
        elif eselecx == emaxselecx:
            leftright = 1
    playermini = p.transform.scale(sta.mc.mini, (15, 20))
    pm1mini = p.transform.scale(sta.pm1.mini, (15, 20))
    pm2mini = p.transform.scale(sta.pm2.mini, (15, 20))
    if not attacktest and not magictest:
        s.ds.blit(text.text7, text.textRect7)
        s.ds.blit(text.text8, text.textRect8)
        s.ds.blit(text.text9, text.textRect9)
        s.ds.blit(text.text10, text.textRect10)
        s.ds.blit(playermini, (playerminix, 225))
        playerhpbar = p.draw.rect(s.ds, red, p.Rect(
            70, 230, 100, 15)), p.draw.rect(s.ds, green,
                                            p.Rect(70, 230, playerhp, 15))
        s.ds.blit(textHp, text.textRectHp)
        playerxpbar = p.draw.rect(s.ds, (0, 101, 255), p.Rect(
            180, 230, 100,
            15)), p.draw.rect(s.ds, (135, 206, 250),
                              p.Rect(180, 230, 100 - (playerxp + 1), 15))
        playerRectlv = text.playerlv.get_rect()
        playerRectlv.topleft = (280, 230)
        s.ds.blit(text.playerlv, playerRectlv)
        s.ds.blit(textXp, text.textRectXp)
        if not sta.pm1.Hp <= 0 and sta.partyamount >= 2:
            s.ds.blit(pm1mini, (pm1minix, 245))
            pm1healthbar = p.draw.rect(s.ds, red, p.Rect(70, 250, 100, 15))
            p.draw.rect(s.ds, green, p.Rect(70, 250, pm1hp, 15))
            s.ds.blit(textHp1, text.textRectHp1)
            pm1xpbar = p.draw.rect(s.ds, (0, 101, 255),
                                   p.Rect(180, 250, 100, 15)), p.draw.rect(
                                       s.ds, (135, 206, 250),
                                       p.Rect(180, 250, 100 - (pm1xp + 1), 15))
            pm1Rectlv = text.pm1lv.get_rect()
            pm1Rectlv.topleft = (280, 250)
            s.ds.blit(text.pm1lv, pm1Rectlv)
            s.ds.blit(textXp1, text.textRectXp1)
        if not sta.pm2.Hp <= 0 and sta.partyamount == 3:
            s.ds.blit(pm2mini, (pm2minix, 265))
            pm2healthbar = p.draw.rect(s.ds, red, p.Rect(70, 270, 100, 15))
            p.draw.rect(s.ds, green, p.Rect(70, 270, pm2hp, 15))
            s.ds.blit(textHp2, text.textRectHp2)
            pm2xpbar = p.draw.rect(s.ds, (0, 101, 255),
                                   p.Rect(180, 270, 100, 15)), p.draw.rect(
                                       s.ds, (135, 206, 250),
                                       p.Rect(180, 270, 100 - (pm2xp + 1), 15))
            pm2Rectlv = text.pm2lv.get_rect()
            pm2Rectlv.topleft = (280, 270)
            s.ds.blit(text.pm2lv, pm2Rectlv)
            s.ds.blit(textXp2, text.textRectXp2)
    elif attacktest:
        if not enemieshp[0] <= 0:
            enem1_ = p.transform.scale(sta.enem.image, (15, 15))
            enem1_5 = s.ds.blit(enem1_, (30, 230))
            enemy1hpbarred = p.draw.rect(s.ds, red, p.Rect(70, 230, 100, 15))
            p.draw.rect(s.ds, green, p.Rect(70, 230, enem1hp, 15))
            if mouseover(enemy1hpbarred) or mouseover(enem1_5):
                attacktest = False
                enemyattacking = 1
                if pmattacking == 1:
                    playerattack()
                if pmattacking == 2:
                    p1attack()
                if pmattacking == 3:
                    p2attack()
                de = 0
        if not enemieshp[1] <= 0 and sta.enemammount >= 2:
            enem2_ = p.transform.scale(sta.enem.image2, (15, 15))
            enem2_5 = s.ds.blit(enem2_, (30, 250))
            enemy2hpbarred = p.draw.rect(s.ds, red, p.Rect(70, 250, 100, 15))
            p.draw.rect(s.ds, green, p.Rect(70, 250, enem2hp, 15))
            if mouseover(enemy2hpbarred) or mouseover(enem2_5):
                attacktest = False
                enemyattacking = 2
                if pmattacking == 1:
                    playerattack()
                if pmattacking == 2:
                    p1attack()
                if pmattacking == 3:
                    p2attack()
                de = 0
        if not enemieshp[2] <= 0 and sta.enemammount == 3:
            enem3_ = p.transform.scale(sta.enem.image3, (15, 15))
            enem3_5 = s.ds.blit(enem3_, (30, 270))
            enemy3hpbarred = p.draw.rect(s.ds, red, p.Rect(70, 270, 100, 15))
            p.draw.rect(s.ds, green, p.Rect(70, 270, enem3hp, 15))
            if mouseover(enemy3hpbarred) or mouseover(enem3_5):
                attacktest = False
                enemyattacking = 3
                if pmattacking == 1:
                    playerattack()
                if pmattacking == 2:
                    p1attack()
                if pmattacking == 3:
                    p2attack()
                de = 0
    elif magictest:
        if selectorover == 1:
          playermana = (sta.mc.currentmana / sta.mc.mana)*100
          if sta.mc.clas >=2:
            playerbar = text.fonthp.render('Mana:'+str(sta.mc.currentmana)+'/'+str(sta.mc.mana),True,black)
            manabar = p.draw.rect(s.ds, (60,0,100), p.Rect(0, 210, 100, 15)), p.draw.rect(s.ds, (235,205,255), p.Rect(0, 210, playermana, 15))
            s.ds.blit(playerbar,(5,213))
          else:
            playerbar = text.fonthp.render('Energy:'+str(sta.mc.currentmana)+'/'+str(sta.mc.mana),True,black)
            manabar = p.draw.rect(s.ds, (0,0,139), p.Rect(0, 210, 100, 15)),p.draw.rect(s.ds, (173,216,230), p.Rect(0, 210, playermana, 15))
            s.ds.blit(playerbar,(5,213))
        if selectorover == 2:
          pm1mana = (sta.pm1.currentmana / sta.pm1.mana)*100
          if sta.pm1.clas >=2:
            pm1bar = text.fonthp.render('Mana:'+str(sta.pm1.currentmana)+'/'+str(sta.pm1.mana),True,black)
            manabar = p.draw.rect(s.ds, (60,0,100), p.Rect(0, 210, 100, 15)), p.draw.rect(s.ds, (235,205,255), p.Rect(0, 210, pm1mana, 15))
            s.ds.blit(pm1bar,(5,213))
          else:
            pm1bar = text.fonthp.render('Energy:'+str(sta.pm1.currentmana)+'/'+str(sta.pm1.mana),True,black)
            manabar = p.draw.rect(s.ds, (0,0,139), p.Rect(0, 210, 100, 15)),p.draw.rect(s.ds, (173,216,230), p.Rect(0, 210, pm1mana, 15))
            s.ds.blit(pm1bar,(5,213))
        if selectorover == 3:
          pm2mana = (sta.pm2.currentmana / sta.pm2.mana)*100
          if sta.pm2.clas >=2:
            pm2bar = text.fonthp.render('Mana:'+str(sta.pm2.currentmana)+'/'+str(sta.pm2.mana),True,black)
            manabar = p.draw.rect(s.ds, (60,0,100), p.Rect(0, 210, 100, 15)), p.draw.rect(s.ds, (235,205,255), p.Rect(0, 210, pm2mana, 15))
            s.ds.blit(pm2bar,(5,213))
          else:
            pm2bar = text.fonthp.render('Energy:'+str(sta.pm2.currentmana)+'/'+str(sta.pm2.mana),True,black)
            manabar = p.draw.rect(s.ds, (0,0,139), p.Rect(0, 210, 100, 15)),p.draw.rect(s.ds, (173,216,230), p.Rect(0, 210, pm2mana, 15))
            s.ds.blit(pm2bar,(5,213))
          
        slo1 = text.font2.render(str(sta.spell[In.eqspells[0]]),True,black)
        slo1R = slo1.get_rect()
        slo1R.topleft = (10, 230)
        slo2 = text.font2.render(str(sta.spell[In.eqspells[1]]),True,black)
        slo2R = slo2.get_rect()
        slo2R.topleft = (10, 255)
        slo3 = text.font2.render(str(sta.spell[In.eqspells[2]]),True,black)
        slo3R = slo3.get_rect()
        slo3R.topleft = (250, 230)
        slo4 = text.font2.render(str(sta.spell[In.eqspells[3]]),True,black)
        slo4R = slo4.get_rect()
        slo4R.topleft = (250, 255)
        s.ds.blit(slo1, slo1R)
        s.ds.blit(slo2, slo2R)
        s.ds.blit(slo3, slo3R)
        s.ds.blit(slo4, slo4R)
    if battleselec == 1 and battleonce == 0:
        text.colora = (100, 100, 100)
        text.colord = (255, 255, 255)
        text.colorm = (255, 255, 255)
        text.colorp = (255, 255, 255)
    elif battleselec == 2 and battleonce == 0:
        text.colora = (255, 255, 255)
        text.colord = (100, 100, 100)
        text.colorm = (255, 255, 255)
        text.colorp = (255, 255, 255)
    elif battleselec == 3 and battleonce == 0:
        text.colora = (255, 255, 255)
        text.colord = (255, 255, 255)
        text.colorm = (100, 100, 100)
        text.colorp = (255, 255, 255)
    elif battleselec == 4 and battleonce == 0:
        text.colora = (255, 255, 255)
        text.colord = (255, 255, 255)
        text.colorm = (255, 255, 255)
        text.colorp = (100, 100, 100)
    elif battleselec == 0:
        text.colora = (255, 255, 255)
        text.colord = (255, 255, 255)
        text.colorm = (255, 255, 255)
        text.colorp = (255, 255, 255)
    s.screen.blit(s.ds, (0, 0))
    p.display.flip()


enemy1health = 0
enemy2health = 0
enemy3health = 0
enemy1maxhealth = 0
enemy2maxhealth = 0
enemy3maxhealth = 0

c11 = 0
c12 = 0
c13 = 0
oncet4 = 0
oncet5 = 0
oncet6 = 0


def battlesequence():
    global yes, pbw, pbh, pbx, pby, ebw, ebh, ebx, eby, de, at, clock, save, attacktest, enemy1health, enemy2health, enemy3health, enemy1maxhealth, enemy2maxhealth, enemy3maxhealth, c11, c12, c13, turns, currentturn, oncet4, oncet5, oncet6, pm1hp, pm2hp, selecy, selecx, oncet1, oncet2, oncet3, minselecy, maxselecy, updown, pmattacking, eminselecx, emaxselecx, eselecy, eselecx, leftright, selectenem, testing, battleselec
    clock.tick(60)
    if yes == 0:
        save = im.g5
        im.g5 = im.battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
        sta.mc.hasattacked = False
        sta.pm1.hasattacked = False
        sta.pm2.hasattacked = False
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
        sta.mc.currentmana = sta.mc.mana
        currentturn = 1
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
        if currentturn == sta.partyamount + 1:
            if oncet4 == 0 and not enemieshp[0] <= 0:
                enemyattack1()
                currentturn += 1
                oncet4 = 1
            elif enemieshp[0] <= 0 and oncet4 == 0:
                currentturn += 1
                oncet4 = 1
        if sta.enemammount >= 2:
            if currentturn == sta.partyamount + 2:
                if oncet5 == 0 and not enemieshp[1] <= 0:
                    enemyattack2()
                    currentturn += 1
                    oncet5 = 1
                elif enemieshp[1] <= 0 and oncet5 == 0:
                    currentturn += 1
                    oncet5 = 1
        if sta.enemammount == 3:
            if currentturn == sta.partyamount + 3:
                if oncet6 == 0 and not enemieshp[2] <= 0:
                    enemyattack3()
                    currentturn += 1
                    oncet6 = 1
                elif enemieshp[2] <= 0 and oncet6 == 0:
                    currentturn += 1
                    oncet6 = 1
    if currentturn > turns:
        currentturn = 1
        sta.mc.hasattacked = False
        sta.pm1.hasattacked = False
        sta.pm2.hasattacked = False
    if enemieshp[0] <= 0 and c11 == 0:
        Xp.gainedxp(sta.hmmm)
        while Xp.xpgained > 0:
            clock.tick(20)
            Xp.levelcalc()
            battledraw()
        c11 = 1
    if sta.enemammount >= 2:
        if enemieshp[1] <= 0 and c12 == 0:
            Xp.gainedxp(sta.hmmm2)
            while Xp.xpgained > 0:
                clock.tick(20)
                Xp.levelcalc()
                battledraw()
            c12 = 1
    if sta.enemammount == 3:
        if enemieshp[2] <= 0 and c13 == 0:
            Xp.gainedxp(sta.hmmm3)
            while Xp.xpgained > 0:
                clock.tick(20)
                Xp.levelcalc()
                battledraw()
            c13 = 1
    if selectorover == 1:
        selecx = 110
        minselecy = 30
        maxselecy = 50
        if oncet1 == 0:
            selecy = 30
            updown = 1
            pmattacking = 1
            selectanim(1)
            oncet1 = 1
    if sta.partyamount >= 2:
        if selectorover == 2:
            selecx = 160
            minselecy = 70
            maxselecy = 90
            if oncet2 == 0:
                selecy = 70
                updown = 1
                pmattacking = 2
                selectanim(2)
                oncet2 = 1
    if sta.partyamount == 3:
        if selectorover == 3:
            selecx = 30
            minselecy = 40
            maxselecy = 60
            if oncet3 == 0:
                selecy = 40
                updown = 1
                pmattacking = 3
                selectanim(3)
                oncet3 = 1
    if selectorover == 1:
        testing = sta.mc.hasattacked
    elif selectorover == 2:
        testing = sta.pm1.hasattacked
    elif selectorover == 3:
        testing = sta.pm2.hasattacked
    if enemieshp[0] <= 0:
        if enemieshp[1] <= 0 or sta.enemammount < 2:
            if enemieshp[2] <= 0 or sta.enemammount < 3:
                c11 = 0
                c12 = 0
                c13 = 0
                im.g5 = save
                sta.S = 0
                yes = 0


def Defend():
    global defend, de, onceanim, selectorover, currentturn, battleselec
    if selectorover == 1:
        sta.dmc.hasattacked = sta.mc.hasattacked
    elif selectorover == 2:
        sta.dmc.hasattacked = sta.pm1.hasattacked
    elif selectorover == 3:
        sta.dmc.hasattacked = sta.pm2.hasattacked
    if mouseover(text.textRect8) and not sta.dmc.hasattacked:
        if selectorover == 1:
            sta.mc.defend = True
            sta.mc.hasattacked = True
        elif selectorover == 2:
            sta.pm1.defend = True
            sta.pm1.hasattacked = True
        elif selectorover == 3:
            sta.pm2.defend = True
            sta.pm2.hasattacked = True
        currentturn += 1


testing = False
attacktest = False


def attackcheck():
    global attacktest, selectorover, testing, magictest
    if mouseover(text.textRect7) and not testing:
        attacktest = True
    if mouseover(text.textRect9) and not testing:
        magictest = True


def playerattack():
    global pbw, pbh, pbx, pby, de, at, save, yes, enemyattacking, enemy1health, enemy2health, enemy3health, currentturn
    if enemyattacking == 1:
        sta.enem.Hp = enemy1health
        _x = 11
        _y = 5
    elif enemyattacking == 2:
        sta.enem.Hp = enemy2health
        _x = 14
        _y = 5.5
    elif enemyattacking == 3:
        sta.enem.Hp = enemy3health
        _x = 9
        _y = 5.5
    while at <= 21:
        clock.tick(60)
        at += 1
        pbx += _x
        pby -= _y
        pbh -= 4
        pbw -= 4
        battledraw()
    damage(sta.enem, sta.mc)
    if enemyattacking == 1:
        enemy1health = sta.enem.Hp
    elif enemyattacking == 2:
        enemy2health = sta.enem.Hp
    elif enemyattacking == 3:
        enemy3health = sta.enem.Hp
    battledraw()
    while at >= 1:
        clock.tick(60)
        at -= 1
        pbx -= _x
        pby += _y
        pbh += 4
        pbw += 4
        battledraw()
    sta.mc.hasattacked = True
    currentturn += 1


def p1attack():
    global pm1w, pm1h, pm1x, pm1y, de, at, save, yes, enemyattacking, enemy1health, enemy2health, enemy3health, currentturn
    if enemyattacking == 1:
        sta.enem.Hp = enemy1health
        _x = 9
        _y = 5.5
    elif enemyattacking == 2:
        sta.enem.Hp = enemy2health
        _x = 12
        _y = 6
    elif enemyattacking == 3:
        sta.enem.Hp = enemy3health
        _x = 7
        _y = 6
    while at <= 21:
        clock.tick(60)
        at += 1
        pm1x += _x
        pm1y -= _y
        pm1h -= 4
        pm1w -= 4
        battledraw()
    damage(sta.enem, sta.mc)
    if enemyattacking == 1:
        enemy1health = sta.enem.Hp
    elif enemyattacking == 2:
        enemy2health = sta.enem.Hp
    elif enemyattacking == 3:
        enemy3health = sta.enem.Hp
    battledraw()
    while at >= 1:
        clock.tick(60)
        at -= 1
        pm1x -= _x
        pm1y += _y
        pm1h += 4
        pm1w += 4
        battledraw()
    sta.pm1.hasattacked = True
    currentturn += 1


def p2attack():
    global pm2w, pm2h, pm2x, pm2y, de, at, save, yes, enemyattacking, enemy1health, enemy2health, enemy3health, currentturn
    if enemyattacking == 1:
        sta.enem.Hp = enemy1health
        _x = 15
        _y = 5
    elif enemyattacking == 2:
        sta.enem.Hp = enemy2health
        _x = 18
        _y = 5.5
    elif enemyattacking == 3:
        sta.enem.Hp = enemy3health
        _x = 13
        _y = 5.5
    while at <= 21:
        clock.tick(60)
        at += 1
        pm2x += _x
        pm2y -= _y
        pm2h -= 4
        pm2w -= 4
        battledraw()
    damage(sta.enem, sta.mc)
    if enemyattacking == 1:
        enemy1health = sta.enem.Hp
    elif enemyattacking == 2:
        enemy2health = sta.enem.Hp
    elif enemyattacking == 3:
        enemy3health = sta.enem.Hp
    battledraw()
    while at >= 1:
        clock.tick(60)
        at -= 1
        pm2x -= _x
        pm2y += _y
        pm2h += 4
        pm2w += 4
        battledraw()
    sta.pm2.hasattacked = True
    currentturn += 1


def enemyattack1():
    global at, ebx, eby, ebh, ebw, de, save
    pmattacking = random.randrange(1, sta.partyamount + 1)
    if pmattacking == 1:
        _x = 11
        _y = 5
        sta.dmc.Hp = sta.mc.Hp
        sta.dmc.defense = sta.mc.defense
        sta.dmc.defend = sta.mc.defend
    elif pmattacking == 2:
        _x = 9
        _y = 5.5
        sta.dmc.Hp = sta.pm1.Hp
        sta.dmc.defense = sta.pm1.defense
        sta.dmc.defend = sta.pm1.defend
    elif pmattacking == 3:
        _x = 14
        _y = 5.5
        sta.dmc.Hp = sta.pm2.Hp
        sta.dmc.defense = sta.pm2.defense
        sta.dmc.defend = sta.pm2.defend
    while at <= 21:
        clock.tick(60)
        at += 1
        ebx -= _x
        eby += _y
        ebh += 2
        ebw += 2
        battledraw()
    damage(sta.dmc, sta.enem)
    battledraw()
    if pmattacking == 1:
        sta.mc.Hp = sta.dmc.Hp
    elif pmattacking == 2:
        sta.pm1.Hp = sta.dmc.Hp
    elif pmattacking == 3:
        sta.pm2.Hp = sta.dmc.Hp
    while at >= 1:
        clock.tick(60)
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
    pmattacking = random.randrange(1, sta.partyamount + 1)
    if pmattacking == 1:
        _x = 10
        _y = 5
        sta.dmc.Hp = sta.mc.Hp
        sta.dmc.defense = sta.mc.defense
        sta.dmc.defend = sta.mc.defend
    elif pmattacking == 2:
        _x = 7
        _y = 5.5
        sta.dmc.Hp = sta.pm1.Hp
        sta.dmc.defense = sta.pm1.defense
        sta.dmc.defend = sta.pm1.defend
    elif pmattacking == 3:
        _x = 12
        _y = 5.5
        sta.dmc.Hp = sta.pm2.Hp
        sta.dmc.defense = sta.pm2.defense
        sta.dmc.defend = sta.pm2.defend
    while at <= 21:
        clock.tick(60)
        at += 1
        e2bx -= _x
        e2by += _y
        e2bh += 2
        e2bw += 2
        battledraw()
    damage(sta.dmc, sta.enem)
    battledraw()
    if pmattacking == 1:
        sta.mc.Hp = sta.dmc.Hp
    elif pmattacking == 2:
        sta.pm1.Hp = sta.dmc.Hp
    elif pmattacking == 3:
        sta.pm2.Hp = sta.dmc.Hp
    while at >= 1:
        clock.tick(60)
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
    pmattacking = random.randrange(1, sta.partyamount + 1)
    if pmattacking == 1:
        _x = 9
        _y = 5
        sta.dmc.Hp = sta.mc.Hp
        sta.dmc.defense = sta.mc.defense
        sta.dmc.defend = sta.mc.defend
    elif pmattacking == 2:
        _x = 6
        _y = 5.5
        sta.dmc.Hp = sta.pm1.Hp
        sta.dmc.defense = sta.pm1.defense
        sta.dmc.defend = sta.pm1.defend
    elif pmattacking == 3:
        _x = 11
        _y = 5.5
        sta.dmc.Hp = sta.pm2.Hp
        sta.dmc.defense = sta.pm2.defense
        sta.dmc.defend = sta.pm2.defend
    while at <= 21:
        clock.tick(60)
        at += 1
        e3bx -= _x
        e3by += _y
        e3bh += 2
        e3bw += 2
        battledraw()
    damage(sta.dmc, sta.enem)
    battledraw()
    if pmattacking == 1:
        sta.mc.Hp = sta.dmc.Hp
    elif pmattacking == 2:
        sta.pm1.Hp = sta.dmc.Hp
    elif pmattacking == 3:
        sta.pm2.Hp = sta.dmc.Hp
    while at >= 1:
        clock.tick(60)
        at -= 1
        e3bx += _x
        e3by -= _y
        e3bh -= 2
        e3bw -= 2
        battledraw()
    if sta.mc.Hp <= 0:
        sta.S = None
def splashspell(spell):
    pass
