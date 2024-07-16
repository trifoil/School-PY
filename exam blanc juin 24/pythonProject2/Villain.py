from abc import *


class Villain:
    def __init__(self):
        pass

    @abstractmethod
    def afronterHero(self,superHero:'SuperHero'):
        pass
