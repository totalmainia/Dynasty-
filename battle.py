import pygame as p
import sta
import im
import In
import Xp
import text
import random
import s

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (10, 10, 10)
black = (0, 0, 0)
color2 = (255, 255.255)
color = black
clock = p.time.Clock()
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
    dam = wht.attack + (random.randrange(1, 3)) - wih.defense
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
    global textHp, pbx, pby, pbh, pbw
    textHp = text.fonthp.render(
        str(sta.mc.Hp) + '/' + str(sta.mc.maxHp), True, black)
    im.P1 = p.transform.scale(im.g5, (pbw, pbh))
    playerhp = (sta.mc.Hp / sta.mc.maxHp) * 100
    enemhp = (sta.enem.Hp / sta.enem.maxHp) * 100
    s.ds.fill(white)
    enemy1hpbar = p.draw.rect(s.ds, red,
                              p.Rect(350, 10, 100, 15)), p.draw.rect(
                                  s.ds, green, p.Rect(350, 10, enemhp, 15))
    playerhpbar = p.draw.rect(s.ds, red, p.Rect(0, 215, 100, 10)), p.draw.rect(
        s.ds, green, p.Rect(0, 215, playerhp, 10))
    eh = p.transform.scale(sta.enem.image, (ebw, ebh))
    s.ds.blit(eh, (ebx, eby))
    s.ds.blit(im.P1, (pbx, pby))
    p.draw.rect(s.ds, grey, p.Rect(0, 225, 500, 90))
    s.ds.blit(textHp, text.textRectHp)
    playerxp = 100 - ((Xp.gxp / Xp.xpn) * 100)
    playerxpbar = p.draw.rect(s.ds, (0, 101, 255),
                              p.Rect(375, 215, 100, 10)), p.draw.rect(
                                  s.ds, (135, 206, 250),
                                  p.Rect(375, 215, 100 - (playerxp + 1), 10))
    s.ds.blit(textHp, text.textRectHp)
    s.ds.blit(text.text7, text.textRect7)
    s.ds.blit(text.text8, text.textRect8)
    s.ds.blit(text.text9, text.textRect9)
    s.ds.blit(text.text10, text.textRect10)
    s.screen.blit(s.ds, (0, 0))
    p.display.flip()


def battlesequence():
    global yes, pbw, pbh, pbx, pby, ebw, ebh, ebx, eby, de, at, clock, save
    if yes == 0:
        save = im.g5
        im.g5 = im.battleP1
        #[defense,attack,maxhp,mana,luck,itemsheld,maxitemsheld]
        sta.enem.defense = sta.Enemystats[sta.enem.image][0]
        sta.enem.attack = sta.Enemystats[sta.enem.image][1]
        sta.enem.maxHp = sta.Enemystats[sta.enem.image][2]
        sta.enem.Hp = sta.Enemystats[sta.enem.image][3]
        sta.enem.mana = sta.Enemystats[sta.enem.image][4]
        yes = 1
    battledraw()
    if sta.enem.Hp <= 0:
        im.g5 = save
        save = None
        Xp.gainedxp(sta.hmmm)
        sta.S = 0
        yes = 0


def Defend():
    global defend, de
    if mouseover(text.textRect8) and de == 0:
        defend = True
        enemyattack()
        de = 1


def attack():
    global pbw, pbh, pbx, pby, de, at, save, yes
    if mouseover(text.textRect7):
        #im.blink(im.P,(255,255,255),20)  
        if de == 0:
            while at <= 21:
                clock.tick(60)
                at += 1
                pbx += 11
                pby -= 5
                pbh -= 4
                pbw -= 4
                battledraw()
            damage(sta.enem, sta.mc)
            battledraw()
            while at >= 1:
                clock.tick(60)
                at -= 1
                pbx -= 11
                pby += 5
                pbh += 4
                pbw += 4
                battledraw()
            if sta.enem.Hp <= 0:
                testdeath = 1
                im.g5 = save
                save = None
                Xp.gainedxp(sta.hmmm)
                sta.S = 0
                yes = 0
            de = 1
    elif not mouseover(text.textRect7):
        de=0


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
