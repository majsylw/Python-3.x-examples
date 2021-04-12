'''
Metoda Monte Carlo jest metodą stosowaną do matematycznego modelowania procesów zbyt złożonych, aby ich wynik można było obliczyć 
stosując podejście analityczne (za pomocą równań). Istotną rolę w tej metodzie odgrywa losowanie (wybór przypadkowy) 
wielkości charakteryzujących proces, przy czym losowanie dokonywane jest zgodnie z rozkładem, który musi być znany. 
Najprostszym przykładem pozwalającym zrozumieć daną metodę jest wyznaczanie przybliżonej wartości liczby π. 
Poniższy rysunek przedstawia daną ideę. Widoczny jest na nim okrąg o promieniu 
r = 1. Okrąg został wpisany w kwadrat, a więc pole tego kwadratu wyniesie P1 = (2r)^2. 
Idea metody Monte Carlo przybliżająca wartość liczby π, sprowadza się do tego, iż będziemy losować dwie liczby, 
będą one stanowić współrzędne punktu tj. wartość x oraz y. Dla każdego wylosowanego punktu musimy sprawdzić, 
czy mieści się on we wnętrzu kwadratu, tj.: x^2 + y^2 < 1. Wtedy możemy wyliczyć ile punktów wpadło do wnętrza kwadratu (k), 
w stosunku do wszystkich losowań (n)  →  P_2/P_1 =k/n. Liczbę π można natomiast wyliczyć stosując wzór π=4*P_2/P_1. 
Napisz program, który losując n par (sprawdź jak zmienia się dokładność wyliczenia liczby π dla różnej liczby losowań – 
rozsądnie jest losować bardzo dużo razy, np. 1000) liczb obliczy przybliżoną wartość liczby π. Wykorzystaj pakiet random 
do generacji liczb losowych o rozkładzie jednorodnym.
'''
import random

if __name__ == '__main__':
    random.seed(2021)
    n = int(input('liczba kroków Monte Carlo = '))
    k = 0
    for j in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            k += 1
    p = 4 * k / n
    print("pi =", p)