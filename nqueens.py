def solve(row):
    if row == n:
        print(board)
        return True

    for col in range(n):
        if col not in board and all(abs(col-c) != row-r
                                    for r, c in enumerate(board)):
            board.append(col)

            if solve(row + 1):
                return True

            board.pop()

    return False


n = 4
board = []
solve(0)
