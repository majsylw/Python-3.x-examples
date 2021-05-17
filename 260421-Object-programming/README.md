# Programowanie obiektowe

System typów w Pythonie jest silnie powiązany z systemem klas. Chociaż typy wbudowane nie są właściwie klasami, klasa może dziedziczyć z dowolnego typu. Można więc dziedziczyć klasy z napisów czy słowników, a nawet z liczb całkowitych. Ponadto możliwe jest dziedziczenie wielokrotne.

## Krok pierwszy: definicja klasy

Tworzenie klas w Pythonie jest proste. Podobnie jak z funkcjami, nie używamy oddzielnego interfejsu definicji. Po prostu definiujemy klasę i zaczynamy ją implementować. Klasa w Pythonie rozpoczyna się słowem kluczowym class, po którym następuje nazwa klasy, a następnie w nawiasach okrągłych umieszczamy, z jakich klas dziedziczymy.

```python
class Klasa:          # Nazwa tej klasy to Klasa - konwencjaL nazwy są zazwyczaj pisane przy użyciu wielkich liter
    pass              # Klasa ta nie definiuje żadnych metod i atrybutów, ale żeby kod był zgodny ze składnią Pythona,
                      # musimy coś umieścić w definicji, tak więc użyliśmy pass

class FileInfo(dict): # klasy po których dziedziczymy (przechwytujemy zdefiniowane dla nich metody)
    pass              # wyszczególniamy w nawiasach okrągłych, tutaj dziedziczymy po dict (słowniku)
```

## Krok drugi: konstruktor

Teraz omówmy, czym jest konstruktor. Jest to taka specjalna funkcja, która jest wywoływana, gdy obiekt jest tworzony. Jej celem jest zainicjowanie pól (czyli danych przechowywanych dla danego obiektu) w instancji. Dla poniższego przykładu jest to przypisanie podanych jako parametry wartości x oraz y do odpowiednich pól w klasie. Konstruktor poznajemy po jego specjalnej nazwie `__init__`. Konstruktor jest wywoływany poprzez podanie nazwy klasy, a następnie jej argumentów (bez `self`!). Jeżeli chcemy zmienić jakiś parametr (pole) naszej instancji wystarczy, że podamy jej nazwę, wpiszemy kropkę `.` i następnie nazwę konkretnego pola (lub metody, o czym za chwilę).

```python
class Point:
    # konstruktor
    def __init__(self, x, y):
        self.x = x  # pole klasy: x
        self.y = y  # pole klasy: y

if __name__ == '__main__':
    zmienna = Point(2, 3)  # wywołanie konstruktora -- tworzymy obiekt klasy Point
    print(zmienna.x, zmienna.y)  # drukujemy odpowiednie pola na ekran (ich wartości)
    zmienna.x = 5
    print(zmienna.x, zmienna.y)  # drukujemy odpowiednie pola na ekran po zmianie ich wartości
```

Podczas definiowania funkcji należących do pewnej klasy, musimy wyraźnie wstawić `self` jako pierwszy argument każdej takiej definicji, włączając w to `__init__`. Kiedy wywołujemy funkcję z klasy nadrzędnej, musimy dołączyć argument `self`. Tworzenie instancji klas jest dosyć proste - w tym celu wywołujemy klasę tak jakby była funkcją, dodając odpowiednie argumenty, które są określone w metodzie `__init__`. Zwracaną wartością będzie zawsze nowo utworzony obiekt.

## Krok drugi: destruktor

Przyszedł czas na omówienie kolejnej funkcji specjalnej - destruktora. Destruktor to metoda analogiczna do konstruktora, której kod wykonuje się, gdy pozbywamy się danego obiektu (poniżej w kodzie main() wymusiliśmy jej wywołanie poprzez przypisanie wartości None do zmiennej przechowującej dany obiekt).

