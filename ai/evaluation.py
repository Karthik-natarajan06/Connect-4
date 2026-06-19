from engine.board import Board

ROWS, COLS = Board.ROWS, Board.COLS

BOARD_SCORE = [[0] * COLS for _ in range(ROWS)]
for r in range(ROWS):
    for c in range(COLS):
        if  c ==0 or c==6:
            BOARD_SCORE[r][c]=1
        elif c==1 or c==5:
            BOARD_SCORE[r][c]=2
        elif c==2 or c==4:
            if r%2==0:
                BOARD_SCORE[r][c]=4
            else:
                BOARD_SCORE[r][c]=3
        elif c==3:
            if r==2 or r==3:
                BOARD_SCORE[r][c]=5
            else:
                BOARD_SCORE[r][c]=4  

def player_score(board, player_tocken):
    score = 0
    for r in range(ROWS):
        for c in range(COLS):
            if board.grid[r][c] == player_tocken:
                score += BOARD_SCORE[r][c]
    return score  

def evaluate(board, player):
    opponent = 2 if player == 1 else 1
    if board.check_win(player):
        return 1000000
    if board.check_win(opponent):
        return -1000000
    if board.check_draw():
        return 0
    return player_score(board, player) - player_score(board, opponent) + threat_score(board, player)


def score_window(window, player, opponent):
    player_count = window.count(player)
    opp_count = window.count(opponent)
    empty_count = window.count(0)

    score = 0
    if player_count == 3 and empty_count == 1:
        score += 50      # player is one move from winning here
    elif player_count == 2 and empty_count == 2:
        score += 10      # building toward something

    if opp_count == 3 and empty_count == 1:
        score -= 60      # opponent is one move from winning — block this
    
    return score

def threat_score(board, player):
    opponent = 2 if player == 1 else 1
    total = 0

    # horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            window = [board.grid[r][c + i] for i in range(4)]
            total += score_window(window, player, opponent)

    # Vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            window = [board.grid[r + i][c] for i in range(4)]
            total += score_window(window, player, opponent)

    # Diagonal (top-left to bottom-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board.grid[r + i][c + i] for i in range(4)]
            total += score_window(window, player, opponent)
    
    # Diagonal (bottom-left to top-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board.grid[r - i][c + i] for i in range(4)]
            total += score_window(window, player, opponent)

    return total