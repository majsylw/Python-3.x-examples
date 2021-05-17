# lista składana (ang. list comprehension), podobnie wyglądaj set comprehension i tuple comprehension
liczby = [1, 2, 3, 4, 5]

# jeśli liczba jest parzysta wypełniamy listę 2 potęgami, inaczej 1 
nowe_liczby = []
for i in liczby:
    if i % 2 == 0:
        nowe_liczby.append(i ** 2)
    else:
        nowe_liczby.append(1)

print(nowe_liczby)

nowe_liczby21 = [i ** 2 for i in liczby]  # wypełniamy listę 2 potęgami
print(nowe_liczby21)
nowe_liczby22 = [i ** 2 for i in liczby if i%2==0 ]  # jeśli liczba jest parzysta wypełniamy listę 2 potęgami
print(nowe_liczby22)
nowe_liczby2 = [i ** 2 if i%2==0 else 1 for i in liczby]  # jeśli liczba jest parzysta wypełniamy listę 2 potęgami, inaczej 1 (jak w petli powyżej)
print(nowe_liczby2)

###################################################################################################################################################
# funkcje a wyrażenia lambda

# standardowa definicja funkcji suma
def suma(x, y):
    return x + y
print(suma(2, 3))  # wywołanie funkcji suma

# zdefiniowanie wyrażenia lambda - jeden argument
potega = lambda x: x**2
print(potega(16))  # wywołanie

# zdefiniowanie wyrażń lambda - jeden w drugim (wyrażenie lambda generuje drugie)
sumator = lambda x: lambda y: x + y
print(sumator(2)(3))  # wywołanie

# generatory
'''
Generatory są w Pythonie mechanizmem leniwej ewaluacji funkcji, 
która w przeciwnym razie musiałaby zwracać obciążającą pamięć lub kosztowną w obliczaniu listę.
'''
print(range(3))

def generuj_calkowite(n):
    for i in range(n):
        yield i

print(generuj_calkowite)
for i in generuj_calkowite(7):
    print(i)
