import pygame as p
import random
import sta
level=1
gxp=0
xpn=10
asp=1
tsp=1
Class= 1
def levelcalc(xpgained):
  global level,gxp,xpn,asp,tsp
  gxp +=xpgained
  if gxp >= xpn:
    level +=1
    gxp = 0
    xpn *= 1.5
    asp+=level
    tsp+=asp
    sta.mcstats[0]+=(random.randrange(1,4))
    sta.mcstats[1]+=(random.randrange(1,4))
    health=sta.mcstats[2]+(random.randrange(1,4))
    sta.mc.Hp += health-sta.mcstats[2]
    sta.mcstats[2]=health
    sta.mc.maxHp=health
    
def gainedxp(enemy):
  max= sta.Enemystats[enemy][0]+ sta.Enemystats[enemy][1]+ sta.Enemystats[enemy][2]
  if max>6:
    min =1
  elif 6<=max<=30:
    min = max-5
  else:
    min = max-15
  x=random.randrange(min,max)
  levelcalc(x)