
# Kilka słów uzupełnienia na temat kolekcji i funkcji

## List comprehension

Jedną z cech Pythona jest dostępność składni funkcyjnej. Jak można oczekiwać, upraszcza to znacznie operowanie na listach i innych kolekcjach. Jedną z takich konstrukcji jest tzw. lista składana (ang. list comprehension), jak w przedstawionym poniżej przykładzie obliczania drugiej potęgi pierwszych pięciu liczb naturalnych dla 3 wariantów.

```python
# tworzymy listę na której będziemy operować
liczby = [1, 2, 3, 4, 5]

# wypełniamy listę 2 potęgami
nowe_liczby21 = [i ** 2 for i in liczby]
print(nowe_liczby21)

# jeśli liczba jest parzysta wypełniamy listę 2 potęgami
nowe_liczby22 = [i ** 2 for i in liczby if i%2==0]
print(nowe_liczby22)

# jeśli liczba jest parzysta wypełniamy listę 2 potęgami, inaczej wstawiamy 1
nowe_liczby23 = [i ** 2 if i%2==0 else 1 for i in liczby]
print(nowe_liczby23)
```

Jak widac lista składana umożliwia sprawne operowanie na elementach listy (jak pętla `for`) zarowno stosując konstrukcję `if` (`if-else`), jak i obywając się bez instrukcji warunkowcyh.

## Wyrażenia `lambda`

Python za pomocą pewnych wyrażeń pozwala nam zdefiniować jednolinijkowe mini-funkcje. Te funkcje to tzw. wyrażenia `lambda`, które w istocie są jednolinijkowymi, anonimowymi funkcjami, które można szybko wykorzystać na przykład tworząc listę składaną. Najprostsza froma wyrażenia lambda ma postać

```python
lambda <parametry> : <wyrażenie>
```

Jest to funkcja która nie ma nazwy. Poprzez użycie słowa kluczowego 'lambda' informujemy Python, że właśnie taką anonimową funkcję chcemy utworzyć. Następnie podajemy listę parametrów, które chcemy aby przyjmowała, używamy „:”, oraz definiujemy jej zawartość.

```python
lambda x : x + 1    # funkcja przyjmuje jeden parametr, a następnie dodaje jeden i zwraca wynik
lambda _ : _ + 1    # ta funkcja robi dokładnie to samo, ale zamiast nazwy parametru podajemy znak 

# wyrażenie lambda możemy przypisać do obiektu i korzystać z niego jak z funkcji
jeden_argument = lambda x : x + 1
print(jeden_argument(5))
wyrazenie_lambda = lambda x,y: x+y
wyrazenie_lambda(2,3)

# tutaj wywołamy funkcję bez przypisywania do 'zmiennej'
print((lambda x,y: x+y)(3,4))
```

Aby zrozumieć `lambdę`, musimy najpierw uświadomić sobie że istnieje coś takiego jak funkcje wyższego rzędu, czyli taką funkcję, która przyjmuje jako parametr inną funkcję, lub zwraca funkcję. Wtedy po prostu jako argument dla takiej funkcji nie ma potrzeby tworzenia innej tylko podania wyrażenia lambda (lub jego zwrócenia). Wyrażenia lambda także pozwalają na *definicję funkcji w funkcji* - jedno wyrażenia lambda wygeneruje drugie.

```python
# zdefiniowanie wyrażń lambda - jeden w drugim (wyrażenie lambda generuje drugie)
sumator = lambda x: lambda y: x + y
print(sumator(2)(3))  # wywołanie

# inne zastosowania: map, filter, reduce, sorted
lista = [1,3,5,7]
from functools import reduce
print(f"Nasza lista: {lista}\n")
print(f"Przykład zastosowania map: {list( map(lambda _: _*2, lista) )}")
print(f"Przykład zastosowania filter: {list( filter(lambda _: _>3, lista) )}")
print(f"Przykład zastosowania reduce: { reduce(lambda x,y: x+y, lista) }")

things = {'a': 11, 'b': 2, 'c': 0, 'd': 33}
print(sorted(things.items(), key=lambda x: x[1]))  # sortujemy po wartości ze słownika
```

