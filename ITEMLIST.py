

def testitem():
  s=0
  ws = 0
  if s ==0:
            Stick =ds.blit(Items.image1, (x-70, y+50))
            if colI(Stick):
              if additem(Items.image1):
                s=1
  if ws ==0:
            Woodsword =ds.blit(Items.image2, (x-50, y-100))
            if colI(Woodsword):
              if additem(Items.image2):
                ws=1
  if s ==0:
            Stick =ds.blit(Items.image1, (x-70, y+50))
            if colI(Stick):
              if additem(Items.image1):
                s=1