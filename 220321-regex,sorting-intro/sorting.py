
def bubble_sort(list):
    # Zamieniamy elementy miejscami
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

def smalest_index(myarray):
    '''
    # Zakładamy, że pierwszy element wycinka listy jest najmniejszy
    smallest_idx = 0
    # Przechodzimy po liście
    for j in range(len(myarray) - 1):
        if myarray[j] < myarray[j + 1]:
            smallest_idx = j
    return smallest_idx
    '''
    return myarray.index(min(myarray)) # bardziej pythonowy sposób ;-)

def selection_sort(nums):
    # Iterujemy po wszystkich elementach listy
    for i in range(len(nums)):
        # Przechodzimy po nieposortowanym fragmencie listy
        lowest_value_index = smalest_index(nums[i:])
        # Zamieniemy wartości najmniejszego elementu z nieposortowanej listy oraz oraz bieżącego elementu
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def insertion_sort(nums):
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
