class Family:
    def __init__(self, last_name, members):
        # Initialisation de la famille avec un nom et des membres
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        # Ajoute un enfant à la famille et affiche un message de félicitations
        self.members.append(kwargs)
        print(f"Félicitations à la famille {self.last_name} pour la naissance de {kwargs['name']} !")

    def is_18(self, name):
        # Vérifie si un membre est majeur (plus de 18 ans)
        for membre in self.members:
            if membre['name'] == name:
                return membre['age'] >= 18
        return False

    def family_presentation(self):
        # Affiche les détails de chaque membre de la famille
        print(f"Voici la famille {self.last_name} :")
        for membre in self.members:
            print(f"Nom: {membre['name']}, Âge: {membre['age']}, Genre: {membre['gender']}, Enfant: {'Oui' if membre['is_child'] else 'Non'}")