import Mission
import SuperPower
from abc import *


class SuperHumain:
    def __init__(self, nom, listeSuperpouvoirs):
        self._nom = nom
        self._listeSuperpouvoirs = listeSuperpouvoirs



    @property
    def nom(self):
        return self._nom

    @property
    def listeSuperPouvoir(self):
        return self._listeSuperpouvoirs


    @abstractmethod
    def ajouterSuperpouvoir(self, superPouvoir: 'SuperPower'):
        pass
    @abstractmethod
    def participerMission(self, mission: 'Mission'):
        pass
    @abstractmethod
    def afficherInfo(self):
        pass
