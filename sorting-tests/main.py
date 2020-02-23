import functools
import timeit

from numpy.random import randint

from sort import Sort

array = [randint(0, 100) for i in range(0, 100)]

sort = Sort()
t = [0, 0, 0, 0, 0, 0]

t[0] = timeit.Timer(functools.partial(sort.bubble_sort, array)).timeit(100)
t[1] = timeit.Timer(functools.partial(sort.heap_sort, array)).timeit(100)
t[2] = timeit.Timer(functools.partial(sort.insertion_sort, array)).timeit(100)
t[3] = timeit.Timer(functools.partial(sort.merge_sort, array)).timeit(100)
t[4] = timeit.Timer(functools.partial(sort.quick_sort, array)).timeit(100)
t[5] = timeit.Timer(functools.partial(sort.selection_sort, array)).timeit(100)


