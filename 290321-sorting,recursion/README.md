# Algorytmy sortujące w pythonie - ciąg dalszy

Na tej lekcji zajmiemy się trochę bardziej skomplikowanymi, ale i wydajniejszymi czasowo (przynajmniej dla dwóch pierwszych metod) algorytmami sortującymi.
Jednak najpierw zapoznamy się z podstawowym pojęciem w programowaniu - rekursją, znaną także pod nazwą rekurencja.

## Koncepcja rekurencji

Rekurencja jest jednym ze sposóbów rozwiązania problemu, zakładając, że możemy go rozbić na coraz to mniejsze części, aż dojdziemy do takiego punktu, 
w którym problem będzie tak niewielki, iz będzie go można rozwiązać z łatwością.

Sprowadza to nas do napisania funkcji (rekurencyjnej), która będzie wywoływać samą siebie. W ogólności zakładamy, że:

- znamy problem bazowy i jego proste rozwiązanie,
- jesteśmy w stanie rozbić główne zadanie na mniejsze, dochodząc do problemu bazowego,
- wywołujemy w ciele funkcji ją samą.

Najbardziej modelowym zadaniem jest obliczanie silni.

![](rekurencja.png)

```python
# definicja funkcji iteracyjnej
def silnia_iteracyjnie(x) :
    silnia = 1
    for i in range(1, x+1):
        silnia *= i
    return silnia

# definicja funkcji rekurencyjnej
def silnia_rekurencyjnie(x) :
    if x < 1 :
        return 1
    else :
        return x * silnia_rekurencyjnie(x - 1)

print(silnia_iteracyjnie(5))
print(silnia_rekurencyjnie(5))
```

Rodzajem rekurencji, w której ostatnia operacja wykonywana przez funkcję to rekurencyjne wywołanie samej siebie lub zwrócenie wyniku nazywane 
jest rekurencją ogonową.

![](ogonowa.png)

```python
def silnia_ogonowa(n, accumulator=1):
  if n == 0: return accumulator
  else: return silnia_ogonowa(n-1, accumulator * n)
```

## Płytka, a głęboka kopia

Zanim przejdziemy do sortowania, zatrzymajmy się na chwilę na omówieniu kopi w pythonie.
Zmienna (w każdym języku programowania) jest aliasem (nazwą) na miejsce w pamięci komputera.
W przypadku list (i nie tylko, tyczy się to także innych złożonych obiektów) możemy stworzyć obiekty, 
które będą przechowywane w tym samym miejscu w pamięci.
Do sprawdzenia adresu służy funkcja ```id()```.

```python
a = [1, 2, 3, 4, 5]
b = a

id(a) == id(b)  # True

# możesz je sobie nawet wypisać, będa to bardzo duże liczby
print('id of a - {}, id of b - {}'.format(id(a), id(b)))
```

Różnica między kopiowaniem płytkim i głębokim jest istotna szczególnie istotna w przypadku obiektów złożonych 
(obiektów zawierających inne obiekty, takich jak listy lub instancje klas).

### Płytka kopia

To co stworzyliśmy powyżej jest płytką kopią (*shallow copy*) obiektu, najłatwiej się będzie o tym przekonać modyfikując element jednej z list.

```python
b.append(6)

# mimo iż nie modyfikowaliśmy a to ten obiekt też się powiększył o jeden element
print(a)  # [1, 2, 3, 4, 5, 6]
print(b)  # [1, 2, 3, 4, 5, 6]
```

Teraz przechodzimy do bardziej interesującej części. Jeśli oryginalna lista jest obiektem złożonym (np. Lista list), to po płytkiej kopii nowe elementy listy nadal odwołują się do oryginalnych elementów. Tak więc, jeśli zmodyfikujesz zmienne elementy, takie jak listy, zmiany zostaną odzwierciedlone w oryginalnych elementach.

