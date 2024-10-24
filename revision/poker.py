import cards
from typing import Literal, List

class Poker:
    def __init__(self, player_count: int, type: Literal["texas", "5-card"], auto_deal: bool=False) -> None:
        self.player_count = player_count
        self.type = type

        self.deck = cards.Deck()
        self.deck.shuffle()

        if auto_deal:
            self.deal()
    
    def draw_cards(self, count: int=1) -> List[str]:
        to_return = []
        for _ in range(count):
            to_return.append(self.deck.draw())
        return to_return

    def deal(self) -> None:
        self.players = {}
        for player_id in range(self.player_count):
            draw_number = 2 if self.type == "texas" else 5
            self.players[player_id] = self.draw_cards(draw_number)

if __name__ == "__main__":
    game = Poker(4, "5-card", auto_deal=True)
    print(game.players)

