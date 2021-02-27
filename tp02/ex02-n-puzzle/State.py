from math import sqrt


class State:
    def __init__(self, board: list, empty: tuple, info: str):
        self.board = board
        self.empty = empty
        self.info = info

    def __str__(self):
        state = "Empty: " + str(self.empty) + " - " + self.info + "\n"
        for row in self.board:
            state += str(row) + "\n"
        return state


def clone_board(board):
    cloned = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        cloned.append(new_row)
    return cloned


def moveUp(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y - 1][x]
    new_board[y - 1][x] = 0
    return State(new_board, (x, y - 1), "Move Up")


def moveDown(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y + 1][x]
    new_board[y + 1][x] = 0
    return State(new_board, (x, y + 1), "Move Down")


def moveLeft(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y][x - 1]
    new_board[y][x - 1] = 0
    return State(new_board, (x - 1, y), "Move Left")


def moveRight(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y][x + 1]
    new_board[y][x + 1] = 0
    return State(new_board, (x + 1, y), "Move Right")


def expand(state: State, N):
    x, y = state.empty

    descendants = []

    if 0 < x < sqrt(N + 1) - 1:
        descendants.append(moveRight(state.board, x, y))
        descendants.append(moveLeft(state.board, x, y))
        if 0 < y < sqrt(N + 1) - 1:
            # it's on the middle, can move to the four sides
            descendants.append(moveUp(state.board, x, y))
            descendants.append(moveDown(state.board, x, y))
        elif y == 0:
            # it's on the middle of the top
            descendants.append(moveDown(state.board, x, y))
        else:
            # it's on the middle of the bottom
            descendants.append(moveUp(state.board, x, y))
    elif 0 < y < sqrt(N + 1) - 1:
        descendants.append(moveUp(state.board, x, y))
        descendants.append(moveDown(state.board, x, y))
        if x == 0:
            # it's on the middle of the left
            descendants.append(moveRight(state.board, x, y))
        else:
            # it's on the middle of the right
            descendants.append(moveLeft(state.board, x, y))
    elif y == 0:
        descendants.append(moveDown(state.board, x, y))
        if x == 0:
            # top left corner
            descendants.append(moveRight(state.board, x, y))
        else:
            # top right corner
            descendants.append(moveLeft(state.board, x, y))
    else:
        descendants.append(moveUp(state.board, x, y))
        if x == 0:
            # bottom left corner
            descendants.append(moveRight(state.board, x, y))
        else:
            # bottom right corner
            descendants.append(moveLeft(state.board, x, y))

    return descendants


def h1(board):
    h = 0
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 0:
                continue
            if y * len(board) + x != col - 1:
                h += 1
    return h


def h2(board):
    h = 0
    goal = [[len(board) * y + x for x in range(1, len(board) + 1)] for y in range(0, len(board))]
    goal[len(board)-1][len(board)-1] = 0

    import math

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            bij = board[i][j]
            i_b = i
            j_b = j

            for i_g, r in enumerate(goal):
                for j_g, c in enumerate(r):
                    if c == bij:
                        h += (math.fabs(i_g - i_b) + math.fabs(j_g - j_b))

    return h