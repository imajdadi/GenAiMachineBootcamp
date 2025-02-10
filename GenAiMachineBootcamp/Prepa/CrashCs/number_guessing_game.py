import random
random_number = random.randint(1, 100)
max_attempts = 7
count = 0  # Initialisation du compteur

#Définissez le nombre maximum de tentatives que le joueur peut avoir,(à) par exemple 7.

for attempt_Game in range(max_attempts):  
    #tilisez une for boucle pour donner au joueur un nombre limité de tentatives (7 dans ce cas).
    num_user = int(input(f"entrer un nombre essaie num {attempt_Game} :"))
    #joueur de saisir sa supposition en utilisant input().
    # Donnez votre avis sur la base de la comparaison :
    if num_user < random_number:
        print("Too low!")
    elif num_user > random_number:
        print("Too high!")
    elif num_user == random_number:
        print("félicitations ")
        break

    if attempt_Game == 6 :
        print(f"révélant le numéro {random_number} correct.")