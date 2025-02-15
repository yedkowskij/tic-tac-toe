from random import choice
import math


def impossible(board, size):
    """ Make the best possible move using the minimax algorithm """
    best_step, best_result = None, -math.inf

    # Try all available cells
    for i in range(size):
        for j in range(size):
            if isinstance(board[i][j], int):
                board[i][j] = "🟢"
                current_result = mini_max(board, size, is_max=False)
                board[i][j] = size * i + j + 1

                # Update the best move
                if current_result > best_result:
                    best_result = current_result
                    best_step = [i, j]

    # Make the best move if found
    if best_step:
        i, j = best_step
        board[i][j] = "🟢"


def mini_max(board, size, is_max):
    """ Minimax algorithm to find the best move """
    x = evaluate(board, size)
    if x is not None:
        return x

    if is_max:
        max_result = -math.inf
        for i in range(size):
            for j in range(size):
                if isinstance(board[i][j], int):
                    board[i][j] = "🟢"
                    current_result = mini_max(board, size, is_max=False)
                    board[i][j] = size * i + j + 1
                    if current_result > max_result:
                        max_result = current_result

        return max_result

    else:
        min_result = +math.inf
        for i in range(size):
            for j in range(size):
                if isinstance(board[i][j], int):
                    board[i][j] = "❌"
                    current_result = mini_max(board, size, is_max=True)
                    board[i][j] = size * i + j + 1
                    if current_result < min_result:
                        min_result = current_result

        return min_result


def evaluate(board, size):
    """ Evaluate the board state """
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] == "🟢":
            return 1
        elif len(set(row)) == 1 and row[0] == "❌":
            return -1

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if len(set(column)) == 1 and column[0] == "🟢":
            return 1
        elif len(set(column)) == 1 and column[0] == "❌":
            return -1

    # Check diagonals
    d1 = [board[i][i] for i in range(size)]
    d2 = [board[i][size - i - 1] for i in range(size)]

    for d in [d1, d2]:
        if len(set(d)) == 1 and d[0] == "🟢":
            return 1
        elif len(set(d)) == 1 and d[0] == "❌":
            return -1

    # Check for a tie
    if all(not isinstance(cell, int) for row in board for cell in row):
        return 0

    return None
