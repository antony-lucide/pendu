import pygame as py
from sys import exit
import random
import  sys

def mot():
    f = open('mot.txt')
    résultat = f.read().splitlines() 
    f.close()
    return random.choice(résultat)

total = mot()

def string (phrase):
    variable = ''
    for name  in phrase:
        if name.lower() in liste_de_lettre:
            variable += name
        else:
            variable += " _ "
    return(variable)


défaite = 0

def lettre (paramètre,section):
    global liste_de_lettre,défaite
    if paramètre in section.lower() and paramètre not in liste_de_lettre:
        liste_de_lettre += [paramètre]
    if paramètre not in section.lower() and paramètre not in liste_de_lettre:
        défaite += 1
    
    
def victorie():
    for i in total:
        if i.lower() not in liste_de_lettre:
            return False
    return(True)



liste_de_lettre = []

py.display.init()
py.font.init()
interface = py.display.set_mode((820,500))
description = py.display.set_caption('pendu')
frame = py.time.Clock()
text = py.font.Font(None,50)
interface_image = py.image.load('img/background.jpeg').convert()
titre = text.render('Pendu',False,'Green')
couleur_active = py.Color('dark blue')
pendu = text.render(string(total),False,'red')
liste_image = []

frame = True
for i in range (6):
    liste_image += [py.image.load(f'img/pendu_{i}.png')]
while frame:   
    for event in py.event.get():
        if event.type == py.QUIT:
            frame = False
        if event.type == py.KEYDOWN:
            config = py.key.name(event.key)
            print(config,lettre(config,total),liste_de_lettre)
            pendu = text.render(string(total),False,'red')
            if victorie():
                print("victoire")
            if défaite == 6:
                print("défaite")
            
    py.display.update()
    interface.blit(interface_image,(0,0))
    interface.blit(liste_image[défaite],(0,0))
    interface.blit(pendu,(580,200))
    interface.blit(titre,(620,100))
