import random 

mysteriousNum = random.randint(1, 50)
tentativeNum = 0
playerNum = 0
title = "Bienvenue sur le jeux du nombre mystère !"
chooseNum = "Veuillez choisir un nombre entre 1 et 50: "

print(title)
input(chooseNum)

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