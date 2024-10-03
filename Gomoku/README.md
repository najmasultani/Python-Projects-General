# Gomoku Game

This project implements a simple AI engine for the classic board game Gomoku. The game is played on an 8x8 grid, where the objective is to place five stones in a row (horizontally, vertically, or diagonally) before your opponent. The game allows a user to play against a computer AI, which determines optimal moves using a scoring system.

## Project Overview
- **Game Type**: Two-player (Black vs White) Gomoku, where the computer plays as Black.
- **Board Setup**: The game is played on a configurable board (default 8x8).
- **Goal**: The first player to align five stones wins.
- **AI Engine**: The computer AI uses a scoring algorithm to determine the best move and plays as Black.
- **User Input**: The user places White stones on the board by specifying coordinates.

## Features:
- **AI Opponent**: The computer AI evaluates the board using a custom scoring function and plays optimally to maximize its chances of winning.
- **Game Analysis**: The game detects and classifies sequences as `OPEN`, `SEMIOPEN`, or `CLOSED`.
- **Win Detection**: The game checks for win conditions and declares "Black won", "White won", or a "Draw."
- **No Global Variables**: The project follows best practices, ensuring no global variables are used.

## Key Functions:
- `play_gomoku(board_size)`: Main function to play the game. The user plays against the computer on a configurable board size.
- `is_win(board)`: Determines the current game state, checking if a player has won, if it's a draw, or if the game should continue.
- `search_max(board)`: AI function that finds the best move for Black based on the board score.
- `detect_rows(board, col, length)`: Analyzes the board for open and semi-open sequences of a given length.
- `is_sequence_complete(board, col, y, x, length, d_y, d_x)`: Checks if there is a complete sequence of a given color in the specified direction.

## How to Play:
1. **Computer (Black)** moves first by placing a stone in the center of the board.
2. **User (White)** inputs the coordinates `(x, y)` to place their stone.
3. The game alternates between the computer and the user until a player wins or the game ends in a draw.

## Resources: 
This project was originally developed as part of the **ESC180 course** at the University of Toronto.

## How to Run:
```bash
# Clone the repository
git clone https://github.com/najmasultani/Python-Projects-General.git

# Navigate to the Gamification folder
cd Python-Projects-General/Gomoku

# Run the game
python gomoku.py

