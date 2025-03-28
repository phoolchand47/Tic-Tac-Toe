# Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check other diagonal
        return True
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to handle the player's move
def make_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move! Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != ' ':
                print("That spot is already taken, try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Main function to run the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        make_move(board, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
