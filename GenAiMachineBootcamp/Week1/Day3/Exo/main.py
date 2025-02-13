#Exercice 1 : Les chats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
#Instanciez trois Cat objets en utilisant le code fourni ci-dessus.
first_cat = Cat("minou", 4)
second_cat = Cat("pacha", 9)
third_cat = Cat("pixou", 11)
#En dehors de la classe, créez une fonction qui trouve le chat le plus vieux 
def oldest_cat(cat1: Cat, cat2: Cat, cat3: Cat) -> Cat:
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    if cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    return cat3
#Imprimez la chaîne suivante : « Le chat le plus âgé est <cat_name>,     
oldest= oldest_cat(first_cat,second_cat, third_cat )  
print(f"Le plus vieux chat est {oldest.name}, âge: {oldest.age}")
#Exercise 2 : Dogs
#Create a class called Dog.
class Dog : 
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark (self) :
        print(self.name + " Ouaf Ouaf")

    def jump (self) :
        print(f"saute {self.height*2} cm de haut !")

       
davids_dog = Dog("rex", 50)
print(f"name : {davids_dog.name} height : {davids_dog.height}")

davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup" , 20)
print(f"name : {sarahs_dog.name} height : {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height >= sarahs_dog.height :
    print(f"le nom de le chien le plus grand est {davids_dog.name}")
else : 
    print(f"le chien et le plus grand est {sarahs_dog.name} ")
    

