from Employee import Employee

class Developer(Employee):

    def __init__(self, fn, ln, age_emp, job_emp = "devloper", salary_emp = 15000):
        super().__init__(self, fn, ln, age_emp, job_emp, salary_emp)
        self.coding_skills = [] 
        #compétences de codage tous les développeurs doivent commencer avec une liste de compétences vide
    # Création des développeurs
    def add_skills (self, *skills):
        self.coding_skills.extend(skills)


dev1 = Developer("Tom", "cruize" 30)
dev2 = Developer("Angelina" , "Jolie", 23)
print(dev1.first_name)
print(dev1.full_name())

print(dev1.coding_skills)


#Créez 2 objets développeurs et affichez leur attribut
#Tom Cruiz 30 ans
#Angelina Jolie 23 ans
#Ajoutez ces méthodes à la classe
#add_skills(self, *skills) : reçoit un tuple de compétences et 
# les ajoute à la liste des compétences de codage
coding(self) : affiche une belle phrase avec tous les langages de codage que le développeur connaît
coding_with_partner(self, other_developer) : affiche une jolie phrase avec le nom des deux développeurs et leurs compétences
remplacer le get_promotion(self, promotion_amount) : qui multiplie le salaire de l'utilisateur par la promotion
Appelez toutes les méthodes, y compris celles de la classe Employee