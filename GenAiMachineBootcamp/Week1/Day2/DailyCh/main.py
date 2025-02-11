#Défi
#Demandez un mot à un utilisateur.
word = input("Entrez un mot : ")

#Écrivez un programme qui crée un dictionnaire
letter_index = {}
#Ce dictionnaire stocke les index de chaque élément letter dans une liste
for index, letter in enumerate(word):
    if letter in letter_index:
        letter_index[letter].append(index) 
    else:
        letter_index[letter] = [index] #Assurez-vous que les lettres sont les keys.
#Assurez-vous que les lettres sont strings.

# Afficher le dictionnaire résultant
print(letter_index)
#ssurez-vous que les index sont stockés dans un fichier list, et que ces listes sont values.

#Exemples
#dodo ➞ { "d" : [0, 2], "o" : [1, 3] }
#« grenouille » ➞ { « f » : [0], « r » : [1], « o » : [2], « g » : [3, 4], « y » : [5] }
#« raisins » ➞ { « g » : [0], « r » : [1], « a » : [2], « p » : [3] }