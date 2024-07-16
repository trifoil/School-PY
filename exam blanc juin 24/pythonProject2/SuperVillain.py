import random

import SuperHero
from SuperHumain import SuperHumain
from Villain import Villain


class SuperVillainProf(SuperHumain,Villain):
    def __init__(self,nom,listeSuperPouvoirs,repliqueDiablique):
        super().__init__(nom,listeSuperPouvoirs)
        self._repliqueDiabolique = repliqueDiablique


    def afronterHero(self,superHero:'SuperHero'):
        choixPouvoir = random.choice(self.listSuperPouvoirs)
        print(f"Le mechant : {self.nom} attaque le superHero nommé "
              f"{superHero.nom} avec le superPouvoir nommé "
              f"{choixPouvoir.nomPouvoir}")

