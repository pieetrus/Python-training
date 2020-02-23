class Sort():


    #METHODS

    def bubble_sort(self, array):
        arr = array.copy()
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):  # -1 bo ostatni element jest już ustawiony na swojej pozycji
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, array):
        arr = array.copy()
        n = len(arr)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def insertion_sort(self, array):
        arr = array.copy()
        n = len(arr)

        # 1 element uważamy za posortowany
        for i in range(1, n):
            # key - pierwszy nieposortowany element
            # index - indeks tego elementu
            key = arr[i]
            index = i
            # dopóki istnieje element mniejszy od klucza to przessuwaj go o jedną pozycję w lewo
            # index > 0 zapobiega wyjściu poza tablicę gdy znajdziemy najmniejszy element w całej tablicy
            while key < arr[index - 1] and index > 0:
                arr[index] = arr[index - 1]
                index = index - 1
            # index to miejsce w którym powinien się znaleźć dotychczas nieposortowany element
            arr[index] = key
        return arr

    def merge_sort(self, array):
        # left, right = [],[]
        n = len(array)
        if (n < 2):
            return array
        mid = n // 2

        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])

        return self.__merge(left, right)

    def __merge(self, left, right):
        result = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        # jeśli doszliśmy do końca którejś z tablic to dopisz końcówkę drugiej tablicy do result
        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result

    def heap_sort(self, array):
        arr = array.copy()
        n = len(arr)
        # sprowadzamy kopiec do kopca masymalnego
        for i in range(n // 2 - 1, -1, -1):  # [n//2 - 1, n//2 -2, ..., 0 ]
            self.__validate_max_heap(array, n, i)
        for i in range(n - 1, 1, -1):  # [n-1,n-2,...,1] bo korzeń jest posortowany już
            array[0], array[i] = array[i], array[0]
            self.__validate_max_heap(array, i, 0)
        return arr

    def __validate_max_heap(self, array, heap_size, parent_index):
        max_index = parent_index
        left_index, right_index = 2 * parent_index + 1, 2 * parent_index + 2

        if left_index < heap_size and array[max_index] < array[left_index]:
            max_index = left_index
        if right_index < heap_size and array[max_index] < array[right_index]:
            max_index = right_index
        if max_index != parent_index:
            array[max_index], array[parent_index] = array[parent_index], array[max_index]
            self.__validate_max_heap(array, heap_size, max_index)

    def quick_sort(self, array):
        arr = array.copy()
        return self.__quick_sort2(arr, 0, len(arr) - 1)

    def __quick_sort2(self, array, left, right):
        if left < right:
            border = self.__partition(array, left, right)
            self.__quick_sort2(array, left, border - 1)
            self.__quick_sort2(array, border + 1, right)
        return array

    def __get_pivot(self, array, left, right):
        mid = left + (right - left) // 2
        pivot = left
        if array[left] < array[mid]:
            if array[mid] < array[right]:
                pivot = mid
        elif array[left] < array[right]:
            pivot = right
        return pivot

    def __partition(self, array, left, right):
        pivot_index = self.__get_pivot(array, left, right)
        partition_index = left
        pivot = array[pivot_index]

        for i in range(left, right):
            if array[i] < pivot:
                array[partition_index], array[i] = array[i], array[partition_index]
                partition_index += 1
        array[pivot_index], array[partition_index] = array[partition_index], array[pivot_index]
        return partition_index