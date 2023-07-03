#!/usr/bin/python3
""" Solve the N-queens puzzle"""


import sys


def create_board(n):
    """Initialize chessboard with empty spaces"""
    board = []
    for _ in range(n):
        row = [' ' for _ in range(n)]
        board.append(row)
    return board


def board_copy(board):
    """ Create a copy of the board"""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return board


def find_queens(board):
    """ Find position of the queens on the board"""
    queen_Pos = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                queen_Pos.append([row, col])
                break
    return queen_Pos


def mark_spots(board, row, col):
    """Mark X out spots on the chessboard.

    Args:
        board (list): The current chessboard.
        r (int): The row
        c (int): The column
    """
    # Mark spots horizontally to the right
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark spots horizontally to the right
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark spots vertically downwards
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark spots vertically upwards
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark spots diagonally downwards to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark spots diagonally upwards to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Mark spots diagonally upwards to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark spots diagonally downwards to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_n_queens(board, row, num_queens, all_solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        board (list): current chessboard.
        row (int): The row being processed.
        num_queens (int): The number of queens placed.
        all_solutions (list): A list of all found solutions.
    """
    if num_queens == len(board):
        all_solutions.append(find_queens(board))
        return all_solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            new_board = board_copy(board)
            new_board[row][col] = "Q"
            mark_spots(new_board, row, col)
            all_solutions = solve_n_queens(new_board, row + 1,
                                           num_queens + 1, all_solutions)

    return all_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(int(sys.argv[1]))
    all_solutions = solve_n_queens(board, 0, 0, [])
    for solution in all_solutions:
        print(solution)
