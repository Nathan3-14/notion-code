def linear_search(_unordered_list, target):
    for element in _unordered_list:
        if element == target:
            print(f"Item {target} found!")
            return
    print(f"Item {target} not found")