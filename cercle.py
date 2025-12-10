import math
class Cercle:
    def __init__(self, rayon : float):
        self.rayon = rayon
    @property
    def rayon(self):
        return self._rayon
    @rayon.setter
    def rayon(self,valeur):
       if valeur <= 0 :
           raise ValueError("Doit etre ppositive")
       self._rayon = valeur
    @property
    def perimetre(self)->float:
         return 2*math.pi*self._rayon
    @property
    def surface(self)->float:
        return math.pi * self._rayon ** 2
    def agrandir(self,pourcentage: float)->float:
        if pourcentage < 0 :
            raise ValueError("Doit etre positive")
        self._rayon = self._rayon * (1+pourcentage/100)


