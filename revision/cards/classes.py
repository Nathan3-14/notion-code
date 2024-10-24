from typing import Dict, List, Tuple
from random import shuffle

class Deck:
    def __init__(self, suits: str="SCHD", num_range: Tuple[int, int]=(2, 10), letters: str="A...JQK", debug: bool=False) -> None:
        self.debug = debug
        self.cards = []
        letters_split = letters.split("...")
        values = [letter for letter in letters_split[0] if len(letters_split) > 1] + list(range(num_range[0], num_range[1]+1)) + [letter for letter in letters_split[-1]]
        for suit in suits:
            for value in values:
                self.cards.append(f"{value}{suit}")
        self.display()

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw(self) -> str:
        card = self.cards[0]
        self.cards.pop(0)
        return card
    
    def display(self) -> None:
        for index, card in enumerate(self.cards):
            print(f"{card} ", end="")
            if (index+1)%13 == 0:
                print("")
        print("")
