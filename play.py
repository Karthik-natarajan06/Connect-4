from engine.board import Board
from ai.minimax import minimax

AI_PLAYER=2
SEARCH_DEPTH=4

def play():
    board = Board()
    current_player = 1
    temp_player=1

    while (not board.check_win(temp_player) and not board.check_draw()):
        board.display()

        if current_player==AI_PLAYER:
            print(f"player {current_player} (AI) is thinking...")
            score, column = minimax(SEARCH_DEPTH, board, True, current_player, current_player, float("-inf"), float("inf"))
            board.drop_piece(column, current_player)
            print(f"player {current_player} (AI) played column {column}")
        else:
            while True:
                try:
                    column = int(input(f"player {current_player} enter the column you want to drop the token in "))
                except ValueError:
                    print("Invalid input! Letters are not allowed. Please try again.")
                    continue
                if column < 0 or column >= board.COLS:
                    print("That column doesn't exist, pick 0-6.")
                    continue
                if board.drop_piece(column, current_player) is not None:
                    break
                print(f"Column {column} is full, pick a different one.")

        temp_player=current_player
        if (current_player%2==0):
            current_player = 1
        else:
            current_player = 2
    
    if (board.check_win(temp_player)):
        print(f"Player {temp_player} won")
        board.display()
    
    if (board.check_draw()):
        print("draw")
        board.display()
    
if __name__ == "__main__":
    play()

