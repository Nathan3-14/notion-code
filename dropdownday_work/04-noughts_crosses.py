from typing import List

wins = [
    ("00", "01", "02"),
    ("10", "11", "12"),
    ("20", "21", "22"),
    ("00", "10", "20"),
    ("01", "11", "21"),
    ("02", "12", "22"),
    ("00", "11", "22"),
    ("02", "11", "20")
]
def display_board(board: List[List[str]]):
    for index, row in enumerate(board):
        print("|".join(row))
        if index in [0, 1]:
            print("-+-+-")
def check_win(board: List[List[str]]) -> bool:
    for win in wins:
        if board[int(win[0][0])][int(win[0][1])] == board[int(win[1][0])][int(win[1][1])] == board[int(win[2][0])][int(win[2][1])] and board[int(win[0][0])][int(win[0][1])] in ["X", "O"]:
            return True
    return False
    
current_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
current_turn = "O"

while True:
    print(f"{current_turn} is going")
    display_board(current_board)
    chosen_pos = input("Enter a position")
    x, y = 9, 9
    for index, row in enumerate(current_board):
        if chosen_pos in row:
            x = row.index(chosen_pos)
            y = index
            break
    if x == 9 or y == 9:
        print("Bad pos :(")
        continue
    current_board[y][x] = current_turn
    if check_win(current_board):
        print(f"{current_turn} won!")
        quit()
    for index, row in enumerate(current_board):
        for item in row:
            if item.isdigit():
                theres_a_digit = True
        if index == 2 and not theres_a_digit:
            display_board(current_board)
            print("No moves left!")
            quit()
    current_turn = "X" if current_turn == "O" else "O"
    

    