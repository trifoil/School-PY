from SuperHumain import SuperHumain


class SuperHero(SuperHumain):
    def __init__(self, nom, listeSuperpouvoirs,historiqueMissions):
        super().__init__(nom, listeSuperpouvoirs)
        self.__historiqueMissions = historiqueMissions

    @property
    def historiqueMissions(self):
        return self.__historiqueMissions

    def ajouterSuperpouvoir(self, superPouvoir: 'SuperPower'):
        self._listeSuperpouvoirs.append(superPouvoir)

    def afficherSuperPouvoir(self):
        for s in self._listeSuperpouvoirs:
            print(s.nomPouvoir)

    def participerMission(self, mission: 'Mission'):
        print(f"Le hero participe à la mission {self.mission.nomMission} ")
        for desc in mission.listeDefisARelever:
            print(desc)
    def afficherInfo(self):
        print(f"Le Hero : {self.info.nom} sa liste de pouvoirs {self.listeDefisARelever} ainsi que son historique de missions {self.historiqueMissions}")
