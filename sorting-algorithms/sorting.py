import numpy as np

list_of_random_numbers = [np.random.randint(0,1000) for i in range(0,100)]


def bubble_sort(array):
    arr = array.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1): # -1 bo ostatni element jest już ustawiony na swojej pozycji
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(array):
    arr = array.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr 

def insertion_sort(array):
    arr = array.copy()
    n = len(array)

    #1 element uważamy za posortowany
    for i in range(1,n):
        #key - pierwszy nieposortowany element
        #index - indeks tego elementu
        key = arr[i]
        index = i
        #dopóki istnieje element mniejszy od klucza to przessuwaj go o jedną pozycję w lewo
        #index > 0 zapobiega wyjściu poza tablicę gdy znajdziemy najmniejszy element w całej tablicy
        while key < arr[i-1] and index > 0:
            arr[i] = arr[i-1]
            index = i-1
        #index to miejsce w którym powinien się znaleźć dotychczas nieposortowany element
        arr[index] = key
    return arr




#sorted_list1 = bubble_sort(list_of_random_numbers)
sorted_list2 = selection_sort(list_of_random_numbers)
sorted_list3 = insertion_sort2(list_of_random_numbers)

#print(list_of_random_numbers)
#print(sorted_list1)
#print(sorted_list2)
print(sorted_list3)


