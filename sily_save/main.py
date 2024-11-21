# game
# import os
import json
from typing import Any, Dict, List

import rich

def printjson(data: Dict[Any, Any]) -> None:
    rich.print_json(json.dumps(data))


class SaveData:
    def __init__(self, file_name: str) -> None:
        pass

    def read_file(self, file_name: str) -> List[str]:
        with open(file_name, "r") as f:
            data = f.readlines()

        self.data: Dict[str, Dict[str, Any]] = {}
        state = ""
        value = ""

        for char in data[0]:
            match char:
                case "," | "." | "\n":
                    match state:
                        case "name":
                            self.data[value] = {}
                        case "variable":
                            for player_name in list(self.data.keys()):
                                self.data[player_name][value] = ""

                    value = ""
                    state = "name" if char == "," else "variable"
                case _:
                    value += char
        for line_index, line in enumerate(data[1:]):
            line_split = line.strip().split(",")
            data_names = list(self.data.keys())
            if len(line_split) != len(data_names):
                print("File bad")
                raise Exception
            for name_index, name in enumerate(data_names):
                self.data[name][
                    list(self.data[name].keys())
                    [line_index]
                ] = line_split[name_index]
        
        printjson(self.data)
        return [] #! ONLY USED AS A TEMP !#
    

data = SaveData("save.txt")
data.read_file("save.txt")