Lambda nie wnosi niczego, czego nie byli byśmy wstanie osiągnąć za pomocą zwykłej funkcji. Jej celem jest jedynie skrócenie zapisu. Trzeba jednak przyznać, że jest bardzo wygodna w użyciu.

## Generatory

Generatory są w Pythonie mechanizmem leniwej ewaluacji funkcji, która w przeciwnym razie musiałaby zwracać obciążającą pamięć lub kosztowną w obliczaniu listę.

```python
# definiujemy generator generuj_calkowite
def generuj_calkowite(n):
    for i in range(n):
        yield i # produkujemy sekwencję wartości, a nie zwracamy wysecyfikowanej dokładnie liczby (jak w przypadku return)

print(type(generuj_calkowite(7)))  # wypisze <class 'generator'>
for i in generuj_calkowite(7):
    print i
```

Definicja generatora przypomina definicję funkcji, ale zamiast słowa kluczowego `return` używa się `yield`. Jednakowoż generator jest obiektem przechowującym stan, mogącym wielokrotnie wchodzić do i opuszczać ten sam dynamiczny zakres. Wywołanie generatora może być użyte zamiast listy lub innej struktury, po której elementach będziemy iterować. Za każdym razem, gdy pętla for w powyższym przykładzie potrzebuje następnego elementu, wywoływany jest generator, który daje następny element.

# O klasach raz jeszcze

Kontynuując nasza opowieść na temat tworzenia klas jest przeciążenie operatorów, które w pythonie sprowadza się do zdefiniowania pewnych [metod specjalnych](https://docs.python.org/3/reference/datamodel.html#special-method-names), jak na przykład: dodawanie `__add__`, odejmowanie `__sub__`, czy mnożenie `__mul__`. Przeciążanie operatorów jeat więc sposobem na nadanie znaczenia takich operatorów, jak `+`, `>` czy `==` w sytuacji, gdy ich argumentami są obiekty klas przez nas definiowanych. Przeciążanie nie jest zwykle absolutnie konieczne, choć bywa bardzo wygodne (zamiast przeciążać operatory, można definiować zwykłe funkcje i metody wykonujące te same zadania, jak to zrobilismy tydzień temu definiując metodę statyczną).

Wspomniane metody `__add__` i `__sub__`mogą być wykorzystywane do emulacji obiektów liczbowych. Jeśli obiekty danego typu nie obsługują pewnych operacji (np. operacji bitowych w przypadku liczb niecałkowitych), odpowiadające im metody należy pozostawić niezdefiniowane. Dla naszej uprzednio zdefiniowanej klasy Ulamek mogą wyglądać następująco:

```python
    # przeciążamy operator *
    def __mul__(self, u2):
        wynik = Ulamek(self.licznik*u2.licznik,
                       self.mianownik*u2.mianownik)
        return wynik

    # przeciążamy operator + uzywając napisanej wcześniej metody statycznej
    def __add__(self, inny_ulamek):
        return Ulamek.dodawanie(self, inny_ulamek)

    # metoda statyczna
    @staticmethod
    def dodawanie(ulamek1, ulamek2):
        wynik = Ulamek(ulamek1.licznik*ulamek2.mianownik + ulamek2.licznik*ulamek1.mianownik,
                       ulamek1.mianownik*ulamek2.mianownik)
        wynik.skracanie()
        return wynik
```

Innym rodzajem są tzw. metody "porównań szczegółowych", a wywoływane są przy użyciu operatorów porównania przed wywołaniem opisanej poniżej metody, czyli:
-`__lt__` czyli `<`,
-`__le__` czyli `<=`,
-`__eq__` czyli `==`,
-`__ne__` czyli `!=`,
-`__gt__` czyli `>`,
-`__ge__` czyli `>=`.

```python
    # przeciążamy operator ==
    def __eq__(self, u2):
        return self.licznik == u2.licznik and self.mianownik == u2.mianownik
```
