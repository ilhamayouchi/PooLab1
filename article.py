class Article:
    reference: str
    designation : str
    prix_ht : float 
    stock: int 

    def __init__(self,reference,designation,prix_ht,stock):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock 
    def valeur_stock(self)->float :
        return self.prix_ht * self.stock
    def __str__(self) :
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} € HT"
    def approvisionner(self, qte: int) :
      self.stock += qte
#Mouvements du augmentation
      with open("mouvements.log", "a", encoding="utf-8") as f:
              f.write(
                f"Approvisionnement : {qte} unités ajoutées à "
                f"{self.reference} ({self.designation}). "
                f"Nouveau stock = {self.stock}\n"
            )
