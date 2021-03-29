import random
import sys

from timeit import repeat

from numpy import mean

#generuje losowe dane wejsciowe
def losowe(n, a=10, b=30):
    '''
    lst = []
    a = list(range(n))
    for _ in range(n):
        lst.append(random.choice(a))
    '''
    if a < b:
        lst = random.sample(range(a, b), n)
    else:
        sys.exit("Zły zakres!")
    return lst

# sortowanie bąbelkowe
def bubble_sort(list):
    # Zamieniamy elementy miejscami
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

# indeks minimalnego elementu
def smalest_index(myarray):
    '''
    # Zakładamy, że pierwszy element wycinka listy jest minimalny
    smallest_idx = 0
    # Przechodzimy po liście
    for j in range(len(myarray) - 1):
        if myarray[j] < myarray[j + 1]:
            smallest_idx = j
    return smallest_idx
    '''
    return myarray.index(min(myarray)) # bardziej pythonowy sposób ;-)

# sortowanie przez wybór
def select_sort(nums):
    # Iterujemy po wszystkich elementach listy
    for i in range(len(nums)):
        # Przechodzimy po nieposortowanym fragmencie listy
        lowest_value_index = smalest_index(nums[i:])
        # Zamieniemy wartości najmniejszego elementu z nieposortowanej listy oraz oraz bieżącego elementu
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# sortowanie przez wstawianie
def insert_sort(nums):
    # Zaczynamy od drugiego elementu zakładając, że pierwszy jest na dobrym miejscu
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Przechowujemy indeks do poprzedzającego elementu
        j = i - 1
        # Przesuwamy elementy w posortowanym segmencie jeśli są większe niż element do wstawienia
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Wstawiamy element
        nums[j + 1] = item_to_insert

# sortowanie szybkie
def quick_sort(lst): 
    if len(lst) <= 1: 
        return lst
    #pobieranie pivota wg ktorego bedzimey operowac
    pivot = lst[0] # tutaj jako pierwszy element listy
    less = []
    #wszystkie mniejsze elementy od pivot przerzucamy do listy mniejszych
    for x in lst:
        if x < pivot:
            less.append(x)
    #wszystkie rowne elementy przerzucamy do listy rownych
    equal = []
    for x in lst:
        if x == pivot:
            equal.append(x)
    #wszystkie wiesze elementy od pivot przerzucamy do listy wiekszych
    greater= []
    for x in lst:
        if x > pivot:
            greater.append(x)

    #(rekurencja) odnawiamy procedure dla mniejszych i wiekszych elementow
    return quick_sort(less)+equal+quick_sort(greater) 

# Sortowanie przez scalanie
def merge_sort(arr):
    if len(arr) > 1:
        # szukamy połowy tablicy
        mid = len(arr)//2
 
        # dzielimy ją na dwie części
        L = arr[:mid]
        R = arr[mid:]
 
        # sortujemy pierwszą połowę
        merge_sort(L)
        # i drugą
        merge_sort(R)
 
        i = j = k = 0
 
        # Kopiujemy dane z tablic L[] i R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # sprawdzamy, czy wszystko zostało zrobione
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# sortowanie bogosort
def bogo_sort(a):
    while (is_sorted(a)== False):
        shuffle(a)
  
# Sprawdzamy czy lista jest posortowana
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
  
# losowa zamiana elementów - tasowanie
def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randint(0,n-1)  # losujemy indeksy
        a[i], a[r] = a[r], a[i]

def check_sorting(algorithm, array):
    # importujemy napisaną funkcję ze skryptu bazowego jeśli jest różna od sorted
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    # wykonamy kod 10 razy i zmierzymy czas
    times = repeat(setup=setup_code,
                   stmt=f"{algorithm}({array})",
                   repeat=3, number=10)
    print(f"Algorytm: {algorithm}. Średni czas: {mean(times)}")

if __name__ == "__main__":
    random.seed(123)
    # generujemy tablicę
    tab = losowe(5, 1, 10)
    print(tab)
    check_sorting('sorted', tab)
    check_sorting('bubble_sort', tab)
    check_sorting('select_sort', tab)
    check_sorting('insert_sort', tab)
    check_sorting('merge_sort', tab)
    check_sorting('quick_sort', tab)
    check_sorting('bogo_sort', tab)
