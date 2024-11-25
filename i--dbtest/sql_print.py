from typing import Any, List
from rich.console import Console
from rich.table import Table

def print_table(table_name: str, columns: List[Any], rows: List[Any]) -> None:
    table = Table(title=table_name)
    
    for column_name in columns:
        table.add_column(column_name)
    for row_data in rows:
        row_data_str = [str(row_item) for row_item in row_data]
        table.add_row(*row_data_str)

    console = Console()
    console.print("\n")
    console.print(table)
    console.print("\n")


if __name__ == "__main__":
    print_table("Test", ["number", "string", "another number"], [(1, 1, '21-11-2024'), (2, 2, '23-11-2024'), (3, 3, '23-11-2024'), (4, 4, '24-11-2024'), (5, 5, '25-11-2024'), (6, 2, '30-11-2024'), (7, 3, '01-12-2024')])
