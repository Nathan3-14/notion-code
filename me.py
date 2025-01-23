from typing import List, Callable

def move():
    print("Moving\n")
def inv():
    print("1xSword, 2xPotion\n")
def attack():
    print("Attacked with sword!\n")

entity_traits = [move]
player_traits = [inv, attack]

class Obj:
    def __init__(self, name: str, trait_list: List[List[Callable]]) -> None:
        self.commands = {}
        for command_list in trait_list:
            self.commands = self.commands | {command.__name__: command for command in command_list}
        self.__name__ = name
    def run(self, command_name: str) -> None:
        print(f"{self.__name__} running {command_name}")
        try:
            self.commands[command_name]()
        except:
            print(f"No such command: {command_name}\n")

player = Obj("player", [entity_traits, player_traits])
entity = Obj("entity", [entity_traits])

player.run("move")
entity.run("move")
player.run("inv")
entity.run("inv")
player.run("attack")
entity.run("attack")
player.run("potion")
entity.run("potion")
