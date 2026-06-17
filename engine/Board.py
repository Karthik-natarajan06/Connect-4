class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        # 6 rows and 7 columns grid filled with 0 (empty)
        self.grid = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def drop_piece(self, column, player):
        """
        Drop a piece into a column.
        player = 1 or 2
        """
        if column < 0 or column >=self.COLS:
            raise ValueError("Invalid column")
        
        #start from bottom row
        for row in range(self.ROWS-1, -1, -1):
            if self.grid[row][column]==0:
                self.grid[row][column] = player
                return row  # return where it landed
            
        #column fail
        return False
    
    def check_win(self, player):
        # Horizontal
        for r in range(self.ROWS):
            for c in range(self.COLS-3):
                if all(self.grid[r][c + i] == player for i in range(4)):
                    return True
                
        # Vertical
        for c in range(self.COLS):
            for r in range(self.ROWS-3):
                if all(self.grid[r + i][c] == player for i in range(4)):
                    return True
                
        # Diagonal (top-left to bottom-right)
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if all(self.grid[r + i][c + i] == player for i in range(4)):
                    return True
        
        # Diagonal (bottom-left to top-right)
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.grid[r - i][c + i] == player for i in range(4)):
                    return True
                
        return False
    
    def check_draw(self):
        # if any empty cell exists, not a draw
        for row in self.grid:
            if 0 in row:
                return False
        return True
    
    def display(self):
        symbols = {0: "[]", 1: "X", 2: "O"}

        for row in self.grid:
            print(" ".join(symbols[cell] for cell in row))

        print("0 1 2 3 4 5 6")
