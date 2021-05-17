"""
Przykładowa definicja klasy ułamek -- wykorzystanie metod specjalnych
"""

import math

class Ulamek:
    def __init__(self, licznik, mianownik):
        assert(mianownik > 0)
        self.licznik, self.mianownik = licznik, mianownik
        self.skracanie()

    # funkcja print
    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'
    
    def skracanie(self):
        temp = math.gcd(self.licznik, self.mianownik)
        self.licznik //= temp
        self.mianownik //= temp

    # przeciążamy operator ==
    def __eq__(self, u2):
        return self.licznik == u2.licznik and self.mianownik == u2.mianownik

    # przeciążamy operator + uzywając napisanej wcześniej metody statycznej
    def __add__(self, inny_ulamek):
        return Ulamek.dodawanie(self, inny_ulamek)

    # przeciążamy operator *
    def __mul__(self, u2):
        wynik = Ulamek(self.licznik*u2.licznik,
                       self.mianownik*u2.mianownik)
        return wynik

    # metoda statyczna
    @staticmethod
    def dodawanie(ulamek1, ulamek2):
        wynik = Ulamek(ulamek1.licznik*ulamek2.mianownik + ulamek2.licznik*ulamek1.mianownik,
                       ulamek1.mianownik*ulamek2.mianownik)
        wynik.skracanie()
        return wynik

if __name__ == '__main__':
    u1 = Ulamek(3, 4)
    u2 = Ulamek(2, 6)
    print(u1)
    print(u1, '+', u2, '=', Ulamek.dodawanie(u1, u2))  # wykorzystanie metody statycznej
    print(u1, '+', u2, '=', u1 + u2)  # przeciażenie +
    print(u1, '*', u2, '=', u1 * u2)  # przeciażenie *
    print(u1, '==', u2, '->', u1 == u2)
