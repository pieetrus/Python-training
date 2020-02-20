import numpy as np

list_numbers = np.arange(0,101,2)



def binary_search_recursive(list_of_elements, element, left, right):
    if(left > right):
        return False

    mid = left + (right - left) // 2 #protected from overflow

    if(list_of_elements[mid] == element):
        return True
    elif(element > list_of_elements[mid]):
        return binary_search_recursive(list_of_elements, element, mid + 1, right)
    elif(element < list_of_elements[mid]):
        return binary_search_recursive(list_of_elements, element, left, mid - 1)

def binary_search_itterative(list_of_elements, element):
    left = 0
    right = len(list_of_elements) - 1

    while left <= right:
        mid = left + (right - left) // 2 #protected from overflow
        if element == list_of_elements[mid]:
            return True
        if element > list_of_elements[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False

result1 = binary_search_recursive(list_numbers, 40, 0, len(list_numbers) - 1)

result2 = binary_search_itterative(list_numbers, 38)

print(result1)
print(result2)
