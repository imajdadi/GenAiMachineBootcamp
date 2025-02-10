name = 'John Doe'
longueur = len(name)
if longueur > 20:
    print(f"Name {name} is more than 20 chars long")
    length_description = 'long'
elif longueur > 15:
    print(f"Name {name} is more than 15 chars long")
    length_description = 'semi long'
elif longueur > 10:
    print(f"Name {name} is more than 10 chars long")
    length_description = 'semi long'
elif 8 <= longueur <= 20:
    print(f"Name {name} is 8, 9 or 10 20 chars long")
    length_description = 'semi short'
else:
    print(f"Name {name} is a short name")
    length_description = 'short'
#Vous avez une amie qui s'appelle Alice 
name2 = "Alice"
age = 30
city = "New York"
print("Hello, {}. You are {}. live in {}".format(name2, age , city))
