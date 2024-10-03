# Gomoku Game

This project is an implementation of the classic board game Gomoku in Python. The game is played on an 8x8 grid, where the objective is to place five stones in a row (either horizontally, vertically, or diagonally) before your opponent. The game allows a user to play against a computer AI, which determines optimal moves using a scoring system.

## Features:
- **Board Setup**: The game is played on a configurable board (default 8x8).
- **AI Opponent**: The computer AI uses a scoring algorithm to determine the best move.
- **Game Analysis**: The game detects sequences and identifies whether they are open, semi-open, or closed.
- **Win Detection**: The game checks for win conditions and announces whether "Black won," "White won," or if the game is a "Draw."

## Key Functions:
- `play_gomoku(board_size)`: Main function to play the game. The user plays against the computer on a board of the given size.
- `is_win(board)`: Determines the current game state, checking if a player has won, if it's a draw, or if the game should continue.
- `search_max(board)`: AI algorithm that searches for the optimal move for the black player by maximizing the board score.
- `detect_rows(board, col, length)`: Analyzes the board and counts open and semi-open sequences of a given length.
- `is_sequence_complete(board, col, y, x, length, d_y, d_x)`: Helper function that checks if there is a complete sequence of a given color.

## How to Play:
1. The computer makes the first move by placing a black stone in the center of the board.
2. The player then takes their turn by entering the coordinates (x, y) for placing a white stone.
3. The game alternates between the computer and the player until one side wins or the game results in a draw.

## How to Run:
```bash
# Clone the repository
git clone <https://github.com/najmasultani/Python-Projects-General/tree/main/Gomoku>

# Run the game
python gomoku.py
