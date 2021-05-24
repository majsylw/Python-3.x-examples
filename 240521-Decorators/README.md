# Dekoratory

Jedną z ważnych koncepcji, na drodze do stania się sprawnym programistą Python, są dekoratory. Mieliśmy już z nimi do czynienia w przypadku nauki programowania obiektowego, gdzie wykorzystywaliśmy dekorator, aby zadeklarować metody statyczne. Jest to jednak wierzchołek góry lodowej, a same dekoratory, okazują się być niezwykle przydatne oraz często spotykane.

## `*args` oraz `**kwargs` czyli zmienna liczba argumentów

Do tej pory, nasza definicja funkcji w Python, zakładała, stałą liczbę parametrów. Mogły to być liczby, tekst, listy, ale zawsze ich liczba była stała. Z czasem, pojawia się konieczność, przygotowania naszej funkcji na przyjęcie zmiennej liczby parametrów. Tutaj, z pomocą przychodzi nam pojedyncza `*` i podwójna `**`.

W przypadku pojedynczej `*` definicja naszej funkcji, zawiera zmienną, której nazwa rozpoczyna się od `*`. Jest to informacja, że parametry przekazane do funkcji, należy 'spakować', do zmiennej typu krotka. Czyli forma podobna do listy, lecz niemodyfikowalna. Tym samym, niezależnie, z jaką liczbą parametrów, wywołamy funkcję, czy 0 czy 100, wszystkie zostaną umieszczone w krotce. W tym przypadku, jest to nazwa `args`, jednak może być dowolna inna nazwa zmiennej (nazwa `*args` jest konwencją).

```python
def foo(*args):
    print("Liczba przekazanych parametrów:",len(args))
    for arg in args:
        print ("Wartość:",arg)
    
lista = [1,3,5,6]
    
foo(1,lista,2,'xyz',3)
```

Język Python, daje nam jeszcze jedną, ciekawą możliwość. Mianowicie, możemy przekazywać do funkcji, zmienne typy `klucz:wartość`. Tutaj definiujemy funkcję z parametrem `**`. Jest to informacja dla Python, że przekazywane parametry, są typy `klucz:wartość`, i należy je 'spakować', oraz umieścić w zmiennej typu słownik. Aby pobrać wartość posługujemy się kluczem jak dla słównika.

```python
def foo2(**kwargs):
    print("Liczba przekazanych parametrów:",len(kwargs))

    for key, item in kwargs.items():
        print ("Klucz:", key, "Wartość:", item)

foo2(a=1,b=2,c=3)

# Zarówno * jak i ** , możemy wykorzystać w tej samej definicji funkcji
def foo3(*args, **kwargs):
    
    print("Liczba przekazanych parametrów *args:",len(args))
    for arg in args:
        print ("Args - Wartość:", arg)
    
    print("Liczba przekazanych parametrów **kwargs:",len(kwargs))
    for key, item in kwargs.items():
        print ("Kwargs - ", "Klucz:", key, "Wartość:", item)
funk(11,22,['x','y','z'],a=1,b=2,c=3)
```

## Dekoratory w praktyce

Dekoratory w Pythonie opierają się przede wszystkim na dwóch założeniach:

- funkcja może przyjąć jako argument inną funkcję,

```python
def srednia(funkcja, argumenty):
    x = funkcja(**kwargs)
    return x

def srednia_wazona(wagi, liczby):
    suma = 0
    sum_wag = 0
    for i in range(len(wagi)):
        suma += wagi[i]*liczby[i]
        sum_wag += wagi[i]
    return suma/sum_wag

def srednia_arytmetyczna(liczby):
    suma = 0
    for a in liczby:
        suma += a
    return suma/len(liczby)

srednia(srednia_wazona, {'wagi': [2, 3], 'liczby': [5, 4]})
srednia(srednia_arytmetyczna, {'liczby': [5, 4]}))
```

- wewnątrz funkcji można stworzyć kolejną funkcję,

```python
def główna():

    def wewnętrzna(a,b):
        return a*b

    x = wewnętrzna(2,3)
    return x

główna()
```

- funkcja może zwracać funkcję.

```python
def główna():

    def wewnętrzna(a,b):
        return a*b

    return wewnętrzna

x = główna()
x(3,3)
```

Dekorator w Pythonie, to nic innego jak funkcja, która przyjmuje jako parametr funkcję, którą chcemy udekorować, następnie tworzy wewnętrzną funkcję, która nadpisuje działanie przekazanej przez parametr funkcji, a następnie zwraca wewnętrzną funkcję. Python w kwestii pisania dekoratorów pozwala na użycie go poprzez ```@<nazwa dekoratora>```.

```python
def zwykłaFunkcja():
    print ("To jest zwykła funkcja")
def dekor(funkcja):
    
    def wew():
        print("Dekorujemy funkcję")
        return funkcja()
        
    return wew
nowaFunkcja = dekor(zwykłaFunkcja)
nowaFunkcja()

#########################################
def dekor(funkcja):
    
    def wew():
        print("Dekorujemy funkcję")
        return funkcja()
        
    return wew
@dekor
def nowaFunkcja2():
    print ("To jest zwykła funkcja")
nowaFunkcja2()
```
