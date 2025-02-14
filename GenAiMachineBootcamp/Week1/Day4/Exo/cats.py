#Exercice 1 : Les animaux de compagnie
from pets import Cat#Créez une autre race de chat nommée Siamese
from pets import Pets
from pets import Bengal
from pets import Chartreux
class Siamese(Cat) :#qui hérite de la Catclasse.
    def __init__(self, name, age):
        super().__init__(name, age) 
        self.all_cats = []
        
chat1 = Bengal("Minou", 5)
chat2 = Chartreux("Pixou", 8)
chat3 = Siamese("Twix", 2)


all_cats = [chat1, chat2, chat3] 
sara_pets = Pets(all_cats)


sara_pets.walk()

#Créez une liste appelée all_cats, qui contient trois instances de chat : un Bengal, un Chartreux et un Siamois.
#Ces trois chats sont les animaux de compagnie de Sara. 
#Emmenez tous les chats en promenade, utilisez la walkméthode.