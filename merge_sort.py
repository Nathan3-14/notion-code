def merge_sort(_unordered_list):
    _list_old = [[element] for element in _unordered_list]
    _list_new = []

    for index in range(0, len(_list_old), 2):
        to_add = []
        
        index_1 = 0
        index_2 = 0
        while True:
            if _list_old[index][index_1] <= _list_old[index+1][index_2]:
                to_add.append(_list_old[index][index_1])
                index_1 += 1
            else:
                to_add.append(_list_old[index+1][index_2])
                index_2 += 1
            
            if index_1 >= len(_list_old[index]):
                while index_2 < len(_list_old[index+1]):
                    to_add.append(_list_old[index+1][index_2])
                    index_2 += 1
                break
            elif index_1 >= len(_list_old[index]):
                while index_1 < len(_list_old[index]):
                    to_add.append(_list_old[index][index_1])
                    index_1 += 1
                break

        _list_new.append(to_add)

    # _list_new = [_list_old[index] + _list_old[index+1] for index in range(0, len(_list_old), 2)]


    print(_list_new)

    if len(_list_new) == 1:
        print("Done!")
        return _list_new
    else:
        return merge_sort(_list_new)

if __name__ == "__main__":
    print(merge_sort([1, 3, 6, 1, 2, 10, 14, 4]))
