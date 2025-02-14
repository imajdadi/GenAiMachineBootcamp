#Exercice 2 : Les chiens
# Instructions
#Créez une classe appelée Dog
class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
#avec les attributs suivants name, age, weight.
#Implémentez les méthodes suivantes dans la Dogclasse :
    def bark (self) :#bark: renvoie une chaîne qui indique
        print(self.name + " Ouaf Ouaf")
        
    def run_speed(self) -> int:#renvoie la vitesse de course du chien (weight/age*10).
        return self.weight/self.age*10

    def fight(self, other_dog:"Dog"):#fight: prend un paramètre 

        power_self = self.run_speed() * self.weight#appelée other_dog
        power_other = other_dog.run_speed() * other_dog.weight

        if power_self > power_other:
            return f"{self.name} wins the fight!"
        elif power_self < power_other:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie! "

dog_1 = Dog("Rex", 3 , 7)
dog_2 = Dog("Husky", 1 , 9)
dog_3 = Dog("Fifou", 2, 3)  

dog_1.bark()
dog_2.bark()
dog_3.bark()
dog_1.run_speed()
dog_2.run_speed()
dog_3.run_speed()

# les combats
print(dog_1.fight(dog_2)) 
print(dog_2.fight(dog_3)) 
print(dog_1.fight(dog_3))  
    

print(f"{dog_1.name} run speed: {dog_1.run_speed():.2f} km/h")
print(f"{dog_2.name} run speed: {dog_2.run_speed():.2f} km/h")
print(f"{dog_3.name} run speed: {dog_3.run_speed():.2f} km/h")


#Créez 3 chiens et faites-les courir dans votre classe.