import sqlite3 as sq3
from sys import argv
from typing import Any, Dict, List
from sql_print import get_select_table
import rich

class Main:
    def __init__(self, file_address: str) -> None:
        self.connection = sq3.connect(file_address)
        self.cursor = self.connection.cursor()
        # self.cursor.

    def console(self, args) -> int:
        # try:
            _input = ""
            while True:
                _input = input(">> ")
                command = _input.split(" ")[0].lower()
                output: List[Any] | str = ""
                match command:
                    case "quit" | "exit" | "end":
                        break
                    case "select":
                        output = get_select_table(_input, self.cursor)
                    case _:
                        output = self.cursor.execute(_input).fetchall()
                rich.print(output)
        # except Exception as e:
        #     print(e)
        #     return -1
            return 0
    

    # def create_table(self, args) -> int:
    #     if len(args) != 1:
    #         print("BAD args :(")
    #         return -1
    #     file_path = args[0]
    #     try:
    #         with open(file_path, "r") as f:
    #             data = f.readlines()
    #         table_name = data[0]
    #         table_keys = data[1].split(",")
    #         table_types = data[2].split(",")
    #         table_extras = [extra_list.split(".") for extra_list in data[3].split(",")]

    #         temp_var_name = [
    #             f"{table_keys[index]} {table_types[index]} {' '.join(table_extras[index])},"
    #             for index in range(len(table_keys))
    #         ]

    #         command = f"CREATE TABLE {table_name} ( {''.join(temp_var_name).strip(',')} );"
    #         print(command)
    #         self.cursor.execute(command)
            
    #     except Exception as e:
    #         print(e)
    #         return -1
    #     return 0
    

if __name__ == "__main__":
    main = Main("shop.db")
    args = argv[1:]
    commands = {
        "console": main.console,
        # "create": main.create_table
    }

    if not len(args) >= 1:
        print(f"Invalid run code, requires one of ({', '.join(list(commands.keys()))}) to run")
        quit()
    try:
        commands[args[0]](args[1:])
    finally:
        main.connection.close()

