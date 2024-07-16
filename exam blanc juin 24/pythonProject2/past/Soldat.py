from Humain import Humain
from Terroriste import Terroriste


class Soldat(Humain):
    def __init__(self,nom, age, point_de_vie,defense,force_datk,arme):
        super().__init__(nom, age, point_de_vie,force_datk)
        self._defense = defense
        self._arme = arme

    @property
    def defense(self):
        return self._defense
    @property
    def arme(self):
        return self._arme
    def infliger_degats(self,t:'Terroriste'):
        t.point_de_vie = t.point_de_vie - self.arme.degat*2


