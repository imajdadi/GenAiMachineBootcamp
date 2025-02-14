#Créez une classe appelée Farm
class Farm :
    def __init__(self, animal_name):#La Farmclasse a-t-elle besoin d'une __init__méthode ? Si oui, 
        self.name = animal_name # quels paramètres doit-elle accepter ? 
        self.animals = {}
    def add_animal(self, animal, animal_number =1):#Combien de méthodes la Farmclasse a-t-elle besoin
        if animal in self.animals:
            self.animals[animal] += animal_number
        else:
            self.animals[animal] = animal_number

    def info_animals(self):
        total = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            total += f"{animal} : {count}\n"
        total += "\n    E-I-E-I-0!"
        return total
    def get_animal_types(self):#méthode à la Farmclasse appelée get_short_info
        return sorted(self.animals.keys()) 

    def get_short_info(self):#méthode doit appeler la get_animal_typesfonction 
        animal_list = ', '.join(self.get_animal_types())
        return (f"La ferme {self.name} possède {animal_list}")
    #pour le s ntlk module


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.info_animals())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
