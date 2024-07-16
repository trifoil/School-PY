class Mission:
    def __init__(self,nomMission,listeHero,listeMechant,resultat,listeDefisARelever=["defi1","defi2"]):
        self.__nomMission = nomMission
        self.__listeHero = listeHero
        self.__resultat = resultat
        self.__listeMechant = listeMechant
        self.__listeDefisARelever = listeDefisARelever

    @property
    def nomMission(self):
        return self.__nomMission
    @property
    def listeHero(self):
        return self.__listeHero
    @property
    def resultat(self):
        return self.__resultat
    @property
    def listeMechant(self):
        return self.__listeMechant
    @property
    def listeDefisARelever(self):
        return self.__listeDefisARelever
