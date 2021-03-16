'''
Dwa ciągi znaków nazywamy anagramami jeśli zawierają dokładnie takie same
litery w tej samej ilości (ignorujemy wszelkie inne znaki takie jak cyfry, znaki interpunkcyjne, itd.).
Nie rozróżniamy wielkości liter. Na przykład: William Shakespeare oraz I am a weakish speller są
anagramami podczas gdy Anna oraz na nie są (zob. też https://pl.wikipedia.org/wiki/Anagram).
Napisz funkcję, która dla podanych dwóch napisów orzeknie czy są one anagramami
'''
def is_anagram(string1, string2):
    if sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower()):
        return True
    return False


def main():
    s1 = input("Podaj pierwszą sentencję: ")
    s2 = input("Podaj drugą sentencję: ")
    if is_anagram(s1, s2):
        print("Te sentencje są anagramami.")
    else:
        print("Te sentencje nie są anagramami.")

if __name__ == '__main__':
    main()
