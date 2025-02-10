#Exercice 1 : Bonjour le monde
print("Hello world\n" * 4)
#Exercice 2 : Un peu de mathématiques
#(99^3)*8(ce qui signifie 99 à la puissance 3, multiplié par 8).
result_1 = (9**3)*8
print(result_1) 
#Exercice 3 : Comment t'appelles-tu ?
#name = input("Comment t'appelles-tu ?")
#for namen in name :
      #print(f {movie}")
#Exercice 4 : Assez grand pour faire des montagnes russes           
height = int(input("Enter your height in cm: "))
if height >= 145:
    print(f"your height is {height} cm you are tall enough to ride")
else : 
    print(f"your height is {height} cm you need to grow some more to ride.")
#Exercise 5 : Favorite 
#Create a set called  with all your favorites numbers.
my_fav_numbers = {19 , 18 , 13 , 30}
#Add two new numbers to the set.
my_fav_numbers.add(15)
my_fav_numbers.add(16)
print(my_fav_numbers)
#Remove the last number.
my_fav_numbers.pop()
print(my_fav_numbers)
#Create a set
friend_fav_numbers = {96 , 17 , 89 , 23}
#our_fav_numbers
our_fav_numbers = my_fav_numbers | friend_fav_numbers
#our_fav_numbers = list(our_fav_numbers)
#our_fav_numbers.sort()
print(our_fav_numbers)
#Exercice 6 : Tuple
#Non un tuple en Python est immuable 
# si je souhaite ajouter des éléments je peux créer un nouveau 

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Supprimer Banana de la liste.
basket.remove("Banana")
print(basket)
#Supprimer Blueberries de la liste.
basket.remove("Blueberries")
print(basket)
#Ajouter Kiwi à la fin de la liste.
basket.append("kiwi")
print(basket) 
#Ajouter Apples au début de la liste.
basket.insert(0, 'Apples')
print(basket)
#Comptez combien de pommes il y a dans le basket.
apple_count = basket.count("Apples")
print(f"Nombre de pommes dans le basket : {apple_count}")
print(basket) 
#Vider le basket.
basket.clear()
print(basket) 
#Print(basket
#Exercice 8 : Commandes de sandwichs
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
#charcuterie n'a plus de pastrami, 
# utilisez une boucle while pour supprimer Pastrami 
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print  (sandwich_orders)
#Créez une liste vide appelée finished_sandwiches.
finished_sandwiched = [] 

#print(finished_sandwiched)
while sandwich_orders:
    sandwich = sandwich_orders.pop(0) 
    print(f"I made your {sandwich}.")
    finished_sandwiched.append(sandwich)


