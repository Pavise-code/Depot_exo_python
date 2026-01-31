#restaurant management system
import os
def presentation(): 
    print('-'*10 , "RESTAURANT- LA GROSE BOUFF!!" , '-'*10)
    print('-'*22, "MENU", '-'*22)
    print('1' , ' '*3, "Afficher le menu") 
    print('2' , ' '*3, "Ajouter un plat") 
    print('3' , ' '*3, "Supprimer un plat")
    print('4' , ' '*3, "Modifier un plat")
    print('5' , ' '*3, "Quitter le programme")

choice = 0
#option = {1:"Afficher le menu", 2:"Ajouter un plat", 3:"Supprimer un plat", 4: "Modifier un plat", 5:"Quitter le programme"}

plat = {1:"Pâte", 2:"Cerveau-bouilli", 3:"Dibi-mbot", 4:"Gresse de panthere", 5:"lake-chauve-souris" }

def verification_choice():
    choice = int(input('Que voulez-vous faire entre (1-5): '))
    while choice < 1 or choice > 5:
        choice = int(input('OUPS! Mauvaise entrer, reessayer (1-5): '))
    return choice

def menu_display():
    print(plat)

def parcours_plat():
    for key in plat.keys():
        pass
    return key

def ajout_dish():
    print('\nOK! va pour ajout de plat.')
    menu_display()
    ajout = input("\nEntrer le plat a ajouter: ")
    last_position_plat = parcours_plat()
    plat[last_position_plat + 1] = ajout
    menu_display()

def delete_dish():
    print('OK! va pour supprimer un plat.')
    menu_display()
    delete = int(input("Pour suprimer un plat, il suffit juste d'entrer son numero: "))
    last_position_plat = parcours_plat()

    while delete < 1 or delete > last_position_plat:
        delete = int(input("OUPS! suffit juste d'entrer son numero, reessayer: "))
    plat.pop(delete)
    menu_display()

def modif_dish():
    print('OK! va pour une modification d\'un plat.')
    menu_display()
    modif = int(input("Pour modifier un plat, il suffit juste d'entrer son numero: "))
    last_position_plat = parcours_plat()

    while modif < 1 or modif > last_position_plat:
        modif = int(input("OUPS! suffit juste d'entrer son numero, reessayer: "))
    new_dish = input("Entrer le nouveau plat: ")
    plat.update({modif : new_dish})
    menu_display()

presentation() #affiche seulement le menu
verification_choice() #Verifie les choix qu'on a fait dans menu
parcours_plat() #permet juste de parcourir le dictionnaire de plat
#ajout_dish() #ajoute simplement un plat a la fin du dictionnaire
delete_dish()
#modif_dish()