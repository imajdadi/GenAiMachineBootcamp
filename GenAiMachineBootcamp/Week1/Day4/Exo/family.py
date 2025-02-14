class Family : 
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):#a child to the members list (use **kwargs)
        self.members.append(kwargs)
        print(f"Félicitations à la famille {self.last_name} pour la naissance de {kwargs['name']} !")

    def is_18(self,name):
        for membre in self.members:
            if membre['name'] == name:#returns True if they are over 18 and False if not.
                return membre['age'] >= 18
        return False 
    def family_presentation(self):#a method that prints the family’s 
        for membre in self.members:

            print(f"Nom: {membre['name']}, Âge: {membre['age']}, Genre: {membre['gender']}, Enfant: {'Oui' if membre['is_child'] else 'Non'}")
#Create an instance of the Family class,
membres_initiaux = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family(membres_initiaux, "Adamnou")

my_family.family_presentation()

# Ajout d'un enfant
my_family.born(name='Emmane', age=0, gender='Female', is_child=True)

# Vérification de l'âge
print(my_family.is_18('Michael'))  # True
print(my_family.is_18('Emmane'))  # False

# Affichage mis à jour de la famille
my_family.family_presentation()