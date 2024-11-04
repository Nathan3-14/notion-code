from math import floor

def binary_to_denary(binary: str) -> int:
    current = 0
    for char in binary:
        current *= 2
        if char == "1":
            current += 1
    return current

def denary_to_binary(denary: int) -> str:
    current = []
    while denary != 0:
        current.append(denary % 2)
        denary = floor(denary/2)

    current.reverse()
    return "".join(
        [str(item) for item in current]
    )

if __name__ == "__main__":
    print(binary_to_denary("1011"))
    print(denary_to_binary(11))
