# Operowanie na napisach - ciąg dalszy

Często będziemy szukać w napisach pewnych wyrażeń według pewnego wzorca, np. kodu pocztowego, który w Polsce składa się z:
`cyfra cyfra - cyfra cyfra cyfra`
Wyrażenia regularne (ang. regular expression, w skrócie regex lub regexp), to właśnie sposób na opisanie wzorca dla tego typu łańcuchów znaków.
Regexy stosowane są w wielu różnych językach programowania.

## Moduł `re`

Aby wyszukać jakiejś sekwencji w łańcucu znaków korzystaliśmy z dwóch metod: `find` oraz `index`.
Podstawowa różnica między nimi polega na odmiennym zachowaniu, gdy nie znalezony zostanie poszukiwany łańcuch - metoda `find` zwróci -1,
podczas gdy metoda `index` rzuci błędem.

```python
s = 'foo123bar'
s.find('123')   # 3
s.index('123')  # 3
```

Jednak w przypadku bardziej skąplikowanych zapytań, warto poznać wyrażenia regularne. 
Istnieje wiele notacji, które służą zapisywaniu wyrażeń regularnych i jedną z nich jest notacja Pythona. 
Aby skorzystać z narzędzi jakie one nam oferują, wystarczy zaimportować [moduł `re`](https://docs.python.org/3/library/re.html).
My głównie skupimy się na funkcji `search` z tego modułu, która przeszukuje dany napis (podany jako drugi argument), 
pod kątem zadanego wzorca (podany jako pierwszy argument).

```python
import re # import całej biblioteki
re.search('wzorzec', 'łańcuch znaków')

from re import search # import jedynie jednej metody
search('wzorzec', 'łańcuch znaków') # w przypadku powyższego importu nie trzeba pisac nazwy modułu
```

Funkcja `search` zwraca specjalny obiekt. Posiada on pole `span`, które mówi, od którego do którego indeksu rozpościera się wyszukiwana fraza 
(a dokładniej pierwsza napotkana fraza pasująca do zadanego wzorca),
oraz `match` przechowujące łańczuch znaków, którey udało się odszukać. Jeśli nie został znaleziony żaden pasujący napis zwracany jest `None`.

```python
s = 'foo123bar'

# importujemy całą bibliotekę
import re

znaleziony = re.search('123', s)  # <_sre.SRE_Match object; span=(3, 6), match='123'> 

# bezpieczniej jest sprawdzić czy cokolwiek zostało znalezione
if znaleziony:  # jeśli nic nieznaleziono, mamy None, więc przejdziemy do else
    print(znaleziony.group())  # pozwala na wypisanie jedynie zanlezionego dopasowania, nie może zostać wykonany na None (błąd!)
else:
    print('No match.')
```

Możemy także skorzystać z funkcji `findall`, która zwróci listę wszystkich łańcuchów znaków, które będa pasowały do zadanego wzorca.

```python
import re

string = 'hello 12 hi 89. Howdy 34'

# tutaj zaczynamy prawdziwą zabawę, \d oznacza cyfrę, a +, że poprzedzaj¡cy go znak/ciąg znaków musi wystąpić co najmniej raz
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']
```

## Fromułowanie wzorców - metaznaki

Poszukiwane wzorce mogą odpowiednio składać się z cyfr i/lub liter w odpowiednim ułożeniu.
Aby je znaleźć można posłuzyć się specjalnymi znakami. Poniżej wymienię kilka z nich.
Po pierwsze - pojedyncza kropka `.`. We wzorcu zastępuje ona jeden, dowolny znak, 
który nie jest znakiem nowego wiersza (literę, cyfrę, spację itp.)

```python
s = 'sinson'

print(re.search('s.n', s))  # znajdzie 'sin', gdyż jest to pierwszy łańcuch, który pasuje do schematu 
```

Inne ważne znaki to:

- znak `?` - poprzedzający go znak/ciąg znaków może wystąpić zero lub jeden raz
- znak `*` - poprzedzający go znak/ciąg znaków może wystąpić zero lub dowolna liczbę razy
- znak `+` - poprzedzający go znak/ciąg znaków musi wystąpić co najmniej raz

```python
s1 = 'kwiat'
s2 = 'kwit'
s3 = 'kwiaat'

print(re.search('kwia?t', s1))  # pasuje do schematu
print(re.search('kwia?t', s2))  # pasuje do schematu
print(re.search('kwia?t', s3))  # nie pasuje do schematu, słowo nie zostanie znalezione -- None

print(re.search('kwia+t', s1))  # pasuje do schematu
print(re.search('kwia+t', s2))  # nie pasuje do schematu
print(re.search('kwia+t', s3))  # pasuje do schematu

print(re.search('kwia*t', s1))  # pasuje do schematu
print(re.search('kwia*t', s2))  # pasuje do schematu
print(re.search('kwia*t', s3))  # pasuje do schematu
```

Znaki umieszczone w nawiasie kwadratowym `[]` we wzorcu oznaczają, że program będzie próbował po kolei dopasować
wszystkie elementy znajdujące się w nawiasie. Można w ten sposób podawac także zakresy.

```python
import re

re.search('[0-9][0-9][0-9]', 'foo456bar') # tutaj szukamy łańcucha składajacego się z 3 dowolnych cyfr występujących po sobie
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('[abc]xyz', 'foobxyz') # ten wzorzec spróbuje odnaleźć zarówno axyz, bxyz, jak i cxyz
# <_sre.SRE_Match object; span=(3, 7), match='bxyz'>

re.search('a-h1-4', 'aabcdefgh1234') # ten wzorzec oznacza dokładnie abcdefgh1234
# <_sre.SRE_Match object; span=(1, 13), match='abcdefgh1234'>
```

Aby ułatwić sobie zadanie sformułowano pewne klasy znaków za pomocą odpowiednich kodów.
| Kod | Klasa znaków   | Znaczenie  |
| :-: | :------------: | :--------: |
| \d  |`[0-9]`         | dowolna cyfra |
| \D  |`[^0-9]`        | dowolny znak, który nie jest cyfrą |
| \w  |`[0-9a-zA-Z]`   | dowolna litera lub cyfra |
| \W  |`[^0-9a-zA-Z]`  | dowolny znak, który nie jest cyfrą bądź literą |
| \s  |`[\t\n\r\f]`    | dowolny biały znak (spacja, tabulator, koniec lini itp.) |
| \S  |`[^\t\n\r\f]`   | dowolny znak, który nie jest białym znakiem |

W przypadku długich ciągów można stworzyć wzorzec, określajacy liczbę wystąpień korzystając z `{}`.

```python
import re

re.search('[0-9][0-9][0-9]', 'foo456bar') # tutaj szukamy łańcucha składajacego się z 3 dowolnych cyfr występujących po sobie
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('\d\d\d', 'foo456bar') # tutaj także szukamy łańcucha składajacego się z 3 dowolnych cyfr występujących po sobie
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('\d{3}', 'foo456bar') # i tu też szukamy łańcucha składajacego się z 3 dowolnych cyfr występujących po sobie
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('\d{3, 6}', 'foo456bar') # w ten sposób szukamy od 3 do 6 cyfr
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('\d{3, }', 'foo456bar') # znajdź przynajmniej 4 cyfry
# <_sre.SRE_Match object; span=(3, 6), match='456'>
```

Więcej na temat wyrażeń regularnych i ich funkcji z modułu `re` znajdziesz w [Dokumentacji](https://docs.python.org/3/library/re.html).

# Wprowadzenie do algorytmów sortujących w pythonie

Python posiada dwie główne funkcje, które umożliwiają sortowanie list.
Jedna z nich jest metoda `list.sort()`, która pozwala na posortowanie listy w miejscu (bez tworzenia nowego obiektu),
a drugą funkcja `sorted()`, która sortuje listę podaną jako argument i tworzy nowy obiekt - posortowaną listę.

```python
a = [5, 2, 3, 1, 4]
b = sorted([5, 2, 3, 1, 4])
print(b)  # [1, 2, 3, 4, 5]
print(a)  # [5, 2, 3, 1, 4]

a.sort()
print(a)  # [1, 2, 3, 4, 5]
```

W obu przypadkach znajdziesz dwa argumenty domyślne: `key` (pozwala podać funkcję określajacą nietypowy sposób sortowania obiektów) oraz `reverse` (pozwala na sortowanie malejące).

```python
a = [5, 2, 3, 1, 4]
b = sorted([5, 2, 3, 1, 4], reverse=True)
print(b)  # [5, 4, 3, 2, 1]
print(a)  # [5, 2, 3, 1, 4]

a.sort(reverse=True)
print(a)  # [5, 4, 3, 2, 1]

a = ['Harry', 'Ron', 'Hermiona']
a.sort(key=len)  # posortujemy nie leksykograficznie, ale ze wzlędu na liczbe liter w napise
print(a)  # ['Ron', 'Harry', 'Hermiona']
```

Więcej o metodzie `sort` i funkcji `sorted` znajdziesz w [Dokumentacji](https://docs.python.org/3/howto/sorting.html).

## Ocena złożoności algorytmu

Teoria obliczeń to dział informatyki. Jedną z gałęzi tego działu jest teoria złożoności obliczeniowej. W uproszczeniu można powiedzieć, że zajmuje się ona oszacowaniem wydajności czasowej i pamięciowej algorytmów. Teoria złożoności obliczeniowej bazuje na wielu modelach, które służą do łatwego porównywania algorytmów. Złożoność obliczeniową określamy jako funkcję danych wejściowych algorytmu. Notacja `Ο` jest najczęściej spotykana do określania złożoności algorytmów. Jest to oszacowanie z góry, zatem jeśli algorytm ma złozoność O(n<sup>2</sup>) to ma także złozoność O(n<sup>3</sup>) - jednak O(n<sup>2</sup>) może być najlepszym oszacowaniem złożoności danego algorytmu. Możesz sobie wyobrazić, że w przypadku algorytmów sortujących, dany zapis mówi o tym, że przy dołożeniu kolejnych elementów do sortowanej tablicy (listy czy też krotki) czas wykonywania się algorytmów wzrośnie kwadratowo.

Więcej na temat notacji Dużego O znajdziecie [TUTAJ](https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/).

## Sortowanie bąbelkowe

Prosta metoda, która polega na porównywaniu dwóch kolejnych elementów i zamianie ich kolejności, jeżeli zaburza ona porządek, w jakim się sortuje tablicę. Sortowanie kończy się, gdy podczas kolejnego przejścia nie dokonano żadnej zmiany. Do jej wykonania potrzebujemy dwóch pętli:

- pierwsza posłuży do porównywania parami sąsiadujących elementów i w razie potrzeby zamiany ich kolejności,
- druga pozwoli na przejście przez tablice kolejny raz, gdy juz jeden z elementów (ostatni badanego wycinka tablicy) zostanie dobrze ustawiony.

Aby zwizualizować sobie tę metodę zajrzyj do filmu: [LINK](https://www.youtube.com/watch?v=lyZQPjUT5B4&ab_channel=AlgoRythmics).

## Sortowanie przez wybór

Prosta metoda, która polega na znajdowaniu minimalnego elementu zbioru i przesuwaniu go na początek tablicy. W kolejnych krokach minimalny element jest wyszukiwany spośród wycinka tablicy - bez ustawionych już elementw minimalnych znalezionych w poprzednich krokach.

Aby zwizualizować sobie tę metodę zajrzyj do filmu: [LINK](https://www.youtube.com/watch?v=Ns4TPTC8whw&ab_channel=AlgoRythmics).

## Sortowanie przez wstawianie

Ta metoda polega na wyciaganiu kolejno elementów ze zbioru i wstawianie ich na właściwą pozycję. To znaczy, że idziemy od elementu drugiego porównujemy go z pierwzym i jeśli jest mniejszy zamieniamy je miejscami. Potem idziemy do elementu trzeciego i porównujemy go z drugim, jeśli jest mniejszy zamieniamy je miejscami, a następnie porównujemy dany element (wcześniej umiejscowionym na trzeciej pozycji) z kolejnym - pierwszym na liście (obecnie najmniejszym). Takiego szeregu porównań dokonujemy tak długo, aż przejdziemy do końca tablicy - czyli aż do jej posortowania.

Aby zwizualizować sobie tę metodę zajrzyj do filmu: [LINK](https://www.youtube.com/watch?v=ROalU379l3U&ab_channel=AlgoRythmics).
