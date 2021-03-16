# Operowanie na napisach

Już poznałeś operatory `+` i `*`, czas zobaczyć jak będa się one zachowywać dla napisów.

## Operator konkatenacji

Operator `+` łączy ze sobą dwa łańcuchy znaków.

```python
s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)  # 'foobar'
print(s + t + u)  # 'foobarbaz'

print('Go team' + '!!!')  # 'Go team!!!'
```

## Operator replikacji

Operator `*` tworzy odpowiednią liczbę kopii łańcucha znaków.
Jak to operator mnożenia jest to operacja przemienna.

```python
s = 'foo.'

print(s * 4)  # 'foo.foo.foo.foo.'
print(4 * s)  # 'foo.foo.foo.foo.'
```

Liczba przez która mnożymy napis musi być całkowita.
Zaskakująco może to być 0 lub liczba ujemna, co zaskutkuje utworzeniem pustego napisu.

```python
print('foo.' * 0)  # ''
print('foo.' * -1)  # ''
```

## Operatory przynależności

Dla łańcucha znaków (jak dla każdej kolekcji) możemy skorzystać z operatorów
`in` oraz `not in`, aby sprawdzić czy jakiś znak lub sekwencja, do niego należy.

```python
print('a' in 'abc')  # True
print('z' not in 'xyz')  # False
```

## Podstawowe funkcje wbudowane

| Funkcja | Opis                                              | Użycie               |
| :-----: | :-----------------------------------------------: | :------------------: |
| chr()   |Zamienia liczbę całkowitą na znak (kodowanie ASCI) | ```chr(65)  # 'A'``` |
| ord()   |Zamienia znak na liczbę całkowitą (kodowanie ASCI) | ```ord('A')  # 65``` |
| len()   |Zwraca liczbę całkowitą reprezentującą liczbę znaków w łańcuchu | ```len('Ala')  # 3``` |
| str()   |Zwraca napis (np. konwersja z liczby całkowitej)   | ```str(65)  # '65'```|

## Indeksowanie łańcucha znaków

Aby dobrać się do poszczególnych składowych łańcucha znaków (poszczególnych znaków) korzystamy z `[]`.
Indeksowanie w pythonie rozpoczyna się od zera.
Jeśli chcesz poznać końcowe znaki łańcucha rozpoczynasz iterowanie od -1.

Próba wzięcia litery spoza dopuszczalnej liczby znaków poskutkuje błędem. Podobnie jak próba podmiany liter na inną.

```python
s = 'foobar'
print(s[0])  # 'f'
print(s[1])  # 'o'
print(s[3])  # 'b'
print(len(s))  # 6
print(s[len(s)-1])  # 'r'
print(s[-1])  # 'r' (to samo co powyżej)
print(s[-2])  # 'a'
print(s[-len(s)])  # 'f'

# Errors
s[6]  # IndexError: string index out of range
s[-7]  # IndexError: string index out of range

s[0] = 'a'  # TypeError: 'str' object does not support item assignment
```

## Wycinanie łańcuchów (ang. slicing)

Korzystając z `[]` oraz `:` możemy wycinać fragmenty z napisów.
Pominięcie liczby przed lub po tym znaku (dwukropku `:`) spowoduje odpowiednio,
rozpocząecie od początku lub dociągniecie do końca. W wyrażeniu moga też pojawić
się 3 liczby co będzie rwónoznaczne z przejściem co krok (co jakakis znak).
Zwrócićie uwagę, że przy wycinaniu pod uwagę nie jest brany ostatni znak dla wycięcia,
co znaczy, że jeśli chcemy wyciąć znaki od 0 do 6, będziemy musieli to zapisać jako `[:7]`.
W ten sposób możemy też próbować stworzyć nowy napis i nadpisac zmienną, skoro nie możemy bezpośrednio
podmienić liter.

