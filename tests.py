import random

from searches import linear_search, binary_search
from sorts import bubble_sort, merge_sort

#* List Setup *#
ordered_list = list(range(1, 101))
unordered_list = ordered_list.copy()
random.shuffle(unordered_list)

#* Run Searches *#
linear_search(unordered_list, 57)
binary_search(ordered_list, 57)
linear_search(unordered_list, 107)
binary_search(ordered_list, 107)

#* Run Sorts *#
print(
    bubble_sort(unordered_list)
)
print(
    merge_sort(unordered_list, True)
)
