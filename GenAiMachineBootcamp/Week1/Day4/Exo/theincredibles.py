from family import Family
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        # Hérite du constructeur de la classe Family
        super().__init__(last_name, members)

    def use_power(self, name):
        # Utilise le pouvoir d'un membre si ce dernier est majeur
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(f"{member['name']} uses their power to {member['power']}.")
                    return
                else:
                    raise Exception(f"{name} is not over 18 years old!")

    def incredible_presentation(self):
        # Affiche l'introduction et les détails des membres
        print("Here is our powerful family!")
        super().family_presentation()


# Créer un exemple de famille TheIncredibles
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# Créer une instance de la famille TheIncredibles
incredible_family = TheIncredibles("Incredibles", members)

# Appeler la méthode incredible_presentation pour afficher les informations
incredible_family.incredible_presentation()

# Ajouter un enfant à la famille (Baby Jack)
baby_adam = {'name': 'Adam', 'age': 2, 'gender': 'Male', 'is_child': True, 'power': 'Unknown Power', 'incredible_name': 'BabyAdam'}
incredible_family.born(**baby_adam)

# Appeler à nouveau la méthode incredible_presentation pour afficher la famille mise à jour
incredible_family.incredible_presentation()

# Essayer d'utiliser les pouvoirs d'un membre majeur
incredible_family.use_power('Michael')  # Devrait imprimer le pouvoir de Michael

# Essayer d'utiliser les pouvoirs d'un membre mineur (Jack)
try:
    incredible_family.use_power('Adam')  # Devrait lever une exception car Jack n'a pas 18 ans
except Exception as e:
    print(e)