```python
s = 'foobar'

print(s[-5:-2])  # 'oob'
print(s[1:4])  # 'oob'
print(s[-5:-2] == s[1:4])  # True

print(s[0:6:2])  # 'foa'
print(s[5:0:-2])  # 'rbo'

print(s[:4])  # 'foob'
print(s[4:])  # 'ar'
print(s[4:4])  # ''

napis = 'If Comrade Napoleon says it, it must be right.'
print(s[::-1])  # '.thgir eb tsum ti ,ti syas noelopaN edarmoC fI'

print(s[:4] + 'o' + s[5:])  # 'foobor'
```

## Podstawowe metody łańcuchów znaków

Różnica między metodą, a funkcją jest taka, że metoda jest powiązana bezpośrednio z obiektem, na którym jest wywoływana.
Przy jej wywołaniu piszemy ```<nazwa obiektu>.<nazwa metody>(<argumenty>)```.
Niech nasz obiekt `s = 'foO BaR 123 BAZ quX'` będzie łańcuchem znaków.

| Metoda  | Opis                                              | Użycie               |
| :-----: | :-----------------------------------------------: | :------------------: |
| `s.capitalize()`   |Zwraca kopię napisu z pierwszą literą zamieniona na wielką, a reszte na małe (liczby ozostawia bez zmian). | ```s.capitalize()  # 'Foo bar 123 baz qux'``` |
| `s.lower()`   |Zamienia wszystkie znaki na małe | ```s.lower()  # 'foo bar 123 baz qux'``` |
| `s.upper()`   |Zamienia wszystkie znaki na duże | ```s.upper()  # 'FOO BAR 123 BAZ QUX'``` |
| `s.swapcase()`   |Zamienia wszystkie małe znaki na duże, a duże na małe | ```s.upper()  # 'fOo bAr 123 baz QUx'``` |
| `s.replace(<sub>, <new_sub>)`   |Zamienia wszystkie sekwencje `<sub>` na `<new_sub>` | ```s.replace(" ", "")  # 'foOBaR123BAZquX'``` |
| `s.count(<sub>[, <start>[, <end>]])`   |Zwraca ile raz dana sekwencja `<sub>` występuje w danym napisie (lub jego wyciętym fragmencie `<start>, <end>`) | ```s.lower().count('ba', 0, 8)  # 1```|
|`s.endswith(<suffix>[, <start>[, <end>]])`|Sprawdza czy łańcuch (lub jego fragment) kończy się odpowiednią sekwencją | `s.endswith('quX') # True`|
|`s.startswith(<suffix>[, <start>[, <end>]])`|Sprawdza czy łańcuch (lub jego fragment) zaczyna się odpowiednią sekwencją | `s.startswith('quX') # False`|
|`s.find(<sub>[, <start>[, <end>]])`|Zwraca indeks, od którego zaczyna się pierwszy raz napotkana dana sekwencja `<sub>` w napisie (lub jego wyciętym fragmencie `<start>, <end>`, jeśli nie ma jej zwróci `-1`); napis przeszukiwany jest od przodu) | ```s.lower().find('a')  # 5```|
|`s.rfind(<sub>[, <start>[, <end>]])`|Zwraca indeks, od którego zaczyna się pierwszy raz napotkana dana sekwencja `<sub>` w napisie (lub jego wyciętym fragmencie `<start>, <end>`), jeśli nie ma jej zwróci `-1`; napis przeszukiwany jest od tyłu) | ```s.lower().rfind('a')  # 13```|
|`s.index(<sub>[, <start>[, <end>]])`|działa podobnie do `.find()`, jednak w przypadku braku sekwencji w napisie zwórci błąd | ```s.lower().find('gra')  # ValueError: substring not found```|
|`s.isalpha()`| Zwróci prawdę jeśli wszystkie znaki w napisie są literami, a napis nie jest pusty | `s.isalpha()  # False`|
|`s.isdigit()`| Zwróci prawdę jeśli wszystkie znaki w napisie są cyframi, a napis nie jest pusty | `s.isdiit()  # False`|

Więcej na temat łańcuchów znaków i ich metod znajdziesz w [Dokumentacji](https://docs.python.org/3/library/stdtypes.html#string-methods).
