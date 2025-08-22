# Import du module random pour le choix du nombre mystère
import random 

# Déclaration des différentes variables 
mysteriousNum = random.randint(1, 50)
tentativeNum = 0
playerNum = 0
title = "Bienvenue sur le jeux du nombre mystère !"
chooseNum = "Veuillez choisir un nombre entre 1 et 50: "

# Lancement du jeux
print(title)
input(chooseNum)

# Boucle while pour le fonctionnement du jeux 
while playerNum != mysteriousNum:
    if mysteriousNum > playerNum:
        print("Le nombre mystère est plus grand")
        input("Taper un nouveau chiffre: ")
    if mysteriousNum < playerNum:
        print("Le nombre mystère est plus petit")
        input("Taper un nouveau chiffre: ")
        
    if playerNum == mysteriousNum: 
        print("Bien joué ! Vous avez trouvé le nombre mystère !")
        break