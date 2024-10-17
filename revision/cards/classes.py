from typing import Dict, List, Tuple
from random import shuffle

class Deck:
    def __init__(self, suits: str="SCHD", num_range: Tuple[int, int]=(2, 10), letters: str="JQKA", debug: bool=False) -> None:
        self.debug = debug
        self.cards = []
        values = list(range(num_range[0], num_range[1]+1)) + [letter for letter in letters]
        for suit in suits:
            for value in values:
                self.cards.append(f"{value}{suit}")
        self.display()

    def shuffle(self) -> None:
        shuffle(self.cards)
    
    def display(self) -> None:
        for index, card in enumerate(self.cards):
            print(f"{card} ", end="")
            if index+1 % 13 == 0:
                print("")
