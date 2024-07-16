from Humain import Humain


class Terroriste(Humain):
    def __init__(self, nom, age, point_de_vie, force_datk, resistance):
        super().__init__(nom, age, point_de_vie, force_datk)
        self._resistance = resistance

    @property
    def resitance(self):
        return self._resistance
