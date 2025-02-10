#Défi 1
#Demandez à l'utilisateur un number et un length.
number = int(input ("entrez un nombre ? "))
length = int(input("entrez une longueur ? "))
multiple = []
#Créez un programme qui imprime une liste de multiples

for numleng in range(1, length + 1) :
   multiple.append(number*numleng)  

print(f" number : length {length} ➞ {multiple}")
#Défi 2
text = input("entrez un mot ?")
def remove_consecutive_duplicates(text):
    result = ""
    for i in range(len(text)):
        if i == 0 or text[i] != text[i - 1]: 
            result += text[i]
    return result
result = remove_consecutive_duplicates(text)
print(f" user word : {text} ➞  {result} ")
    
