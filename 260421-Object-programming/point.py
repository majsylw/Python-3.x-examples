"""
Przykładowa definicja klasy Punkt
"""

class Point:

    # konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # destruktor
    def __del__(self):
        class_name = self.__class__.__name__
        print("Usunięto obiekt:", class_name)

    # metoda -- tu akurat wyliczamy wartość y na podstawie równania prostej
    def prosta(self, a, b):
        self.y = self.x * a + b

    # przeciążenie operatora wypisywania na ekran --- funkcja print
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

if __name__ == '__main__':
    zmienna = Point(2, 3)
    print("Przed: ")
    print(zmienna.x, zmienna.y)
    zmienna.prosta(2, 2)
    print(zmienna.y)
    print(zmienna)
