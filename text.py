import pygame as p
import sta
white = (255, 255, 255)
green = (0,255,0)
red = (255,0,0)
grey = (10,10,10)
black = (0,0,0)
color2 = (255,255.255)
color = black
font999 = p.font.Font('freesansbold.ttf', 50)
text999 = font999.render('YOU DIED', True, red, black)
textRect999 = text999.get_rect()
textRect999.center = (250,150)
fonthp = p.font.Font('freesansbold.ttf', 10)
textHp = fonthp.render(str(sta.mc.Hp)+'/'+str(sta.mc.maxHp), True, black)
textRectHp = textHp.get_rect()
textRectHp.center = (50,220)

font = p.font.Font('freesansbold.ttf', 32)
font2 = p.font.Font('freesansbold.ttf', 20)
font3 = p.font.Font('freesansbold.ttf', 18)
text = font.render('Pause', True, color, white)
text2 = font2.render('Party', True, color, white)
text3 = font2.render('Settings', True, color, white)
text4 = font2.render('Back', True, color, white)
text5 = font.render('There Are No Settings', True, color, white)
text6 = font2.render('Inventory full', True, color, white)
text7 = font3.render('Attack',True, white,grey)
text8 = font3.render('Defend',True, white,grey)
text9 = font3.render('Magic',True, white,grey)
text10 = font3.render('Potion',True, white,grey)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect7 = text7.get_rect()
textRect8 = text8.get_rect()
textRect9 = text9.get_rect()
textRect10 = text10.get_rect()
textRect.center = (250, 50)
textRect2.center = (250, 75)
textRect3.center = (250, 100)
textRect4.center = (250, 125)
textRect5.center = (250, 75)
textRect7.center = (360, 250)
textRect8.center = (440, 250)
textRect9.center = (360, 290)
textRect10.center = (440, 290)
savefont= p.font.Font('freesansbold.ttf', 40)
textsave1 = savefont.render('Save file 1', True, black,white)
textRectsave1 = textsave1.get_rect()
textRectsave1.center = (250,50)
textsave2 = savefont.render('Save file 2', True, black,white)
textRectsave2 = textsave2.get_rect()
textRectsave2.center = (250,120)
textsave3 = savefont.render('Save file 3', True, black,white)
textRectsave3 = textsave3.get_rect()
textRectsave3.center = (250,190)
textsave4 = savefont.render('Save file 4', True, black,white)
textRectsave4 = textsave4.get_rect()
textRectsave4.center = (250,260)
textscreen = font999.render('Dynasty', True, black,white)
textRectscreen = textscreen.get_rect()
textRectscreen.center = (250,50)
textscreen1 = font.render('Start', True, black,white)
textRectscreen1 = textscreen1.get_rect()
textRectscreen1.center = (250,100)
textscreen2 = font.render('Settings', True, black,white)
textRectscreen2 = textscreen2.get_rect()
textRectscreen2.center = (250,150)
textscreen3 = font.render('Quit', True, black,white)
textRectscreen3 = textscreen3.get_rect()
textRectscreen3.center = (250,200)
user_text = ''
Passwordtext = ''
Password = font.render(Passwordtext,True,black)
texts = font.render('password?',True,black,white)
texts2 = font.render('yes/', True, black, white)
texts3 = font.render('No', True, black, white)
textsRect = p.Rect(150,50,200,150)
texts2Rect = texts2.get_rect()
texts2Rect.center = (200,200)
texts3Rect = texts3.get_rect()
texts3Rect.center = (260,200)
texts4Rect = p.Rect(150,100,200,150)
testext= font.render(user_text, True, black)
testRect = testext.get_rect()
testRect.center = (250,250)