class SuperPower:
    def __init__(self, nomPouvoir, descriptionPouvoir, niveauPuissance):
        self.__nomPouvoir = nomPouvoir
        self.__descriptionPouvoir = descriptionPouvoir
        self.__niveauPuissance = niveauPuissance

    """
    GETTERS
    """
    @property
    def nomPouvoir(self):
        return self.__nomPouvoir

    @property
    def descriptionPouvoir(self):
        return self.__descriptionPouvoir

    @property
    def niveauPuissance(self):
        return self.__niveauPuissance

    """
    SETTERS
    """
    @nomPouvoir.setter
    def nomPouvoir(self,nouveauNom):
        self.__nomPouvoir = nouveauNom


