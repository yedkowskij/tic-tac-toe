# Import required libraries
from tabulate import tabulate

# Import messages and game logic by difficulty
from messages import (
    welcome_message, size_message, level_message, your_turn_message,
    occupied, result_message, replay_message, clear
)
from level_1_easy import easy
from level_2_medium import medium
from level_3_hard import hard
from level_4_impossible import impossible


def main():
    """ Main game loop: starts and runs the game """
    while True:
        welcome_message()
        level = level_message()
        size = size_message(level)
        board = create_board(size)
        play_game(board, size, level)
        replay_message()


def create_board(size):
    """ Create a game board of given size """
    board = [[j + i * size + 1 for j in range(size)] for i in range(size)]
    return board


def print_board(board):
    """ Clear the screen and print the current game board """
    clear()
    print(tabulate(board, tablefmt="double_grid", colalign=("center", "center")))


def play_game(board, size, level):
    """ Main game flow between player and computer """
    while True:
        # Player move
        player_step(board, size)
        if check(board, size):
            print_board(board)
            result_message(result="win")
            break

        # Computer move
        computer_step(board, size, level)
        if check(board, size):
            print_board(board)
            result_message(result="lost")
            break

        # Check for a tie
        if all(not isinstance(cell, int) for row in board for cell in row):
            print_board(board)
            result_message(result="tie")
            break

        # Print the board
        print_board(board)


def player_step(board, size):
    """ Allow the player to make a move by choosing a valid cell """
    while True:
        step = your_turn_message(board, size)
        row = (step - 1) // size
        col = (step - 1) % size
        if isinstance(board[row][col], int):
            board[row][col] = "❌"
            break
        else:
            occupied()


def computer_step(board, size, level):
    """ Make the computer move based on difficulty level """
    levels = {
        1: easy,
        2: medium,
        3: hard,
        4: impossible,
    }
    levels.get(level)(board, size)


def check(board, size):
    """ Check if there is a winning combination """
    # Check rows
    for row in board:
        if len(set(row)) == 1:
            return True

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if len(set(column)) == 1:
            return True

    # Check diagonals
    d1 = [board[i][i] for i in range(size)]
    d2 = [board[i][size - i - 1] for i in range(size)]

    for d in [d1, d2]:
        if len(set(d)) == 1:
            return True

    return False


if __name__ == "__main__":
    main()
