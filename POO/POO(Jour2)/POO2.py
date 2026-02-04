class Livre:
    
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
          
    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")


# Exemple d'utilisation
C = Livre(
    "Le capital, la spéculation et la finance au XIXe siècle",
    "Claudio Jannet",
    601
)

# Affichage des valeurs initiales
print(C.get_titre())            
print(C.get_auteur())           
print(C.get_nombre_de_pages())  

# Modification des valeurs
C.set_titre("Babylone")
C.set_auteur("René Crevel")
C.set_nombre_de_pages(316)

# Affichage des valeurs modifiées
print(C.get_titre())            # Babylone
print(C.get_auteur())           # René Crevel
print(C.get_nombre_de_pages())  # 316

# Test avec une valeur invalide pour le nombre de pages
C.set_nombre_de_pages(-50)     
print(C.get_nombre_de_pages())  
