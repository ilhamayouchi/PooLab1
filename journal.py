from datetime import datetime
class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="utf-8")
        return self
    def enregistrer(self, tache:str):
        self.fichier.write(f"{datetime.now().isoformat()}{tache}\n")
    def __exit__(self,exc_type,exc,tb):
        self.fichier.close()
    def lire():
        with open("journal.txt","r") as f:
            lignes = f.readlines()
            for l in reversed(lignes):
                print(l)
    