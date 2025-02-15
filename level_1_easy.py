def easy(board, size):
    """ Make a simple move by chosing first available cell """
    for i in range(size):
        for j in range(size):
            if isinstance(board[i][j], int):
                board[i][j] = "🟢"
                return
