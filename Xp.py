import pygame as p
import random
import sta as s
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
    xpn *= 1.2*(random.randrange(1,2))
    asp+=level
    tsp+=asp
    s.mcstats[0]+=(random.randrange(1,2))
    s.mcstats[1]+=(random.randrange(1,2))
    health=s.mcstats[2]+(random.randrange(1,3))
    s.mc.Hp += health-s.mcstats[2]
    s.mcstats[2]=health
    s.mc.maxHp=health
    
def gainedxp(enemy):
  max= s.Enemystats[enemy][0]+ s.Enemystats[enemy][1]+ s.Enemystats[enemy][2]
  if max>6:
    min =1
  elif 6<=max<=30:
    min = max-5
  else:
    min = max-15
  x=random.randrange(min,max)
  levelcalc(x)