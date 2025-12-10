class CompteurPage:
    total_visites = 0

    def __init__(self,url: str,visites_par_pages: int= 0):
        self.visites_par_pages=visites_par_pages
        self.url = url
        CompteurPage.total_visites +=1
    def afficher_stats(self)->str :
        return (f"Page{self.url} - visits globaes : {CompteurPage.total_visites},"
                f"visites pour cette page : {self.visites_par_pages}")
    def enregistrer_lecture(self)-> int :
        self.visites_par_pages +=1
        return self.visites_par_pages
