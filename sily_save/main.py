# game
import os
from typing import List

class SaveData:
    def __init__(self, file_name: str) -> None:
        pass

    def read_file(self, file_name: str) -> List[str]:
        with open(file_name, "r") as f:
            data = file_name.read_lines()
        self.data = {}
        for char in data[0]:
            if char == ".":
                state = "variable"
            elif char == ",":
                if state != "":
                    raise Exception
                state = "name"
            else:
                raise Exception
            match state:
                case "variable":
                    pass
                case "name":
                    pass
                case _:
                    print(f"Unexpected state ({state})")
                    raise Exception
        
data = SaveData("save.txt")
data.read_file("save.txt")
