import math

class Circle:
    def __init__(self, radius):
        #InitialiseR un cercle avec un rayon
        self.radius = radius

    @property
    def diameter(self):
    #Retourner le diamètre du cercle
        return self.radius * 2

    @property
    def area(self):
        #Retourner l'aire du cercle
        return math.pi * (self.radius ** 2)

    def __str__(self):
        #Afficher les attributs du cercle
        return f"Cercle(rayon={self.radius}, diamètre={self.diameter}, aire={self.area:.2f})"

    def __add__(self, other):
        #Additionner deux cercles et cree un nouveau cercle
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        #Comparer deux cercles
        return self.radius < other.radius

    def __eq__(self, other):
        #Vérifie les cercles sont égaux
        return self.radius == other.radius

#Test:
c_1 = Circle(5)
c_2 = Circle(7)
c_3 = c_1 + c_2  #cercle avec rayon = 5 + 7

print(c_1)  
print(c_2) 
print(c_3) 

# la Comparaison
print(c_1 < c_2)
print(c_1 == Circle(3)) 

# triée
cercles = [c_2, c_1, c_3]
cercles.sort()
print([str(c) for c in cercles])  
