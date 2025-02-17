from game import Game


def get_user_menu_choice():
    #Affiche le menu 
    print("\nMenu du jeux :")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les resultats")
    print("3. Quitter")
    
    choice = input("Votre choix : ")
    while choice not in ["1", "2", "3"]:
        print("Entrée invalide. Veuillez choisir 1, 2 ou 3.")
        choice = input("Votre choix : ")
    return choice

def print_results(results):
    #Affiche les résultats des parties jouées
    print("\nRésultats des parties jouées :")
    print(f"wins : {results['gagné']}")
    print(f"loss : {results['perdu']}")
    print(f"draw : {results['match nul']}")
    print("Merci d'avoir joué !")

def main():
    # menu des resultats
    results = {"gagné": 0, "perdu": 0, "match nul": 0}
    
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        elif choice == "3":
            print_results(results)
            break

if __name__ == "__main__":
    main()
