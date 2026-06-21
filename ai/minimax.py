from engine.board import Board
from ai.evaluation import evaluate
import copy

def get_valid_columns(board):
    COLS = Board.COLS
    return [c for c in range(COLS) if board.grid[0][c] == 0]

def clone_board(board):
    new_board = Board()
    new_board.grid = copy.deepcopy(board.grid)
    return new_board

def minimax(depth, board, maximizing, ai_player, current_player, alpha, beta):
    opponent = 2 if ai_player == 1 else 1

    if (depth<=0 or board.check_win(ai_player) or board.check_win(opponent) or board.check_draw()):
        return (evaluate(board, ai_player), None)
    
    valid_columns = get_valid_columns(board)
    best_column = valid_columns[0]

    if maximizing:
        best_score=float("-inf")
        for c in valid_columns:
            temp_board=clone_board(board)
            temp_board.drop_piece(c, current_player)
            temp_score, _= minimax(depth-1, temp_board, False, ai_player, opponent, alpha, beta)
            alpha = max(alpha, temp_score)
            if temp_score>best_score:
                best_score=temp_score
                best_column=c
            if alpha >=beta:
                break
    else:
        best_score = float("inf")
        for c in valid_columns:
            temp_board=clone_board(board)
            temp_board.drop_piece(c, current_player)
            temp_score, _= minimax(depth-1, temp_board, True, ai_player, ai_player, alpha, beta)
            beta = min(beta, temp_score)
            if temp_score<best_score:
                best_score=temp_score
                best_column=c
            if alpha >= beta:
                break

    return best_score, best_column