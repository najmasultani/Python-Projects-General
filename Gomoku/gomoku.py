# Gomoku Game Implementation

# This function returns True if there are no stones on the board, indicating an empty board.
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                return False
    return True

# Helper function to check if the given (x, y) coordinates are within the board's boundaries.
def is_sq_in_board(board, y, x):
    if x < 0 or x >= len(board[0]):
        return False
    elif y < 0 or y >= len(board):
        return False
    return True

# Analyzes the sequence ending at (y_end, x_end) and determines if it's 'OPEN', 'SEMIOPEN', or 'CLOSED'.
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - (length - 1) * d_y
    x_start = x_end - (length - 1) * d_x

    # Checking the validity of the start and end points for the sequence.
    valid_start = is_sq_in_board(board, y_start - d_y, x_start - d_x)
    valid_end = is_sq_in_board(board, y_end + d_y, x_end + d_x)

    # Determine if the sequence is OPEN, SEMIOPEN, or CLOSED based on the surroundings.
    if valid_start and board[y_start - d_y][x_start - d_x] == ' ' and valid_end and board[y_end + d_y][x_end + d_x] == ' ':
        return 'OPEN'
    elif valid_start and board[y_start - d_y][x_start - d_x] == ' ' or valid_end and board[y_end + d_y][x_end + d_x] == ' ':
        return 'SEMIOPEN'
    return 'CLOSED'

# Checks if there is a complete sequence of a given color starting at (y_start, x_start) with the specified direction (d_y, d_x).
def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    y_end = y_start + (length - 1) * d_y
    x_end = x_start + (length - 1) * d_x

    if not is_sq_in_board(board, y_start, x_start) or not is_sq_in_board(board, y_end, x_end):
        return False

    # Verify if all stones in the sequence are of the same color.
    for i in range(length):
        y = y_start + i * d_y
        x = x_start + i * d_x
        if board[y][x] != col:
            return False

    # Ensure the sequence is not followed or preceded by the same color stone.
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) and board[y_start - d_y][x_start - d_x] == col:
        return False
    if is_sq_in_board(board, y_end + d_y, x_end + d_x) and board[y_end + d_y][x_end + d_x] == col:
        return False
    return True

# Detects open and semi-open sequences of a given length starting from (y_start, x_start) in the direction (d_y, d_x).
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            y_end = y + (length - 1) * d_y
            x_end = x + (length - 1) * d_x
            if is_sq_in_board(board, y_end, x_end) and is_sequence_complete(board, col, y, x, length, d_y, d_x):
                sequence_type = is_bounded(board, y_end, x_end, length, d_y, d_x)
                if sequence_type == 'OPEN':
                    open_seq_count += 1
                elif sequence_type == 'SEMIOPEN':
                    semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

# Analyzes the entire board and returns the number of open and semi-open sequences of a given length for a specific color.
def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0

    sequence_direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for d_y, d_x in sequence_direction:
        for y in range(len(board)):
            for x in range(len(board[0])):
                y_end = y + (length - 1) * d_y
                x_end = x + (length - 1) * d_x
                if is_sq_in_board(board, y_end, x_end) and is_sequence_complete(board, col, y, x, length, d_y, d_x):
                    sequence_type = is_bounded(board, y_end, x_end, length, d_y, d_x)
                    if sequence_type == 'OPEN':
                        open_seq_count += 1
                    elif sequence_type == 'SEMIOPEN':
                        semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

# AI engine uses this function to find the optimal move by maximizing the score for black stones.
def search_max(board):
    max_score = 0
    optimal_move = None
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == " ":
                board[y][x] = "b"
                potential_score = score(board)
                board[y][x] = " "

                if potential_score > max_score:
                    max_score = potential_score
                    optimal_move = (y, x)

    return optimal_move if optimal_move else (0, 0)

# This function computes and returns the score of the board, assuming black has just moved.
def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    if open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

# Determines the current status of the game, returning "White won", "Black won", "Draw", or "Continue playing".
def is_win(board):
    for col in ['b', 'w']:
        sequence_direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for d_y, d_x in sequence_direction:
            for y in range(len(board)):
                for x in range(len(board[0])):
                    if is_sq_in_board(board, y + 4 * d_y, x + 4 * d_x):
                        if is_sequence_complete(board, col, y, x, 5, d_y, d_x):
                            return "Black won" if col == 'b' else "White won"
    for row in board:
        if ' ' in row:
            return "Continue playing"
    return "Draw"

# Function to print the current state of the Gomoku board.
def print_board(board):
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i % 10) + "|"
    s += str((len(board[0])-1) % 10) + "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0])-1):
            s += board[i][j] + "|"
        s += board[i][len(board[0])-1] + "*\n"
    s += (len(board[0]) * 2 + 1) * "*"
    print(s)

# Function to create an empty board of size sz x sz.
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board

# Analyzes the current board state and prints the number of open and semi-open sequences for both players.
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print(f"{full_name} stones")
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print(f"Open rows of length {i}: {open}")
            print(f"Semi-open rows of length {i}: {semi_open}")


# This function allows the user to play against a computer on a board of size board size × board size. 
#This function interacts with the AI engine by calling the function searchMax(), which you will write.def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print(f"Computer move: ({move_y}, {move_x})")
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

# Function to place a sequence of stones on the board for testing purposes.
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

# Main entry point for the game
if __name__ == '__main__':
    play_gomoku(8)
