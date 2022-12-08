import pygame as p
import random
import sta
import In
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
pStr = 0
pDex = 0
pCon = 0
pInt = 0
p1Str = 0
p1Dex = 0
p1Con = 0
p1Int = 0
p2Str = 0
p2Dex = 0
p2Con = 0
p2Int = 0
plevelgap = 6
pstatpoints = 2
p1levelgap = 6
p1statpoints = 2
p2levelgap = 6
p2statpoints = 2
def levelcalc():
  global level,gxp,xpn,asp,tsp,pm1gxp,pm2gxp,pm1xpn,pm2xpn,xpgained,pam,pdm,phm,pmm,p1am,p1dm,p1hm,p1mm,p2am,p2dm,p2hm,p2mm,plevelgap,pstatpoints,p1levelgap,p1statpoints,p2levelgap,p2statpoints
  gxp += 1
  if sta.partyamount >= 2:
    pm1gxp+= 1
  if sta.partyamount == 3:
    pm2gxp+= 1
  xpgained -=1
  if gxp >= xpn:
      sta.mc.level +=1
      plevelgap-=1
      if plevelgap == 0:
        pstatpoints+=(random.randrange(1,3))
        plevelgap = 6
      gxp = 0
      xpn = ((sta.mc.level/0.3)**2)
      if not pdm == 0:
        sta.mcstats[0]+=(random.randrange(1,pdm+1)) + int(((pDex-10)/2))
      if not pam == 0:
        sta.mcstats[1]+=(random.randrange(1,pam+1)) + int(((pStr-10)/2))
      if not phm == 0:
        health=sta.mcstats[2]+(random.randrange(1,phm+1)) + int(((pCon-10)/2))
        sta.mc.Hp += health-sta.mcstats[2]
        sta.mcstats[2]=health
        sta.mc.maxHp=health
      if not pmm == 0:
        sta.mcstats[3] += (random.randrange(1,pmm+1)) + int(((pInt-10)/2))
  if pm1gxp >= pm1xpn:
      sta.pm1.level +=1
      p1levelgap-=1
      if p1levelgap == 0:
        p1statpoints+=(random.randrange(1,3))
        p1levelgap = 6
      pm1gxp = 0
      pm1xpn = ((sta.pm1.level/0.3)**2)
      if not p1am == 0:
        sta.pm1stats[1]+=(random.randrange(1,p1am+1)) + int(((p1Str-10)/2))
      if not p1dm == 0:
        sta.pm1stats[0]+=(random.randrange(1,p1dm+1)) + int(((p1Dex-10)/2))
      if not p1hm == 0:
        health=sta.pm1stats[2]+(random.randrange(1,p1hm+1)) + int(((p1Con-10)/2))
        sta.pm1.Hp += health-sta.pm1stats[2]
        sta.pm1stats[2]=health
        sta.pm1.maxHp=health
      if not p1mm == 0:
        sta.pm1stats[3] += (random.randrange(1,p1mm+1)) + int(((p1Int-10)/2))
  if pm2gxp >= pm2xpn:
      sta.pm2.level +=1
      p2levelgap-=1
      if p2levelgap == 0:
        p2statpoints+=(random.randrange(1,3))
        p2levelgap = 6
      pm2gxp = 0
      pm2xpn = ((sta.pm2.level/0.3)**2)
      if not p2am == 0:
        sta.pm2stats[1]+=(random.randrange(1,p2am+1)) + int(((p2Str-10)/2))
      if not p2dm == 0:
        sta.pm2stats[0]+=(random.randrange(1,p2dm+1)) + int(((p2Dex-10)/2))
      if not p2hm == 0:
        health=sta.pm2stats[2]+(random.randrange(1,p2hm+1)) + int(((p2Con-10)/2))
        sta.pm2.Hp += health-sta.pm2stats[2]
        sta.pm2stats[2]=health
        sta.pm2.maxHp=health
      if not p2mm == 0:
        sta.pm2stats[3] += (random.randrange(1,p2mm+1)) + int(((p2Int-10)/2))
  sta.mc.defense = sta.mcstats[0]+sta.itemstats[In.slotitemid[In.playerinv[0]]][0] +sta.itemstats[In.slotitemid[In.playerinv[1]]][0]
  sta.mc.attack = sta.mcstats[1]+sta.itemstats[In.slotitemid[In.playerinv[0]]][1] +sta.itemstats[In.slotitemid[In.playerinv[1]]][1]
  sta.mc.maxHp = sta.mcstats[2]+sta.itemstats[In.slotitemid[In.playerinv[0]]][2] +sta.itemstats[In.slotitemid[In.playerinv[1]]][2]
  sta.mc.mana = sta.mcstats[3]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
  sta.mc.luck = sta.mcstats[4]+sta.itemstats[In.slotitemid[In.playerinv[0]]][3] +sta.itemstats[In.slotitemid[In.playerinv[1]]][3]
  sta.pm1.defense = sta.pm1stats[0]+sta.itemstats[In.slotitemid[In.pm1inv[0]]][0] +sta.itemstats[In.slotitemid[In.pm1inv[1]]][0]
  sta.pm1.attack = sta.pm1stats[1]+sta.itemstats[In.slotitemid[In.pm1inv[0]]][1] +sta.itemstats[In.slotitemid[In.pm1inv[1]]][1]
  sta.pm1.maxHp = sta.pm1stats[2]+sta.itemstats[In.slotitemid[In.pm1inv[0]]][2] +sta.itemstats[In.slotitemid[In.pm1inv[1]]][2]
  sta.pm1.mana = sta.pm1stats[3]+sta.itemstats[In.slotitemid[In.pm1inv[0]]][3] +sta.itemstats[In.slotitemid[In.pm1inv[1]]][3]
  sta.pm1.luck = sta.pm1stats[4]+sta.itemstats[In.slotitemid[In.pm1inv[0]]][3] +sta.itemstats[In.slotitemid[In.pm1inv[1]]][3]
  sta.pm2.defense = sta.pm2stats[0]+sta.itemstats[In.slotitemid[In.pm2inv[0]]][0] +sta.itemstats[In.slotitemid[In.pm2inv[1]]][0]
  sta.pm2.attack = sta.pm2stats[1]+sta.itemstats[In.slotitemid[In.pm2inv[0]]][1] +sta.itemstats[In.slotitemid[In.pm2inv[1]]][1]
  sta.pm2.maxHp = sta.pm2stats[2]+sta.itemstats[In.slotitemid[In.pm2inv[0]]][2] +sta.itemstats[In.slotitemid[In.pm2inv[1]]][2]
  sta.pm2.mana = sta.pm2stats[3]+sta.itemstats[In.slotitemid[In.pm2inv[0]]][3] +sta.itemstats[In.slotitemid[In.pm2inv[1]]][3]
  sta.pm2.luck = sta.pm2stats[4]+sta.itemstats[In.slotitemid[In.pm2inv[0]]][3] +sta.itemstats[In.slotitemid[In.pm2inv[1]]][3]
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