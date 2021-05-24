'''
Napisz dekorator, który wypisze informację o czasie wykonywania funkcji.
Dekorator, powinien być gotowy dekorować funkcje przyjmujące różną liczbę parametrów.
'''

import time
def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się", koniec - start, "sekund.")
        return x
    return wew

@dekor
def dodaj(a,b):
    time.sleep(1)
    return a+b

@dekor
def odejmij(a,b,c):
    time.sleep(0.5)
    return a-b-c

print(dodaj(2,2))
print(odejmij(1,2,3))
