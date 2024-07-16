import time

from Armes import Arme
from Soldat import Soldat
from Terroriste import Terroriste


class Tournament:
    def __init__(self):
        pass

    def lancer_combat(self,s:'Soldat',t:'Terroriste'):
        try:
            while not t.point_de_vie < 0:
                time.sleep(1)
                s.infliger_degats(t)
                s.point_de_vie = s.point_de_vie -1
                print(t.point_de_vie , " pv restant(s)")
            print(s.nom + " est le vainqueur")
        except Exception as e:
            print(e)


arme = Arme("Akk-47", 30)
k = Soldat("kevin",21,50,60,50,arme)
terro = Terroriste("Ina",21,500,1,1)
test = Tournament()
test.lancer_combat(k,terro)

