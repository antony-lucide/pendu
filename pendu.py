import pygame as py
from sys import exit
import random
import  sys



#Cette fonction permet de lire le fichier des mots pré-enregistrer pour le pendu.
#Ensuite je retourne une valeur aléatoire pour pouvoir choisir au hasard un mot dans mon pendu.
def mot(difficulte):
    f = open("mot" + str(difficulte) + ".txt")
    résultat = f.read().splitlines() 
    f.close()
    return random.choice(résultat)

#Je créer une variable avec la fonction mot à l'interieur afin de pouvoir la réutiliser dans une autres fonctions.
total = mot(1)

#Cette fonction permet de stocker les noms des string dans mon dossier txt.
#Et les ajouters dans ma variable "Variable" pour l'appeller ailleurs.
def string (phrase):
    variable = ''
    for name  in phrase:
        if name.lower() in liste_de_lettre:
            variable += name
        else:
            variable += " _ "
    return(variable)

#Cette variable permet de stocker le nombre d'erreur faite par l'utilisateur.
défaite = 0

#Cette fonction a pour objectif de vérifier si la lettre choisis est la même dans le mot sélectionner.
#Paramètre désigne la lettre, la section désigne les mots.
def lettre (paramètre,section):
    global liste_de_lettre,défaite
    if paramètre in section.lower() and paramètre not in liste_de_lettre:
        liste_de_lettre += [paramètre]
    if paramètre not in section.lower() and paramètre not in liste_de_lettre:
        défaite += 1
    
#Une fonction pour vérifier si l'utilisateur a gagner la partie.
def victorie():
    for i in total:
        if i.lower() not in liste_de_lettre:
            return False
    return(True)

#Une fonction pour recharger la partie avec un autres mots aléatoire.
def reload():
        global liste_de_lettre,total,défaite
        liste_de_lettre = []
        total = mot(difficulte)
        défaite = 0

#Cette fonction vérifie si, ils y a quelque choses à l'interieur de champs
def Menu():
    global total
    if len(champs) > 0:
        total = champs

#Fonction pour afficher le pendu
def window():
    image = interface.blit(liste_image[défaite],(0,0))    
    interface.blit(pendu,(580,200))
    interface.blit(titre,(580,100))
   
#Fonction pour afficher le menu
def opti():
    text_surface = text.render(champs,True,'red')
    entrybox_facile = text.render('Facile',True,'red')
    entrybox_normal = text.render('Normal',True,'red')
    entrybox_difficile = text.render('Difficile',True,'red')
    interface.blit(menu,(300,200))
    py.draw.rect(menu,couleur_noir,[50, 30, 80 , 40], 0)
    menu.blit(boutton,(50,30))
    py.draw.rect(menu,couleur_noir,[50, 130, 90 , 40], 0)
    menu.blit(entrybox,(30,90))
    menu.blit(text_surface,(50,130))
    interface.blit(entrybox_facile,(180,400))
    interface.blit(entrybox_normal,(300,400))
    interface.blit(entrybox_difficile,(460,400))

#Une liste pour stocker les charactère rentré par l'utilisateur.
liste_de_lettre = []

#Arborescence de l'interface.
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
loose = text.render('défaite',True,'red')
win = text.render('victoire',True,'red')
option = text.render('échape pour restart',True,False)
menu = py.image.load('img/menu.jpeg').convert()
menu = py.transform.smoothscale(menu,(200,200))
couleur_noir = (200,200,200)
boutton = text.render('Play',False,'red')
entrybox = text.render('Entrybox',False,'red')
champs = '' 
#Liste contenant les images du pendu.
liste_image = []
#Variable pour la boucle infinie
frame = True
#Permet d'afficher le menu grâce a ma valeur bool
activate = True
#Variable pour le focus de mon entrybox
focus_entrybox = False
#Permet de switcher entre diffculter une fois avoir appuyer sur le boutton
FACILE = 0
NORMAL = 1
DIFFICILE = 2
#Difficulté de base
difficulte = NORMAL
#On appellent cette diffculté en dehors afin de pouvoir l'appeler dans d'autre fonction/conditions
Menu()
#Une boucle pour vérifier les images et pouvoir les formater en fonction de leur position.
for i in range (7):
    liste_image += [py.image.load(f'img/pendu_{i}.png')]


#La boucle principale pour faire tourner l'interface pygame sans intérference.
#La boucle vérifie d'abord si l'utilisateur ferme l'interface ou non.
#KEYDOWN, c'est-a-dire n'importe quel touches appuyer.
#Si KEYDOWN est actif alors, afficher la lettre utiliser et afficher la lettre à la place de "_".
#Les cinque conditions permettent de vérifier la difficulté des mots dans la liste et pouvoir choisir celle-ci.
#la condition de fous_entrybox permet de vérifier les lettres rentrée dans celle-ci et pouvoir l'afficher dans le pendu.
#L'avant dernière condition vérifie si la touche que l'utilisateur a entrée est "KEYDOWN".
#La dernière condition permet de recharger la partie.
while frame:
    for event in py.event.get():
        souris = py.mouse.get_pos()
        if event.type == py.QUIT:
                frame = False
        if activate:
            if event.type == py.MOUSEBUTTONDOWN: 
                if py.mouse.get_pressed()[0] and 350 <= souris[0] <= 430 and 230 <= souris[1] <= 270:
                    activate = False
                    focus_entrybox = False
                    print(difficulte)
                    total = mot(difficulte)
                    Menu()
                if py.mouse.get_pressed()[0] and 350 <= souris[0] <= 430 and 330 <= souris[1] <= 370:
                    focus_entrybox = True
                if py.mouse.get_pressed()[0] and 180 <= souris[0] <= 280 and 400 <= souris[1] <= 430:
                    print("FACILE")
                    difficulte = FACILE
                if py.mouse.get_pressed()[0] and 300 <= souris[0] <= 424 and 400 <= souris[1] <= 430:
                    print("NORM")
                    difficulte = NORMAL
                if py.mouse.get_pressed()[0] and 460 <= souris[0] <= 590 and 400 <= souris[1] <= 430:
                    print("DIFFICILE")
                    difficulte = DIFFICILE
            if focus_entrybox and event.type == py.KEYDOWN:
                if py.key.name(event.key) in "abcdefghijklmnopqrstuvwxyz":
                    champs += py.key.name(event.key)
                else:
                    if event.key == py.K_RETURN:
                        focus_entrybox = False
                    elif event.key == py.K_BACKSPACE:
                        champs = champs[:-1]
                print(champs)
        else:
            if event.type == py.KEYDOWN:
                if not victorie():
                    config = py.key.name(event.key)
                    lettre(config,total)
                pendu = text.render(string(total),False,'red')
                if event.key == py.K_ESCAPE:
                    reload()
    if activate:
        # Permet d'actualiser l'interface.
        py.display.update()
        interface.blit(interface_image, (0, 0))
        opti()
    else:
        #Condition pour vérifier si la partie est gagner et afficher "Victoire".
        #Même condition pour la défaite, sauf que on vérifie le nombre d'images afficher.
        if victorie():
            interface.blit(win,(580,300))
            interface.blit(option,(160,400))
        if défaite > 5:
            interface.blit(loose,(620,400))
            interface.blit(option,(160,400))
        # Permet d'actualiser l'interface.
        py.display.update()
        interface.blit(interface_image, (0, 0))
        #Condition pour recharger la page
        if défaite > 6:
            reload() 
        window()