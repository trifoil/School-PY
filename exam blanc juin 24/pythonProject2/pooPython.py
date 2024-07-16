"""
Exercice POO pour Augustin

"""
from abc import ABCMeta, abstractmethod

"""Exemple d'une interface en Python, même si Python ne les a pas besoin de base"""

class IFoo:

    #je veux juste être fancy, tu peux tout simplement hériter IFoo de ABC
    __metaclass__ = ABCMeta

    #méthode abstraite d'une interface qui doivent être reprises par la classe qui implémente
    @abstractmethod
    def abstractFunction(self):
        pass

    #pour montrer plus tard que l'implémentation est necessaire
    @abstractmethod
    def autreAbstraiteFunction(self):
        raise NotImplementedError


"""Exemple modèle d'une classe en Python"""
#Declaration d'une classe qui implémente une interface
class Foo(IFoo):

    #variable de classe, elle reste la même pour chaque instance de cette classe
    unTruc = 'caca' 

    #variable statique
    staticVar = 0

    #Declaration d'un constructeur avec des paramètres passées
    def __init__(self, bar, pif, paf):  
        
        self.bar = bar   #variable d'instance, propre à une instance de la classe. Celle ci est publique, elle peut-être modifié et consulté partout dans le code

        self._pif = pif  #variable protégé, elle peut être directement modifié à l'intérieur de la classe et hérité par des classes filles

        self.__paf = paf #variable privé, elle peut être modifié qu'à l'intérieur de la classe auquelle elle appartient 
        #Encapsulation en python est juste décorative

        type(self).staticVar += 1   #on peut manipuler les variable statiques qui restera en rapport avec la classe


    #Declaration de la fonction de la classe. Des instances peuvent l'appeler
    def laFonction(self):
        
        return self.bar + str(self._pif + self.__paf)
    

    #Fonction statique. Elle n'est pas influencé par l'instance. Remarque le manque de 'self' entre les parenthèses 
    @staticmethod
    def staticFonction() -> str:

        return "\nDesmet peut me sucer la queue"
    

    #Plusieurs fonctions peuvent avoir le même nom mais utiliser des paramètres différentes. On appele ça du polymorphisme
    #Bon jsp si python permet de faire du vrai polymorphisme à l'intérieur de la même classe donc je fais ça comme ça
    def polymorphisme(self, strVal = None, intVal = None):

        if strVal != None:
            print("\nJ'effectue la fonction avec un String\n")
            print(self.bar + strVal)

        elif intVal != None:
            print("\nJ'effectue la fonction avec un Integer\n")
            for i in range (0, intVal):
                print(self.bar + "\t")

        else:
            print("\nVa te faire foutre")


    #Overloading d'une fonction implémenté (pas une surcharge dans ce cas)
    def abstractFunction(self):
        print("Tu m'as bien implémenté, ouais")


"""Exemple d'un héritage entre les classes"""
class Child(Foo):

    def __init__(self, bar, pif, paf, sup):

        #On appele le constructeur de la classe-mère pour lui passer des variables partagées
        super().__init__(bar, pif, paf)

        self.__sup = sup

    
    #Le polymorphisme peut s'effectuer aussi entre 2 classes en héritage 
    def polymorphisme(self, intFloat):

        print("\nJ'effectue la fonction avec un Float\n")
        print(intFloat / 0.25)
    

"""On va tester tout ça"""

#Déclaration des instances des 2 classes
instanceFoo = Foo("Pute", 6, 9)

instanceChild = Child("Pétasse", 420, 666, "supplément")

#Variable statique staticVar est de 1, alors qu'on a appelé le constructeur de Foo aussi dans Child. Python est blazé? Nouveux, je savais pas
print(Foo.staticVar)

#Prenons la classe Foo. On essaye d'utiliser ses fonctions

print(instanceFoo.laFonction())
instanceFoo.polymorphisme(" mdr")
instanceFoo.polymorphisme(None,3)
instanceFoo.polymorphisme()
instanceFoo.abstractFunction()

try:
    instanceFoo.autreAbstraiteFunction()
except Exception as exc:
    print("Cette fonction n'a pas été implémenté, connard")


#Prenons la classe Child. On essaye d'utiliser ses fonctions

print(instanceChild.laFonction())
instanceChild.polymorphisme(5)

#Il motre que Child c'est l'instance de Foo aussi. D'autant plus je comprends pas pq Child n'influence pas staticVar
print(isinstance(instanceChild, Foo))
print(isinstance(instanceChild, Child))
