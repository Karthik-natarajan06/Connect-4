from ai.minimax import minimax
from engine.board import Board

def test_minimax_returns_valid_move_on_empty_board():
    board = Board()
    score, column = minimax(4, board, True, 1, 1)
    assert column in range(board.COLS)

def test_minimax_takes_winning_move():
    board = Board()
    board.drop_piece(0, 1)
    board.drop_piece(1, 1)
    board.drop_piece(2, 1)
    score, column = minimax(4, board, True, 1, 1)
    assert column == 3

def test_minimax_blocks_opponent_winning_move():
    board = Board()
    board.drop_piece(0, 2)
    board.drop_piece(1, 2)
    board.drop_piece(2, 2)
    score, column = minimax(4, board, True, 1, 1)
    assert column == 3