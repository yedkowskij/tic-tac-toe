import pytest
from project import easy, medium, check, player_step, create_board, print_board


def test_easy():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    easy(board, 3)
    assert board[0][0] == "🟢"

    board = [
        ["❌", "❌", 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    easy(board, 3)
    assert board[0][2] == "🟢"


def test_medium():
    board = [
        ["❌", "❌", 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    medium(board, 3)
    assert board[0][2] == "🟢"
    assert board[2][1] == 8

    board = [
        ["❌", 2, 3],
        ["❌", 5, 6],
        [7, 8, 9]
    ]
    medium(board, 3)
    assert board[2][0] == "🟢"
    assert board[2][1] == 8

    board = [
        ["❌", 2, 3],
        [4, "❌", 6],
        [7, 8, 9]
    ]
    medium(board, 3)
    assert board[2][2] == "🟢"


def test_check():
    board = [
        ["❌", "❌", "❌"],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert check(board, 3) == True

    board = [
        ["🟢", "🟢", "🟢"],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert check(board, 3) == True

    board = [
        ["🟢", "❌", "🟢"],
        ["❌", "🟢", "❌"],
        ["❌", "🟢", "❌"]
    ]
    assert check(board, 3) == False


def test_player_step():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert board[1][1] == 5
    assert board[0][0] == 1
    assert board[2][2] == 9
    assert board == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


def test_create_board():
    board = create_board(3)
    assert len(board) == 3
    assert len(board[0]) == 3
    assert board[0][0] == 1
    assert board[1][2] == 6

    board = create_board(5)
    assert len(board) == 5
    assert len(board[0]) == 5
    assert board[0][0] == 1
    assert board[1][2] == 8

    board = create_board(2)
    assert len(board) == 2
    assert len(board[0]) == 2
    assert board[0][0] == 1
    assert board[1][1] == 4


def test_print_board():
    board = [
        [1, 2, 3],
        [4, "❌", 6],
        [7, 8, "🟢"]
    ]
    assert board[1][1] == "❌"
    assert board[2][2] == "🟢"

    board = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    assert board[4][4] == 25
    assert board[3][2] == 18
