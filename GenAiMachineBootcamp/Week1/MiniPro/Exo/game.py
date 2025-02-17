import random

class Game:
    def __init__(self):
        self.choices = ["pierre", "papier", "ciseaux"]

    def get_user_item(self):
        #choisir pierre, papier ou ciseaux
        while True:
            user_choice = input("Choisissez pierre, papier ou ciseaux : ").lower()
            if user_choice in self.choices:
                return user_choice
            print("Entrée invalide. Veuillez choisir entre pierre, papier ou ciseaux.")

    def get_computer_item(self):
        #l'ordinateur sélectionne un choix aléatoire 
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        #Détermine le gagnant
        if user_item == computer_item:
            return "match nul"
        elif (user_item == "pierre" and computer_item == "ciseaux") or \
             (user_item == "papier" and computer_item == "pierre") or \
             (user_item == "ciseaux" and computer_item == "papier"):
            return "gagné"
        else:
            return "perdu"

    def play(self):
        #Jouer une partie et j'affiche le résultat
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"Vous avez choisi : {user_item}")
        print(f"L'ordinateur a choisi : {computer_item}")
        print(f"Résultat : {result}")

        return result
