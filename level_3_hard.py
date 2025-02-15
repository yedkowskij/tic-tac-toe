from random import choice

def hard(board, size, block_only=False):
    """ Same logic as in medium but first tries to win by completing a line """
    # Define the symbols to check for potential moves
    symbols = ["❌"] if block_only else ["🟢", "❌"]

    for symbol in symbols:
        # Check rows
        for i in range(size):
            if board[i].count(symbol) == size - 1:
                for j in range(size):
                    if isinstance(board[i][j], int):
                        board[i][j] = "🟢"
                        return

        # Check columns
        for j in range(size):
            column = [board[i][j] for i in range(size)]
            if column.count(symbol) == size - 1:
                for i in range(size):
                    if isinstance(board[i][j], int):
                        board[i][j] = "🟢"
                        return

        # Check diagonals
        d1 = [board[i][i] for i in range(size)]
        d2 = [board[i][size - i - 1] for i in range(size)]

        if d1.count(symbol) == size - 1:
            for i in range(size):
                if isinstance(board[i][i], int):
                    board[i][i] = "🟢"
                    return

        if d2.count(symbol) == size - 1:
            for i in range(size):
                if isinstance(board[i][size - i -1], int):
                    board[i][size - i - 1] = "🟢"
                    return

    # If no winning or blocking move is possible, choose a random line
    available_moves = []
    for i in range(size):
        for j in range(size):
            if isinstance(board[i][j], int):
                available_moves.append((i, j))

    if available_moves:
        i, j = choice(available_moves)
        board[i][j] = "🟢"
    else:
        return
