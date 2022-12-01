import pygame as p
import random
import sta
gxp=0
xpn=10
asp=1
tsp=1
Class=1
pm1gxp=0
pm1xpn=10
pm2gxp=0
pm2xpn=10
xpgained = 0
pam = 0
pdm = 0
phm = 0
pmm = 0
p1am = 0
p1dm = 0
p1hm = 0
p1mm = 0
p2am = 0
p2dm = 0
p2hm = 0
p2mm = 0
def levelcalc():
  global level,gxp,xpn,asp,tsp,pm1gxp,pm2gxp,pm1xpn,pm2xpn,xpgained,pam,pdm,phm,pmm,p1am,p1dm,p1hm,p1mm,p2am,p2dm,p2hm,p2mm
  gxp += 1
  if sta.partyamount >= 2:
    pm1gxp+= 1
  if sta.partyamount == 3:
    pm2gxp+= 1
  xpgained -=1
  if gxp >= xpn:
      sta.mc.level +=1
      gxp = 0
      xpn *= 1.5
      if not pam == 0:
        sta.mcstats[0]+=(random.randrange(1,pdm+1))
      if not pdm == 0:
        sta.mcstats[1]+=(random.randrange(1,pam+1))
      if not phm == 0:
        health=sta.mcstats[2]+(random.randrange(1,phm+1))
        sta.mc.Hp += health-sta.mcstats[2]
        sta.mcstats[2]=health
        sta.mc.maxHp=health
      if not pmm == 0:
        sta.mcstats[3] += (random.randrange(1,pmm+1))
  if pm1gxp >= pm1xpn:
      sta.pm1.level +=1
      pm1gxp = 0
      pm1xpn *= 1.5
      if not p1am == 0:
        sta.pm1stats[0]+=(random.randrange(1,p1dm+1))
      if not p1dm == 0:
        sta.pm1stats[1]+=(random.randrange(1,p1am+1))
      if not p1hm == 0:
        health=sta.pm1stats[2]+(random.randrange(1,p1hm+1))
        sta.pm1.Hp += health-sta.pm1stats[2]
        sta.pm1stats[2]=health
        sta.pm1.maxHp=health
      if not p1mm == 0:
        sta.pm1stats[3] += (random.randrange(1,p1mm+1))
  if pm2gxp >= pm2xpn:
      sta.pm2.level +=1
      pm2gxp = 0
      pm2xpn *= 1.5
      if not p2am == 0:
        sta.pm2stats[0]+=(random.randrange(1,p2dm+1))
      if not p2dm == 0:
        sta.pm2stats[1]+=(random.randrange(1,p2am+1))
      if not p2hm == 0:
        health=sta.pm2stats[2]+(random.randrange(1,p2hm+1))
        sta.pm2.Hp += health-sta.pm2stats[2]
        sta.pm2stats[2]=health
        sta.pm2.maxHp=health
      if not p2mm == 0:
        sta.pm2stats[3] += (random.randrange(1,p2mm+1))
    
def gainedxp(enemy):
  global xpgained
  max= sta.Enemystats[enemy][0]+ sta.Enemystats[enemy][1]+ sta.Enemystats[enemy][2]
  if max<6:
    min =1
  elif 6<=max<=30:
    min = max-5
  else:
    min = max-15
  print(min,max)
  xpgained=random.randrange(min,max)