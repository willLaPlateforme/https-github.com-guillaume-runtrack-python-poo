class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def afficherLesPoints(self):
        print(self.X , self.Y)
        
    def afficherX(self):
        print(self.X)

    def afficherY(self):
        print(self.Y)
        
    def changerX(self, x):
       
       self.X = x

       print(self.X)
        
    def changerY(self, y):

        self.Y = y

        print(self.Y)

pt=Point(5, 15)
pt.afficherLesPoints()
pt.afficherX()
pt.afficherY()
pt.changerX(7)
pt.changerY(20)
