def insertion_sort(_unordered_list):
    new_list = _unordered_list.copy()
    for item_index in range(len(new_list)):
        current_comparison = new_list[item_index]
        new_list.pop(item_index)
        target_index = 0
        if item_index != 0:
            for compare_index in range(item_index-1):
                if current_comparison >= new_list[compare_index]:
                    target_index = compare_index + 1
                    print(f"{current_comparison} >= {new_list[compare_index]}, setting target to {target_index}")
                else:
                    print(f"{current_comparison} not >= {new_list[compare_index]}")
        else:
            print("skipped")

        new_list.insert(target_index, current_comparison)
                
        print(new_list)


if __name__ == "__main__":
    insertion_sort([1, 2, 7, 4, 3])