```python
a = [[1, 2], [3, 4]]
b = list(a)

id(a) == id(b)  # False, jeśli chodzi o umiejscowienie list w pamięci

b[0][1] = 'x'
# mimo iż nie modyfikowaliśmy a to ten obiekt też się zmienił
print(a)  # [[1, 'x'], [3, 4]]
print(b)  # [[1, 'x'], [3, 4]]
```

Jak widać w powyższym przykładzie, podczas gdy modyfikujemy wewnętrzne elementy listy w nowej liście, 
jest ona również aktualizowana na oryginalnej liście, ponieważ ```a[0]``` i ```b[0]``` nadal wskazuje ten sam adres pamięci (oryginalna lista).
Tak więc nowa lista ```b``` ma swój własny adres pamięci, ale jej elementy nie. Dzieje się tak dlatego, że w płytkiej kopii, zamiast kopiować elementy listy do nowego obiektu, po prostu kopiuje odwołania do ich adresów pamięci. 
Dlatego gdy wprowadzamy zmiany w oryginalnym obiekcie, jest to odzwierciedlane w skopiowanych obiektach i odwrotnie.
Jest to cecha charakterystyczna dla płytkiej kopii.

### Głęboka kopia

Głęboka kopia (*deep copy*) tworzy nowy obiekt złożony, a następnie rekurencyjnie wstawia do niego kopie obiektów znalezionych w oryginale. 
Tworzenie głębokiej kopii jest wolniejsze, ponieważ tworzysz nowe kopie wszystkiego. W tym przypadku, zamiast tylko kopiować 
adresy obiektów złożonych, po prostu tworzy pełną kopię wszystkich elementów listy (obiektów prostych i złożonych) oryginalnej listy i przydziela inny adres pamięci dla nowej listy, a następnie przypisuje im skopiowane elementy.

Aby uzyskać głęboką kopię, musimy zaimportować moduł ```copy``` i użyć funkcji ```deepcopy()```.

```python
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)  # deep copy

b[0][1] = 'x'
# teraz lista a nie ulegnie zmianie
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 'x'], [3, 4]]
```

## Sortowanie przez scalanie

Rekurencyjny algorytm sortowania danych wymagający zarezerwowania dodatkowego miejsca w pamięci. Polega na sekwencyjnym dzieleniu tablicy na 
dwie części aż do dojścia do części niepodzielnej (jednego elementu). Następnie następuje sortowanie przez scalenie (złożenie) każdej 
z tych cześci odzielnie i połączeniu posortowanych podciągłów w jedną posortowana tablicę.

Aby zwizualizować sobie tę metodę zajrzyj do filmu: [LINK](https://www.youtube.com/watch?v=XaqR3G_NVoo&ab_channel=AlgoRythmics).

## Sortowanie szybkie

Szybki i prosty w implementacji algorytm sortowania, najczęściej stosowany. Polega na wyborze jednego elementu rozdzialejącego (*pivota*), 
na podstawie, którego tablica jest dzielona na dwie cześci: do pierwszej przenoszone są wszystkie elementy nie większe od pivota, 
a do drugiego wszystkie elementy większe. Potem sortuje się osobno początkową i końcową część tablicy. Rekursja kończy się, 
gdy kolejny fragment uzyskany z podziału zawiera pojedynczy element, jako że jednoelementowa tablica nie wymaga sortowania.

Aby zwizualizować sobie tę metodę zajrzyj do filmu: [LINK](https://www.youtube.com/watch?v=ywWBy6J5gz8&ab_channel=AlgoRythmics).

## Bogosort - (nie)ciekawe podejście do sortowania

Trywialny w działaniu algorytm sortowania o bardzo dużej złożoności obliczeniowej, oparty na metodzie prób i błędów. Jego idea jest prosta - losujemy ustawienie elementów tablicy tak długo aż nie zostaną posortowane. Nie jest używany w praktyce – posortowanie kilkunastu elementów 
może trwać bardzo długo i nie ma pewności, czy w ogóle się zakończy.
