import sqlite3 as sq3
from sys import argv
from typing import Any, Dict, List
from sql_print import print_table

class Main:
    def __init__(self, file_address: str) -> None:
        self.connection = sq3.connect(file_address)
        self.cursor = self.connection.cursor()
        # self.cursor.

    def console(self, args) -> int:
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
    
    def display(self, args) -> int:
        if len(args) < 1:
            print("BAD args :(")
            return -1
        database_names = args
        database_names_columns: Dict[str, List[str]] = {}
        try:
            for index, database_name in enumerate(database_names):
                self.cursor.execute(f"SELECT * FROM {database_name}")
                database_names_columns[database_name] = [description[0] for description in self.cursor.description]
            
            
            select_text = ", ".join([
                ", ".join([f"{name}.{key}" for key in data])
                for name, data in database_names_columns.items()
            ])
            
            shared_key = None
            if len(database_names) > 1:
                for key in database_names_columns[database_names[0]]:
                    if key in database_names_columns[database_names[1]]:
                        shared_key = key
            if shared_key == None and len(database_names) > 1:
                print("No shared key :(")
                return -1
            
            self.cursor.execute(f"""
                                SELECT {select_text}
                                FROM {database_names[0]}
                                    {f'''INNER JOIN {database_names[1]}
                                        ON {database_names[0]}.{shared_key} = {database_names[1]}.{shared_key}''' if len(database_names) > 1 else ''}
                                """)
            data = self.cursor.fetchall()
            
            database_columns = [description[0] for description in self.cursor.description]
            print_table(", ".join(database_names), database_columns, data)
            
        except Exception as e:
            print(e)
            return -1

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
        "list": main.display,
        # "create": main.create_table
    }

    if not len(args) >= 1:
        print(f"Invalid run code, requires one of ({', '.join(list(commands.keys()))}) to run")
        quit()
    try:
        commands[args[0]](args[1:])
    finally:
        main.connection.close()

