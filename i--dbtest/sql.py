import sqlite3 as sq3
from sys import argv
from typing import Any, List

class Main:
    def __init__(self, file_address: str) -> None:
        self.connection = sq3.connect(file_address)
        self.cursor = self.connection.cursor()
        # self.cursor.

    def console(self, *args) -> int:
        try:
            _input = ""
            while True:
                _input = input(">> ")
                if _input.lower() in ["quit", "exit", "end"]:
                    break
                output: List[Any] | str = ""
                try:
                    self.cursor.execute(_input)
                    output = self.cursor.fetchall()
                except Exception:
                    pass
                    # print(e)
                print(output)
        except Exception as e:
            print(e)
            return -1
        return 0
    
    def display(self, *args) -> int:
        if len(args) != 1:
            print("BAD :( args")
        try:
            self.cursor.execute(f"SELECT * FROM {args[0]}").fetchall()
        except Exception as e:
            print(e)
            return -1

        return 0

if __name__ == "__main__":
    main = Main("./shop.db")
    args = argv[1:]
    commands = {
        "console": main.console,
        "list": main.display
    }

    if not len(args) >= 1:
        print(f"Invalid run code, requires one of ({', '.join(list(commands.keys()))}) to run")
        quit()
    try:
        commands[args[0]](args[1:])
    finally:
        main.connection.close()

# cursor.execute("CREATE TABLE orders (OrderId INT, CustomerId INT, DateShipped DATE)")
