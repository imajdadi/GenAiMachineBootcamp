import random
from dog import Dog  # Importation de la classe Dog depuis le fichier précédent

class PetDog(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together.")
    
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")

# Exemple d'utilisation :
if __name__ == "__main__":
    dog_1 = PetDog("Rex", 3, "Labrador")
    dog_2 = PetDog("Husky", 1, "Siberian Husky")
    dog_3 = PetDog("Fifou", 2, "Poodle")
    
    dog_1.train()
    dog_2.train()
    dog_3.train()
    
    dog_1.play(dog_1.name, dog_2.name, dog_3.name)
    
    dog_1.do_a_trick()
    dog_2.do_a_trick()
    dog_3.do_a_trick()
