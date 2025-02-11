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

def describe_city(city ,country="France") :
  print(f"the city of {city} is in {country}")

describe_city("Paris")
describe_city("Reykjavik" , "Iceland")
describe_city("Rabat" , "Morocco")
#Exercice 8 : Quiz Star Wars
#projet permet aux utilisateurs de répondre à un quiz pour tester
# leurs connaissances sur Star Wars

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


#Créez une fonction qui pose des questions à l'utilisateur et vérifie ses réponses.
def quiz() :
    correct_answer = 0
    incorrect_answer = 0
    user_response = ""
    for answer in data :
        user_response = input(print(f"{answer["question"]}"))
        if user_response == answer["answer"]:
            correct_answer = correct_answer+1
        else :
            incorrect_answer = incorrect_answer +1

    print(f"le nombre de reponses correct est : {correct_answer} / le nombre de reponses incorrect est : {incorrect_answer} ")

quiz()
#  Suivez le nombre de réponses correctes et incorrectes. Créez une liste de réponses incorrectes
#Créer une fonction qui informe l'utilisateur de son nombre de réponses correctes/incorrectes.
#Bonus :affiche à l'utilisateur les questions auxquelles il a mal répondu, sa réponse et la bonne réponse.
# S'il a eu plus de 3 mauvaises réponses, demandez-lui de rejouer.



