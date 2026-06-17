from engine.board import Board

def test_horizontal_win():
    board = Board()
    for col in range(4):
        board.drop_piece(col, 1)
    assert board.check_win(1) == True