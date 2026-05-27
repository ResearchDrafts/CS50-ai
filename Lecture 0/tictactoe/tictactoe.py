"""
Tic Tac Toe Player
"""

from copy import deepcopy
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
    x_count = 0
    o_count = 0
    if board == initial_state():
        return X
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_count +=1
                if board[i][j] == O:
                    o_count +=1
        if x_count > o_count:
            return O
        else:
            return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions
    # raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = deepcopy(board)
    if action not in actions(board):
        raise Exception("Invalid")
    else:
        board_copy[action[0]][action[1]] = player(board)
    return board_copy
    # raise NotImplementedError

# 00 01 02
# 10 11 12
# 20 21 22

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    else:        
        return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for a in actions(board):
            v = max(v, min_value(result(board,a)))
        return v
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for a in actions(board):
            v = min(v, max_value(result(board,a)))
        return v
    if player(board) == X:
        best_score = -math.inf
        best_action = None
        for a in actions(board):
            score = min_value(result(board, a))
            if score > best_score:
                best_score = score
                best_action = a
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for a in actions(board):
            score = max_value(result(board, a))
            if score < best_score:
                best_score = score
                best_action = a
        return best_action

    # raise NotImplementedError
