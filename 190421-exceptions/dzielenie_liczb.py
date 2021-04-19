def dzielenie(a, b):
    # assert(b != 0)  # sparwdzamy dane wejściowe -- argumenty funkcji
    assert(b != 0), "Nie dzielimy przez 0!"  # sparwdzamy z komunikatem
    return a/b

if __name__ == '__main__':
    try:
        liczba1 = int(input("Podaj liczbę: "))
        liczba2 = int(input("Podaj liczbę: "))
    except ValueError as error:  # jeśli nie będzie to coś co da się zamienić na liczbę całkowita mamy ValueError
        print(error, "Podałeś złe dane!")  # drukujemy komunikat dla tego typu błędu i 'Podałeś złe dane!'

    try:
        # tutaj zamieszczamy sprawdzany kod
        print("Zaraz wykonam dzielenie")
        print(dzielenie(liczba1, liczba2))
    except TypeError as error:  # możemy wyszczególnić różne typy błędu
        print(error, "Tutaj TypeError", error)
    except IndexError as error:
        print("Tutaj IndexError", error)
    except AssertionError as error:
        print("Tutaj AssertionError", error)
    except IndentationError as error:
        print("Tutaj IndentationError", error)
    except:  # albo nie wyszczególniać ich wcale, tu wejdziemy jeśli jest błąd innego typu niż powyższe
        print("Bląd!")
    else:  # ta część się wykona jeśli nie było błędu
        print("Jest ok!")
    finally:  # ta część się wykona zawsze -- niezaleznie od tego czy błąd był czy też nie
        print("Nie wiem co się stało, ale jestem tutaj!")
