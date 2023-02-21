import pygame as py
from sys import exit
import random
import  sys



#Cette fonction permet de lire le fichier des mots pré-enregistrer pour le pendu.
#Ensuite je retourne une valeur aléatoire pour pouvoir choisir au hasard un mot dans mon pendu.
def mot():
    f = open('mot.txt')
    résultat = f.read().splitlines() 
    f.close()
    return random.choice(résultat)

#Je créer une variable avec la fonction mot à l'interieur afin de pouvoir la réutiliser dans une autres fonctions.
total = mot()

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
        total = mot()
        défaite = 0

def Menu():
    global total
    total = input()
    print(total)


def window():
    image = interface.blit(liste_image[défaite],(0,0))    
    interface.blit(pendu,(580,200))
    interface.blit(titre,(580,100))
   

def opti():
    interface.blit(menu,(300,200))
    py.draw.rect(menu,couleur_noir,[50, 30, 80 , 40], 0)
    menu.blit(boutton,(50,30))
    py.draw.rect(menu,couleur_noir,[50, 130, 80 , 40], 0)
    menu.blit(entrybox,(30,90))

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
#Liste contenant les images du pendu.
liste_image = []
#Variable pour la boucle infinie
frame = True


Menu()
#Une boucle pour vérifier les images et pouvoir les formater en fonction de leur position.
for i in range (7):
    liste_image += [py.image.load(f'img/pendu_{i}.png')]


#La boucle principale pour faire tourner l'interface pygame sans intérference.
#La boucle vérifie d'abord si l'utilisateur ferme l'interface ou non.
#La deuxième condition vérifie si la touche que l'utilisateur a entrée est "KEYDOWN".
#KEYDOWN, c'est-a-dire n'importe quel touches appuyer.
#Si KEYDOWN est actif alors, afficher la lettre utiliser et afficher la lettre à la place de "_".
#La dernière condition permet de recharger la partie.
while frame:
    for event in py.event.get():
        if event.type == py.QUIT:
            frame = False
        if event.type == py.KEYDOWN:
            config = py.key.name(event.key)
            lettre(config,total)
            pendu = text.render(string(total),False,'red')
            if event.key == py.K_ESCAPE:
                reload()
            if event.key == py.MOUSEBUTTONDOWN:
                window()               
    #Condition pour vérifier si la partie est gagner et afficher "Victoire".
    #Même condition pour la défaite, sauf que on vérifie le nombre d'images afficher.
    if victorie():
        interface.blit(win,(580,300))
        interface.blit(option,(160,400))
    if défaite > 5:
        interface.blit(loose,(620,400))
    #Permet d'actualiser l'interface.
    py.display.update()
    interface.blit(interface_image,(0,0))
    #Condition pour recharger la page
    if défaite > 6:
        reload()
    window()
    