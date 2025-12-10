from article import Article

a1 = Article("A100", "Stylo bleu", 3.5, 120)
a2 = Article("B200", "Bloc-notes A5", 12.0, 50)
a3 = Article("C300", "Clé USB 32 Go", 25.0, 30)

articles = [a1,a2,a3]

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")
a1.approvisionner(50)
a2.approvisionner(20)
a3.approvisionner(500)
print(a1.stock)
print(a2.stock)
print(a3.stock)