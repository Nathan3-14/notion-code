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
        # self.data = self.read_file(file_name)

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
        return self.data
    
    def write_file(self, file_name: str) -> None:
        names = list(self.data.keys())
        variables = list(self.data[names[0]].keys()).copy()
        lines = ["," + ",".join(names) + "." + ".".join(variables)]

        printjson(lines)

    

data = SaveData("save.txt")
# data.read_file("save.txt")
data.data = {
    "a": {
        "x": 1,
        "y": 2
    },
    "b": {
        "x": 3,
        "y": 0
    },
    "c": {
        "x": 10,
        "y": 20
    }
}
data.write_file("testsave.txt")
