#!/usr/bin/python3

"""Solves the N-queens puzzle: Chess grandmaster Judit Polgár tactics"""

import sys


def init_board(n):
    """define and initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """define and return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return (list(map(board_deepcopy, board)))
    return (board)


def get_solution(board):
    """define & return list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == "Q":
                solution.append([row, column])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for column in range(col + 1, len(board)):
        board[row][column] = "x"
    # X out all backwards spots
    for column in range(col - 1, -1, -1):
        board[row][column] = "x"
    # X out all spots below
    for base in range(row + 1, len(board)):
        board[base][col] = "x"
    # X out all spots above
    for base in range(row - 1, -1, -1):
        board[base][col] = "x"
    # X out all spots diagonally down to the right
    column = col + 1
    for base in range(row + 1, len(board)):
        if column >= len(board):
            break
        board[base][column] = "x"
        column += 1
    # X out all spots diagonally up to the left
    column = col - 1
    for base in range(row - 1, -1, -1):
        if column < 0:
            break
        board[base][column]
        column -= 1
    # X out all spots diagonally up to the right
    column = col + 1
    for base in range(row - 1, -1, -1):
        if column >= len(board):
            break
        board[base][column] = "x"
        column += 1
    # X out all spots diagonally down to the left
    column = col - 1
    for base in range(row + 1, len(board)):
        if column < 0:
            break
        board[base][column] = "x"
        column -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for column in range(len(board)):
        if board[row][column] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][column] = "Q"
            xout(tmp_board, row, column)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


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

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for game in solutions:
        print(game)
