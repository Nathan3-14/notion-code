import rich

print = rich.print

def iinput(message: str) -> int:
    _input = "#<as!:>':j[hlp[gkfoj"
    while not _input.isdigit():
        if _input != "#<as!:>':j[hlp[gkfoj":
            print("Enter an int")
        _input = input(message)
    return int(_input)

if __name__ == "__main__":
    NUMBER_OF_INPUTS = 5

    nums = []
    for _ in range(NUMBER_OF_INPUTS):
        nums.append(iinput("Give num plz "))
    nums.sort()

    total = sum(nums)
    mean = total / len(nums)
    smallest = nums[0]
    largest = nums[-1]

    print(f"Total: {total}\nMean: {mean}\nSmallest: {smallest}\nLargest: {largest}")

