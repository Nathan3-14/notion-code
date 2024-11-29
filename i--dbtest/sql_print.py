import sqlite3 as sq3
from typing import Any, List
from rich.console import Console
from rich.table import Table
import rich

def get_table(table_name: str, columns: List[Any], rows: List[Any]) -> Table:
    table = Table(title=table_name)
    
    for column_name in columns:
        table.add_column(column_name)
    for row_data in rows:
        row_data_str = [str(row_item) for row_item in row_data]
        table.add_row(*row_data_str)

    return table



def get_select_table(select_statement: str, cursor: sq3.Cursor) -> Table:
    data = cursor.execute(select_statement).fetchall()
    column_names = [description[0] for description in cursor.description]

    return get_table(select_statement, column_names, data)

def print_select(select_statement: str, cursor: sq3.Cursor) -> None:
    rich.print(get_select_table(select_statement, cursor))



if __name__ == "__main__":
    conn = sq3.connect("shop.db")
    print_select("select * from customers inner join orders on orders.CustomerID=customers.CustomerID", conn.cursor())
    conn.close()
