print("hello word")
print("The answer is", 42)  # String and integer
print(3.14, "is a float")  # Float and string
print(True)  # Boolean (True/False)
x = 5
print(x)
num = 1 #assign it to a number
word = "YOLO" #we assign it to a string
nothing = None #we assign it to a None value (absence of value)
print(num)
print(word)
print(nothing)
name, age = 'John', 25
print(name)
print(age)
my_variable = 3 
AVOGADRO_CONSTANT = 6.022140857 * 10 ** 23  
name = "what is your name ?"
print ( f"hello {name} !")# https://en.wikipedia.org/wiki/Avogadro_constant
print(AVOGADRO_CONSTANT)
# Taking user input and storing it in the variable user_name
user_name = input("Enter your name: ")
# Displaying the input
print(user_name)
# Taking user input and storing it in the variable user_name
age = input("Enter your age: ")
# Displaying the input
print(f"i am {age} years old.")
# Declare a variable age and take user input
age = input("Enter your age: ")

# Print the user's age
print(f"You are {age} years old.")
#calcul 10 et 3
int = (10+3)
print(int)
#Soustrayez 7 de 15 en utilisant Python.
int = (7-15)
print(int)
#Multipliez 4 par 8 en utilisant Python
int = (4*8)
print(int)
#Divisez 18 par 3.
int = (18/3)
print(int)
#Utilisez la division par le sol pour trouver combien de fois 11 peuvent être divisés par 4.
int_1= 11//4
print(int_1)
#Trouvez le reste lorsque 9 est divisé par 4 en utilisant l'opérateur module.
int_value = (9%4)
print(int)
#Élevez 6 à la puissance 3.
int_value = (6**3)
print(int)
#Utilisez l’opérateur de négation pour rendre le nombre 12 négatif.
int_value = (-12)
print(int)
num = 100
print(str(num))
my_string = "Python"
print(my_string[0:4])  # Output: Pyth
new_string = "J" + my_string[1:]
print(new_string)  # Output: Jython

#this is a list of strings
users = ['Anna','John', 'Mike', 'Sarah']

#this is a list of integers
users_id = [145, 234, 677, 444]

#this is a list() built-in function
user_name = 'John Doe'
user_name_list = list(user_name)

#check what happens to the string:
print(user_name_list)

# This is a tuple of integers
coordinates = (4, 2, 1)

# This is a tuple of strings
users = ('Anna', 'John', 'Mike')

# Trying to change a tuple value will raise an error
coordinates = (10,) + coordinates[1:]  # This causes an error
users = ('imane',)+ users[1:] 
print(coordinates)
print(users)

# This is a set of unique integers
user_ids = {101, 102, 103, 101}  # Duplicate '101' is ignored
print(user_ids)   # Output: {101, 102, 103}

# This is a set of strings
user_names = {"Anna", "John", "Mike", "Sarah"}

# Adding new elements to a set
user_names.add("Anna")
user_names.add("David")
print(user_names) # Output: unordered set of names, no duplicates
# Sets do not allow indexing, so you cannot do something like:
#user_names[0] # this will cause an error
#Créez une liste de fruits et imprimez le deuxième fruit de votre liste.
fruits = ["banane","fraise","ananas"]
print(fruits[1])
#2. Créez un ensemble de nombres et essayez d’imprimer le dernier index de celui-ci
nombres = [1,2,3,4]
print(nombres[-1])
#.3. Créez un tuple de 5 noms de personnages de Star Wars et imprimez le troisième
starwars = ("Alice","Adam","Victor")
print(starwars[-1])
#nom.4. Créez un dictionnaire avec les informations sur une femme appelée Alice, 23 ans, qui vit à New York.
femme = {"name": "Alice", "age": 23 , "ville": "New york"}
print(femme["name"],femme["age"],femme["ville"])
# Check if both conditions are True using 'and'
print(10 > 5 and 20 < 30)  # Output: True

# Check if at least one condition is True using 'or'
print(10 < 5 or 20 > 15)  # Output: True
a = 5
b = 5
print(a == b)  # Output: True
print(a == 5)  # Output: True

# Not equal check
print(a != 3)  # Output: True
# Example:
age = 16

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
  # Example:
age = 10
if age >= 18:
      print("You are an adult.")
elif age >= 13:
      print("You are a teenager.")
else:
      print("You are a child.")
name = "Matt"
if name == "Matt":
      print("Your name is Matt")
elif name == John:
      print("Your name is John")
print("Bye!")
#using only "if" and "else"
user = 'Elie'
if user == 'Elie':
    print('Awesome!')
else:
    print('Nope!')
# Prompt the user for input
secret_word = input("Guess the secret word: ")

# Check the input and respond accordingly
if secret_word == "Python":
      print("Correct! You guessed the secret word!")
elif secret_word == "Java":
      print("Not quite, but close!")
else:
      print("Try again!")
if 1 > 2 or 2 > 1:
    print("cool!")

if 1 == 1 and 2 == 2:
    print("nice!")

if not False:
    print("it is true!")
  # Looping through a iterable - list
prime_numbers = [2, 3, 5, 7, 11]

for num in prime_numbers:
      print(num**2)
  # Looping through an iterable - set
fruits = {"apple", "banana", "cherry", "kiwi"}
for fruit in fruits:
      print(f"I like {fruit}")  # Printing a message for each fruit

  # Output for each iteration (order may vary):
  # I like apple
  # I like banana
  # I like cherry
  # I like kiwi
  # Example: Looping through a list
fruits = ["apple", "banana", "cherry", "kiwi"]

for fruit in fruits:
      print(f"J'adore {fruit}")
movies = ["tinanic", "forgive me", "cendrilon", "spirit"]

for movie in movies:
      print(f"J'adore {movie}")