```python
class Point:

    # konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # destruktor, czyli kod, który wykonuje się
    # podczas niszczenia obiektu
    def __del__(self):
        class_name = self.__class__.__name__
        print("Usunięto obiekt:", class_name)

if __name__ == '__main__':
    zmienna = Point(2, 3)  # wywołanie konstruktora -- tworzymy obiekt klasy Point
    print(zmienna.x, zmienna.y)  # drukujemy odpowiednie pola na ekran (ich wartości)
    zmienna = None  # niszczymy obiekt Point (nawet bez tego zostałby zniszczony wraz z końcem działania programu)
    print("Koniec!")
```

## Krok trzeci: metody

Metoda to zwykła funkcja - jednak, ponieważ jest ona definiowana w ciele klasy, powiemy, że jest to metoda. Możemy poznać, że to metoda, także po pierwszym argumencie: `self`. W języku Python metody przyjmują jako pierwszy parametr obiekt, na rzecz którego są wywoływane. W samym wywołaniu nie musimy go sami podawać. Wystarczy, że metoda jest napisana po kropce. Następnie podajemy kolejne argumenty. Tutaj możemy zaznaczyć, że konstruktor i destruktor to tez takie specjalne metody klasy. Dopiszymy do naszej klasy metodę `prosta` wyliczającą nową warość y na podstawie podanych parametrów prostej ( wyraz wolny b oraz kierunkowy a) oraz pewną metodę specjalną `__str__`, która będzie mówiła co ma się wydarzyć po wywołaniu funkcji `print` na danym obiekcie.

```python
class Point:

    # konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # destruktor
    def __del__(self):
        class_name = self.__class__.__name__
        print("Usunięto obiekt:", class_name)

    # metoda -- tu akurat wyliczamy wartość y na podstawie równania prostej
    def prosta(self, a, b):
        self.y = self.x * a + b

    # przeciążenie operatora wypisywania na ekran --- funkcja print
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
if __name__ == '__main__':
    zmienna = Point(2, 3)
    print("Przed: ")
    print(zmienna.x, zmienna.y)
    zmienna.prosta(2, 2)
    print(zmienna.y)
    print(zmienna)
```

## Krok czwarty: Metody statyczne

Do tej pory omawialiśmy takie pola i metody, do których, by się odwołać, trzeba było stworzyć konkretny obiekt danej klasy. Teraz pokażemy, jak stworzyć metodę lub pole, które jest jedno na całą klasę. Taką metodę lub pole nazywamy statycznym. Tutaj warto przed definicją takiej metody odpowiednio ją oznaczyć - korzystamy z dekoratora `@staticmethod`. Dekoratory (zaczynające się od `@)` służą do modyfikacji definiowanej funkcji lub metody w określony sposób, jednak nie będziemy tutaj temu zagadnieniu poświęcać więcej uwagi. W metodach statycznych argument `self` nie wystęstępuje - oprócz tego, że ich deficnicja znajduje się w klasie, wygląda jak zwykła definicja funkcji. Różni się wywołaniem, gdyż aby skorzystać z metody statycznej nie musimy tworzyć obiektu danej klasy - wpisujemy po prostu nazwę klasy, potem kropkę `.` i następnie nazwę metody statycznej z jej argumentami.

```python
class Point:

    # konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # destruktor
    def __del__(self):
        class_name = self.__class__.__name__
        print("Usunięto obiekt:", class_name)

    # metoda -- tu akurat wyliczamy wartość y na podstawie równania prostej
    def prosta(self, a, b):
        self.y = self.x * a + b
    
    # metoda statyczna
    @staticmethod
    def sumuj(p1, p2):
        wynik = Point(p1.x + p2.x,
                      p1.y + p2.y)
        return wynik

    # przeciążenie operatora wypisywania na ekran --- funkcja print
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
if __name__ == '__main__':
    zmienna = Point(2, 3)
    print("Przed: ")
    print(zmienna.x, zmienna.y)
    zmienna.prosta(2, 2)
    print(zmienna.y)

    # wypisywanie na ekran
    print(zmienna)
    print(Point(zmienna, zmienna))  # wykorzystujemy metodę statyczną
```
