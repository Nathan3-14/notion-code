import datetime
import random

from searches import linear_search, binary_search
from sorts import bubble_sort, merge_sort, insertion_sort

start = None
def time_stamp(message: str=""):
    global start
    if start == None:
        print("")
        start = datetime.datetime.now()
    else:
        end = datetime.datetime.now()
        time_delta = end - start
        print(f"{message} Took {time_delta.microseconds / 1000} milliseconds")
        start = None

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
time_stamp()
print(
    bubble_sort(unordered_list)
)
time_stamp()


time_stamp()
print(
    merge_sort(unordered_list, True)
)
time_stamp()


time_stamp()
print(
    insertion_sort(unordered_list)
)
time_stamp()
