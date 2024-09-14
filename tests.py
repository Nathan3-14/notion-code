import random
from binary_search import binary_search
from linear_search import linear_search

from merge_sort import merge_sort

ordered_list = list(range(1, 101))
unordered_list = ordered_list.copy()
random.shuffle(unordered_list)

linear_search(unordered_list, 57)
binary_search(ordered_list, 57)
linear_search(unordered_list, 107)
binary_search(ordered_list, 107)

print(
    merge_sort(unordered_list, True)
)
