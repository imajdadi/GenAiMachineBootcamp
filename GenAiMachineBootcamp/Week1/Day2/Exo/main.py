#Exercice 2 : Cinemax #2
#Combien chaque membre de la famille doit-il payer ?
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for name, age in family.items():
 if age < 3 :
    print(f" votre age {age} est le billet est gratuit")
 elif 3 <age< 12 :
    print(f"votre age est :  {age} le billet est a 10$")

 else:
   print (f"votre age est : {age} le billet coute 15$")

#Imprimez le coût total des films pour la famille.
total_cout = sum(family.values())
print(f"le cout total pour toute la famille est {total_cout}$ ")

#Bonus : demandez à l'utilisateur de saisir les noms et les âges au lieu
#d'utiliser la variable familiale fournie (Astuce : demandez à l'utilisateur 
#les noms et les âges et ajoutez-les dans un dictionnaire familial initialement vide).
# Exercise 4 : Some Geography
#Write a function called describe_city() that accepts the name of a city and its country as parameters.
def describe_city(city ,country="France") : #Give the country parameter a default value.
  print(f"the city of {city} is in {country}")

#The function should print a simple sentence, such as “city is in country”.
describe_city("Paris")
describe_city("Reykjavik" , "Iceland")
describe_city("Rabat" , "Morocco")




