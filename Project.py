Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Function to draw the Tic-Tac-Toe board
def draw_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False

... def main():
...     # Initialize the board and players
...     board = [[" " for _ in range(3)] for _ in range(3)]
...     player = 'X'
...     
...     print("Welcome to Tic-Tac-Toe!")
... 
...     # Game loop
...     for turn in range(9):
...         # Draw the board
...         draw_board(board)
... 
...         # Prompt for valid input
...         while True:
...             try:
...                 row, col = map(int, input(f"Player {player}, enter row (0-2) and column (0-2): ").split())
...                 if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
...                     print("Invalid move. Try again.")
...                 else:
...                     break  # Valid input, exit the loop
...             except ValueError:
...                 print("Invalid input. Enter two numbers separated by a space.")
... 
...         # Make the move
...         board[row][col] = player
... 
...         # Check for a win after making a move
...         if check_win(board, player):
...             draw_board(board)
...             print(f"Player {player} wins!")
...             return  # Exit the game after a win
... 
...         # Switch to the other player
...         player = 'O' if player == 'X' else 'X'
... 
...     # End of the game
...     draw_board(board)
...     print("It's a draw!")
... 
... if __name__ == "__main__":
...     main()
