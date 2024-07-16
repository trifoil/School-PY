class Humain:
    def __init__(self, nom, age, point_de_vie,force_datk):
        self._nom = nom
        self._age = age
        self._point_de_vie = point_de_vie
        self._force_datk = force_datk

    @property
    def force_datk(self):
        return self._force_datk
    @property
    def point_de_vie(self):
        return self._point_de_vie

    @point_de_vie.setter
    def point_de_vie(self, nouveau_point_de_vie):
        self._point_de_vie = nouveau_point_de_vie

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, nouvel_age):
        self._age = nouvel_age

    def parler(self, phrase):
        pass

    def manger(self):
        pass
