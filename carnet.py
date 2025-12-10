from contact import Contact
class Carnet:
    def __init__(self):
        self._contacts = [] #Att d'instance
    def ajouter(self, contact : Contact):
        self._contacts.append(contact)
    def rechercher(self,fragment: str):
        fragment = fragment.lower()
        liste_attendus = []
        for c in self._contacts:
            if fragment in c.nom.lower():
                liste_attendus.append(c)
        return liste_attendus
    def afficher_tous(self):
       for c in self._contacts:
           print(c)
    @property
    def nombre_contacts(self):
        return len(self._contacts)