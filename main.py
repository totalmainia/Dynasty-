import pygame as p

p.font.init()
ds = p.display.set_mode((500, 300))  # create display
white = (255, 255, 255)
x = 0
y = 0
pressed = p.key.get_pressed()
value = 0
tryhard = 0
black = (0, 0, 0)
P = 0
S = 0
wi = 87
T = 1
L=50
Eq = ["Armor", "Weapon", "Potion"]
Inv = [
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
]

color = black
clock = p.time.Clock()
# idle and animations for main charecter
Di = p.image.load('I/downi.png')
Da = [p.image.load('I/down2.png'), p.image.load('I/down3.png')]
Ui = p.image.load('I/upi.png')
Ua = [p.image.load('I/up2.png'), p.image.load('I/up3.png')]
Li = p.image.load('I/lefti.png')
La = [
    p.image.load('I/left2.png'),
    p.image.load('I/lefti.png'),
    p.image.load('I/left3.png')
]
Ri = p.image.load('I/righti.png')
Ra = [
    p.image.load('I/right2.png'),
    p.image.load('I/righti.png'),
    p.image.load('I/right3.png')
]
g5 = Di
P1 = p.transform.scale(g5, (wi, 100))


# make charecter
class Player(object):
    def __init__(self):
        super().__init__()
        self.image = (P1)
        self.x = 209
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.center = (250, 150)


mc = Player()
drawGrid = False


def drawG():
    blockSize = 50  #Set the size of the grid block
    for x in range(0, 500, blockSize):
        for y in range(0, 300, blockSize):
            rect = p.Rect(x, y, blockSize, blockSize)
            p.draw.rect(ds, black, rect, 1)


font = p.font.Font('freesansbold.ttf', 32)
font2 = p.font.Font('freesansbold.ttf', 20)
text = font.render('Pause', True, color, white)
text2 = font2.render('Party (press 1)', True, color, white)
text3 = font2.render('Settings (press 2)', True, color, white)
text4 = font2.render('Back (press esc)', True, color, white)
text5 = font.render('There Are No Settings', True, color, white)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect.center = (250, 50)
textRect2.center = (250, 75)
textRect3.center = (250, 100)
textRect4.center = (250, 125)
textRect5.center = (250, 75)
r = True
# when the game is active
while r:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.KEYUP:
            if event.key == p.K_e:
                if S == 0:
                    S = 1
                    event.key = p.K_p
                elif event.key == p.K_e:
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
                elif S == 3:
                    S = 2
                    event.key = p.K_p
            elif event.key == p.K_2:
                if S == 2:
                    S = 3
                    event.key = p.K_p
            if event.key == p.K_EQUALS:
                if drawGrid == False:
                    drawGrid = True
                    event.key = p.K_p
                else:
                    drawGrid = False
    rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
    #overworld
    if S == 0:
        ds.fill(white)
        ds.blit(mc.image, (mc.x, mc.y))
        rect1 = p.draw.rect(ds, color, p.Rect(x, y, 500, 50))
        P1 = p.transform.scale(g5, (wi, 100))
        mc.image = P1
        if drawGrid:
            drawG()
        if value >= len(Ua):
            value = 0
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
#movement for the player
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                g5 = La[value]
                x += 5
            if event.key == p.K_RIGHT:
                g5 = Ra[value]
                x -= 5
            if event.key == p.K_UP:
                g5 = Ua[value]
                y += 5
            if event.key == p.K_DOWN:
                g5 = Da[value]
                y -= 5
                T = 4.5

        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                g5 = Li
            if event.key == p.K_RIGHT:
                g5 = Ri
            if event.key == p.K_UP:
                g5 = Ui
            if event.key == p.K_DOWN:
                g5 = Di
#inventory screen
    elif S == 1:
        ds.fill(color)
        #Create inventory slots
        InvSlot1 = p.draw.rect(ds,white,p.Rect(25, 25, L,L))
        InvSlot2 = p.draw.rect(ds,white,p.Rect(75, 25,L,L))
        InvSlot3 = p.draw.rect(ds,white,p.Rect(150, 25,L,L))
        InvSlot4 = p.draw.rect(ds,white,p.Rect(200, 25,L,L))
        InvSlot5 = p.draw.rect(ds,white,p.Rect(250, 25,L,L))
        InvSlot6 = p.draw.rect(ds,white,p.Rect(50, 75,L,L))
        InvSlot7 = p.draw.rect(ds,white,p.Rect(100, 75,L,L))
        InvSlot8 = p.draw.rect(ds,white,p.Rect(150, 75,L,L))
        InvSlot9 = p.draw.rect(ds,white,p.Rect(200, 75,L,L))
        InvSlot10 = p.draw.rect(ds,white,p.Rect(250, 75,L,L))
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

    collideU = rect1.collidepoint(mc.rect.topleft) or rect1.collidepoint(
        mc.rect.topright) or rect1.collidepoint(mc.rect.midtop)
    collideD = rect1.collidepoint(mc.rect.midbottom) or rect1.collidepoint(
        mc.rect.bottomleft) or rect1.collidepoint(mc.rect.bottomright)
    collideR = rect1.collidepoint(mc.rect.midright) or rect1.collidepoint(
        mc.rect.topright) or rect1.collidepoint(mc.rect.bottomright)
    collideL = rect1.collidepoint(mc.rect.midleft) or rect1.collidepoint(
        mc.rect.topleft) or rect1.collidepoint(mc.rect.bottomleft)
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
    if tryhard == 10:
        value += 1
        tryhard = 0
