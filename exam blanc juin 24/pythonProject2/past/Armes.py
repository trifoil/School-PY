class Arme:
    def __init__(self,nom,degat):
        self.__nom = nom
        self.__degat = degat


    @property
    def nom(self):
        return self.__nom
    @property
    def degat(self):
        return self.__degat
