# from random import choice
from level_3_hard import hard

def medium(board, size):
    """ Make a move by blocking the player if winning move is possible """
    return hard(board, size, block_only=True)


# def medium(board, size):
#     # проверяем строки
#     for i in range(size):
#         if board[i].count("❌") == size - 1:
#             for j in range(size):
#                 if isinstance(board[i][j], int):
#                     board[i][j] = "🟢"
#                     return

#     # проверяем столбцы
#     for j in range(size):
#         column = [board[i][j] for i in range(size)]
#         if column.count("❌") == size - 1:
#             for i in range(size):
#                 if isinstance(board[i][j], int):
#                     board[i][j] = "🟢"
#                     return

#     # проверяем диагонали
#     d1 = [board[i][i] for i in range(size)]
#     d2 = [board[i][size - i - 1] for i in range(size)]

#     if d1.count("❌") == size - 1:
#         for i in range(size):
#             if isinstance(board[i][i], int):
#                 board[i][i] = "🟢"
#                 return

#     if d2.count("❌") == size - 1:
#         for i in range(size):
#             if isinstance(board[i][size - i -1], int):
#                 board[i][size - i - 1] = "🟢"
#                 return

#     available_moves = []
#     for i in range(size):
#         for j in range(size):
#             if isinstance(board[i][j], int):
#                 available_moves.append((i, j))

#     if available_moves:
#         i, j = choice(available_moves)
#         board[i][j] = "🟢"
#     else:
#         return
