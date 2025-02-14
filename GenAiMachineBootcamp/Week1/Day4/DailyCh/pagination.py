class Pagination:
    def __init__(self, items=None, page_size=10):
        """Initialise la pagination avec une liste d'éléments et une taille de page."""
        self.items = items if items is not None else []
        self.page_size = int(page_size)  # un entier
        self.total_pages = max(1, (len(self.items) + self.page_size - 1) // self.page_size)  # Nombre total de pages
        self.current_page = 1  # la première page

    def getVisibleItems(self):
        """Retourne la liste des éléments visibles sur la page actuelle."""
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def nextPage(self):
        """Passe à la page suivante ."""
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self 

    def prevPage(self):
        """Revient à la page précédente ."""
        if self.current_page > 1:
            self.current_page -= 1
        return self  

    def firstPage(self):
        """Go à la première page."""
        self.current_page = 1
        return self  # Permet le chaînage

    def lastPage(self):
        """Go à la dernière page."""
        self.current_page = self.total_pages
        return self  # Permet le chaînage

    def goToPage(self, pageNum):
        """Va à une page spécifique en s'assurant qu'elle est dans les limites valides."""
        pageNum = int(pageNum)  # Convertit en entier si un float est donné
        if pageNum < 1:
            self.current_page = 1
        elif pageNum > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = pageNum
        return self 

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

#  4 éléments par page
p = Pagination(alphabetList, 4)


print(p.getVisibleItems())  

p.nextPage()
print(p.getVisibleItems()) 

p.lastPage()
print(p.getVisibleItems()) 
p.firstPage()
print(p.getVisibleItems())  

p.goToPage(3)
print(p.getVisibleItems()) 

# plus grand que le total
p.goToPage(100)
print(p.getVisibleItems())

#zéro ou négatif
p.goToPage(0)
print(p.getVisibleItems()) 

#mode chaînage
p.firstPage().nextPage().nextPage()
print(p.getVisibleItems()) 
