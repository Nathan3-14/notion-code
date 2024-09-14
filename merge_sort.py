def merge_sort(_unordered_list, first: bool=False):
    if first:
        _list_old = [[element] for element in _unordered_list]
    else:
        _list_old = _unordered_list
    _list_new = []

    for index in range(0, len(_list_old), 2):
        to_add = []
        
        index_1 = 0
        index_2 = 0
        while True:
            try:
                _list_old[index+1]
            except IndexError:
                for item in _list_old[index]:
                    to_add.append(item)
                break

            if index_1 >= len(_list_old[index]):
                for index_2_offset in range(len(_list_old[index+1])-index_2):
                    to_add.append(_list_old[index+1][index_2+index_2_offset])
                break
            if index_2 >= len(_list_old[index+1]):
                for index_1_offset in range(len(_list_old[index])-index_1):
                    to_add.append(_list_old[index][index_1+index_1_offset])
                break

            current_1 = _list_old[index][index_1]
            current_2 = _list_old[index+1][index_2]

            if current_1 <= current_2:
                to_add.append(current_1)
                index_1 += 1
            else:
                to_add.append(current_2)
                index_2 += 1

        _list_new.append(to_add)

    if len(_list_new) == 1:
        print("Done!")
        return _list_new[0]
    else:
        return merge_sort(_list_new)

if __name__ == "__main__":
    print(merge_sort([1, 3, 6, 1, 2, 10, 14, 4], True))
