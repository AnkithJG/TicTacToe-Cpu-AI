"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state():
        return X

    if terminal(board):
        return None

    countX = 0
    countO = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                countX += 1
            elif board[i][j] == "O":
                countO += 1

    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return None

    ret = set()


    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                ret.add((i, j))

    return ret


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    all = actions(board)

    if action not in all:
        raise ValueError("Invalid Action")

    play = player(board)
    dummy = copy.deepcopy(board)

    for i in range(len(dummy)):
        for j in range(len(dummy[i])):
            if (i, j) == action:
                dummy[i][j] = play

    return dummy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] is not None:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][0] is not None:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][0] is not None:
        return board[0][2]
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] is not None:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] is not None:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] is not None:
        return board[2][0]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)

    if win == "X" or win == "O":
        return True

    count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                count += 1

    if count == 9:
        return True

    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    play = player(board)

    if play == "X":
        val = -float("inf")
        best = None
        for action in actions(board):
            v = minValue(result(board, action), -float("inf"), float("inf"))
            if v > val:
                val = v
                best = action
    elif play == "O":
        val = float("inf")
        best = None
        for action in actions(board):
            v = maxValue(result(board, action), -float("inf"), float("inf"))
            if v < val:
                val = v
                best = action

    return best


def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -float("inf")

    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v

def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float("inf")

    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v