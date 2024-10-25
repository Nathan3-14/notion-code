from random import choice


def fancy_input(message: str, type=str) -> type:
    pass


ROLL_WEIGHTS = {
    "1": 5,
    "2": 5,
    "3": 5,
    "4": 3,
    "5": 1
}
ROLLS = [
    [num] * weight for num, weight in ROLL_WEIGHTS.items()

]

COST = 1
money = 10

while money > 0:
    if input("go? (y/n)").lower() == "n":
        break
    bet_on = input("What bet on? (red/black)").lower()


print("PLAY AGAIN!")
