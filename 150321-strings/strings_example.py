"""
Napisz program, w którym:
- znajdziesz liczbę unikalnych znaków w zdaniu wprowadzonym przez uzytkownika
- sprawdzisz czy owo zdanie jest palindromem
- pozwolisz uzytkownikowi wprowadzić kolejne wyrażenia i sprawdzisz czy jest ono anagramem pierwszego
"""

def ispalindrom(text1):
    return text1.replace(" ", "").lower() == text1.replace(" ", "").lower()[::-1]

def isanagram(text1, text2):
    return sorted(text1.replace(" ", "").lower()) == sorted(text2.replace(" ", "").lower())

def main():
    n1 = input("Podaj napis: ")

    print(f'W tym stwierdzeniu zawarto {len(set(n1.lower()))} unikalnych znaków.')

    if ispalindrom(n1):
        print("To stwierdzenie jest palindromem!")
    else:
        print("To stwierdzenie nie jest palindromem!")
    
    n2 = input("Podaj drugi napis: ")
    if isanagram(n1, n2):
        print("Te stwierdzenia są anagramami!")
    else:
        print("Te stwierdzenia nie są anagramami!")

if __name__ == '__main__':
    main()
