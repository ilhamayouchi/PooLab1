class Convertisseur:
    taux_eur_dh = 10.9
    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh
    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        return cls.taux_eur_dh
    @staticmethod
    def vers_eur(self,dirhams: float):
        return dirhams/Convertisseur.taux_eur_dh
    