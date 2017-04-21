def __make_row(rowdata, col, empty, full):
    items = [col] * (2 * len(rowdata) + 1)
    items[1::2] = (full if d else empty for d in rowdata)
    return ''.join(items)


def __make_board(queens, col="|", row="---", empty="   ", full=" X "):
    size = len(queens)
    bar = __make_row(queens, col, row, row)
    board = [bar] * (2 * size + 1)
    board[1::2] = (__make_row([i == q for i in range(size)], col, empty, full) for q in queens)
    return '\n'.join(board)


def draw_board(queens):
    print(__make_board(queens))
