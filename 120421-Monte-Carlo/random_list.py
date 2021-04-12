'''
Stwórz 5-cio elementową listę liczb zespolonych wypełnionych 
wartościami losowymi o module równym 1.
'''
import numpy as np
import random


if __name__ == '__main__':
    # tworzymy tablicę liczb zespolonych
    Z = np.zeros(10, dtype=complex) ## tablica liczb zespolonych -- dtype oznacza typ
    print(Z)

    # przechodząc do treści zadania
    random.seed(2021) # ustalamy random seeda, UWAGA musi być z tej samej biblioteki co funkcje losujące
    lista = []
    for i in range(5):
        real = random.random()
        imag = (1 - random.random()**2)**(1/2)
        sign_real = random.randint(0, 1)  # dodatkowo losujemy 0 (-) lub 1 (+)
        sign_imag = random.randint(0, 1)
        if not sign_real:
            real *= -1
        if not sign_imag:
            imag *= -1
        # liczba = complex(real, imag)  # tak też można stworzyć tę liczbę
        lista.append(real+imag*1j)
    print(lista)
