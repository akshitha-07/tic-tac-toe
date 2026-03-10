"""
Tic Tac Toe Player
"""

import math
import copy
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==X:
                x_count += 1
            elif board[i][j]==O:
                o_count += 1
    
    if(x_count<=o_count):
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possibilities.add((i,j))
    
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
   lines = [
       # rows
       [board[0][0], board[0][1], board[0][2]],
       [board[1][0], board[1][1], board[1][2]],
       [board[2][0], board[2][1], board[2][2]],
       # columns
       [board[0][0], board[1][0], board[2][0]],
       [board[0][1], board[1][1], board[2][1]],
       [board[0][2], board[1][2], board[2][2]],
       # diagonals
       [board[0][0], board[1][1], board[2][2]],
       [board[0][2], board[1][1], board[2][0]],
   ]

   for line in lines:
       if line[0] == line[1] == line[2] and line[0] != EMPTY:
           return line[0]
  
   return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!= None:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        best_score = float('-inf')
        best_action = None
        for action in actions(board):
            score = min_value(result(board,action))
            if score>best_score:
                best_score = score
                best_action = action
        return best_action

    else:
        best_score = float('inf')
        best_action = None
        for action in actions(board):
            score = max_value(result(board,action))
            if score<best_score:
                best_score = score
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v,min_value(result(board,action)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v,max_value(result(board,action)))

    return v
