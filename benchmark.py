import time
from engine.board import Board
from ai.minimax import minimax

board = Board()
depth = 6

start = time.time()
score, column = minimax(depth, board, True, 1, 1, float("-inf"), float("inf"))
end = time.time()

print(f"Best column: {column}, score: {score}")
print(f"Time taken: {end - start:.3f} seconds")