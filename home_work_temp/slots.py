from random import choice
from typing import Any, Generic, TypeVar, List, Type, Callable


erase_line = "\033[F\033[K"
slot_ascii = ""

def true() -> bool:
    return True

CustomType = TypeVar('CustomType')
def fancy_input(
        message: str,
        _type: Type[CustomType],
        options: List[Any]=[],
        caps_sensitive: bool=False
    ) -> CustomType:

    def no_option_condition(_option) -> bool: 
        try:
            _type(_option)
        except TypeError:
            return False
        return True
    def options_condition(_option) -> bool:
        try:
            _tmp = _type(_option)
        except TypeError:
            return False
        return _tmp in options

    _input = ""
    condition = true
    if options == []:
        condition = no_option_condition
    else:
        condition = options_condition
    
    while not condition(_input):
        _input = input(message)
        if not caps_sensitive:
            _input = _input.lower()

    return _type(_input) # type: ignore #! Complains about too many inputs


if __name__ == "__main__":
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
        

    print("PLAY AGAIN!")