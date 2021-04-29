"""
Przykładowa definicja klasy ułamek
"""

import math

class Ulamek:
    def __init__(self, licznik, mianownik):
        assert(mianownik > 0)
        temp = math.gcd(licznik, mianownik)
        self.licznik = licznik//temp
        self.mianownik = mianownik//temp
    
    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'
    
    def skracanie(self):
        temp = math.gcd(self.licznik, self.mianownik)
        self.licznik //= temp
        self.mianownik //= temp

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
    print(u1, '+', u2, '=', Ulamek.dodawanie(u1, u2))  # wykorzystanie metody statycznej
