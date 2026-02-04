class Personne:
    def __init__(self, nom="Doe", prenom="John"):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"


# Instanciation de plusieurs personnes
personne1 = Personne("Alice", "Martin")
personne2 = Personne("Bob", "Durand")
personne3 = Personne()  # Utilise les valeurs par défaut

# Appel de la méthode SePresenter pour vérifier
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
