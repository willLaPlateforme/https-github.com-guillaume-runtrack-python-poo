class Rectangle:
    
    def __init__(self, longueur, largeur):
          self.__longueur=longueur
          self.__largeur=largeur
          
    def get_longueur(self):
          return self.__longueur
    
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
         return self.__largeur
    
    def set_largeur(self, largeur):
         self.__largeur = largeur

C=Rectangle(10, 5)
print(C.get_longueur())
print(C.get_largeur())

C.set_longueur(15)
C.set_largeur(7)

print(C.get_longueur())
print(C.get_largeur())



    