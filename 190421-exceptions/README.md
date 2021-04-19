# Wyjątki i ich obsługa

Pewną trudnością w programowaniu jest zarządzanie błędami. Te mogą pojawić się z różnych przyczyn: nie zrobimy wcięcia (`IndentationError`), pojawiło się dzielenie przez zero (`ZeroDivisionError`) czy próba zamiany litery na liczbę za pomoca rzutowania (`TypeError`). Jak powinna zachować się funkcja, którą piszemy, gdy pojawi się taki problem?

Najczęściej staramy się aby funkcje zawsze zwracały dane tego samego typu, a jeśli przytrafi się nieakceptowalna sytuacja spodziewamy się błędu. Python posiada wiele [wbudowanych rodzajów błędów](https://docs.python.org/3/library/exceptions.html) oraz sposóbów na ich obsługę.

## Stowanie funkcji `assert`

Zzamiast czekać aż program nam się "wysypie" z powodu błędu możemy zastosować funkcję `assert`. Zwyczajowo wprowadza się ją na samym początku ciała funkcji podając w nawiasach warunki, jakie muszą spełnić jej argumenty. Liczba assertów jest dowolna.
Dodatkowo możemy zdefiniować komunikat, który będzie się wyświetlał, gdy warunek nie zostanie spełniony (a program się "wysypie" pokazując znany `AssertionError`).

```python
def dzielenie(a, b):
    # assert(b != 0)  # sparwdzamy dane wejściowe -- argumenty funkcji
    assert(b != 0), "Nie dzielimy przez 0!"  # sparwdzamy z komunikatem
    return a/b

# Tu możemy spodziewać się błędu postaci
# AssertionError: "Nie dzielimy przez 0!"
```

## Rzucanie wyjątkami (błędami)

W odniesieniu do wyjątków gdy pojawia się błąd i chcemy o tym poinformować mówimy, że rzucamy wyjątek (ang. raise an exception). Następnie, w innej partii kodu, gdzie będziemy obsługiwać sytuację wyjątkową, mówimy, że łapiemy wyjątek.
Aby rzucić wyjątkiem możemy skorzystać z polecenia `raise`.

```python
x = 10
if x > 5:
    raise Exception('x powinno być mniesze nić 5! Podałeś {}'.format(x))

# Tu możemy spodziewać się błędu postaci
# Exception: "x powinno być mniesze nić 5! Podałeś 10"
```

## Bloki `try` i `catch`

Bloki `try` i `catch` są używane aby obsłużyć napotykane wyjątki. Gdy spodziewamy się, że dany fragment kodu może rzucać wyjątkami, opakowujemy go w konstrukcję `try-except`. Kod, który chcemy wykonać, a który może rzucić wyjątek, zapisujemy w ciele `try:`. Po nim musi wystąpić, `except` i opcjonalnie nazwę klasy wyjątku oraz `as` i nazwa zmiennej, do której chcemy się odnosić podając komunikaty tego wyjątku (przydaje się, gdy np. chcemy wyświetlić komunikat błędu na konsoli). Listę wbudowanych klas wyjątków znajdziemy pod tym [adresem](https://docs.python.org/3/library/exceptions.html). Możemy dopisywać dowolną liczbę typów wyjątków, jakie chcemy wyłapać, również najbardziej ogóle (bez podawania klasy).

```python
try:
    liczba = int(input("Podaj liczbę: "))
except ValueError as error:  # jeśli nie będzie to coś co da się zamienić na liczbę całkowita mamy ValueError
    print(error, "Podałeś złe dane!")  # drukujemy komunikat dla tego typu błędu i 'Podałeś złe dane!'
except:  # jeśli nie będzie to coś co da się zamienić na liczbę całkowita mamy ValueError
    print("Coś jest nie tak!")  # drukujemy komunikat dla tego typu błędu i 'Podałeś złe dane!'

# Tu możemy spodziewać się błędu postaci
# invalid literal for int() with base 10: 'a' Podałeś złe dane! przy ValueError
# lub "Coś jest nie tak!" przy błędzie innym niż ValueError
```

Jeśli chcemy wykonać kod, gdy instrukcje umieszczone w bloku `try` nie rzucą wyjątku możemy skorzystać z konstrukcji `try-except-else`.

```python
try:
    liczba = int(input("Podaj liczbę: "))
except ValueError as error:  # jeśli nie będzie to coś co da się zamienić na liczbę całkowita mamy ValueError
    print(error, "Podałeś złe dane!")  # drukujemy komunikat dla tego typu błędu i 'Podałeś złe dane!'
else:  # wejdziemy tu jeśli nie będzie błędu ValueError
    print("Poprawnie wpisałeś dane!")  # drukujemy komunikat jeśli wszystko poszło zgodnie z planem

# Tu możemy spodziewać się błędu postaci
# invalid literal for int() with base 10: 'a' Podałeś złe dane! przy ValueError
# lub "Poprawnie wpisałeś dane!" przy braku błędu
```

Na koniec dodajmy, że istnieje jeszcze konstrukcja `try-except-finally`. `finally` służy do zdefiniowania kodu, który ma się wykonać na końcu zawsze, zarówno wtedy, gdy kod wykonał się poprawnie, jak i niepoprawnie. Możliwe jest tworzenie własnych klas wyjątków, ale robi się to niezmiernie rzadko i wymaga znajomości programowania obiektowego (tworzenia klas).
