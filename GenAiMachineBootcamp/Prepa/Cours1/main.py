
      #EXO1
first = "hello world" #"This is a comment."
print("I AM A COMPUTER!")
if 1 < 2 < 4:
    print("Math is fun")
#Affecter une variable appelée nope à une absence de valeur.
nope = None
#Utilisez l'opérateur booléen « et » du langage pour combiner la valeur « vrai » du langage avec sa valeur « faux ».
print(True and False)
#Calculer la longueur de la chaîne"What's my length?
chaine = "What's my length?"
longueur = len(chaine)
print(longueur)
#"Convertissez la chaîne "i am shouting"en majuscules.
chaine = "i am shouting"
chaine_majuscule = chaine.upper()
print(chaine_majuscule)
#Convertissez la chaîne "1000"en nombre 1000.
chaine = "1000"
nombre_int = int(chaine)
print(nombre_int)  # Affiche : 1000
#Combinez le nombre 4avec la chaîne "real"pour produire "4real"
nombre = 4
chaine = "real"
resultat = str(nombre) + chaine
print(resultat)
#Enregistrez la sortie de l'expression 3 * "cool".
expression = 3 * "cool"
print(expression)
#Enregistrez la sortie de l'expression 1 / 0.
expression_1 = "1/0"
#Déterminer le type de [].
liste = []
#Demandez à l'utilisateur son nom et stockez-le dans une variable appelée name.
name = "what is your name ?"
#name = input ("what is your name ?")
print ( f"{name}")
#Demandez à l'utilisateur un nombre.Si le nombre est négatif
number = int(input("what is your number?"))
if number < 0:
      print(f"That number {number} is less than 0")
elif number > 0:
      print(f"That number {number} is greater than 0")
else:
      print ("You picked 0!")
#Trouver l'index de "l"dans "apple"
my_string="apple"
index = my_string.find("l")
print(index)
#Vérifiez si "y"c'est dans "xylophone"
my_string_1 = "xylophone"
if "y" in my_string_1:
      print("y is in xylophone")
#Vérifiez si une chaîne appelée my_stringest entièrement en minuscules.
my_string_2 = "my_stringest"
if my_string_2.islower:
 print(f"{my_string_2} est entiérement en minuscules")
def animal_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Exemples d'utilisation
print(animal_years(10))  # [10, 56, 64]
print(animal_years(1))   # [1, 15, 15]
print(animal_years(2))   # [2, 24, 24]