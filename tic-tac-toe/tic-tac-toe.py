'''
Tic Tac Toe
Devin Sigler
'''

def board_position():
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return position

def display(position):
    print(f"{position[0]}|{position[1]}|{position[2]}")
    print("-+-+-")
    print(f"{position[3]}|{position[4]}|{position[5]}")
    print("-+-+-")
    print(f"{position[6]}|{position[7]}|{position[8]}")

def get_player(player):
    if player == "x":
        return "o"
    elif player == "o" or player == "":
        return "x"

def turn(player, board):
    value = int(input(f"{player}'s turn to choose a square (1-9)\n"))
    if value <= 0 or value >=10:
        print("Please enter a value between 1 and 9")
        turn(board)
    elif board[value - 1] == "x" or board[value - 1] == "o":
        print("Please enter a value that hasn't been chosen")
        display(board)
        return turn(player, board)                                                                                             
    board[value - 1] = player

def check_win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[2] == board[4] == board[6] or
            board[0] == board[4] == board[8])
    
def no_win(board):
    if (board[0] != 1 and board[1] != 2 and board[2] != 3 and
        board[3] != 4 and board[4] != 5 and board[5] != 6 and
        board[6] != 7 and board[7] != 8 and board[8] != 9):
        print("No winner! Try again")
        return True

def main():
    player = ""
    board = board_position()
    while not (check_win(board) or no_win(board)):
        display(board)
        turn(player, board)
        player = get_player(player)
    display(board)
    print("Good game!")

if __name__ == "__main__":
    main()