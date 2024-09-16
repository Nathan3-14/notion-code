import math as maths


def binary_search(_ordered_list, target):
    while len(_ordered_list) != 0:
        middle_index = maths.floor(len(_ordered_list)/2)
        middle = _ordered_list[middle_index]
        if middle > target:
            _ordered_list = _ordered_list[:middle_index]
        elif middle < target:
            _ordered_list = _ordered_list[middle_index+1:]
        else:
            print(f"Item {target} found!")
            return
    print(f"Item {target} not found")


if __name__ == "__main__":
    binary_search(list(range(1, 101)), 57)
