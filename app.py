from flask import Flask, request, jsonify, render_template
from engine.board import Board
from ai.minimax import minimax, get_valid_columns
import random

app = Flask(__name__)
board = Board()
HUMAN_PLAYER = 1
AI_PLAYER = 2
SEARCH_DEPTH = 6

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    column = request.json["column"]
    depth = request.json.get("depth", SEARCH_DEPTH)

    if board.drop_piece(column, HUMAN_PLAYER) is None:
        return jsonify({"error": "That column is full"}), 400

    if board.check_win(HUMAN_PLAYER):
        return jsonify({"board": board.grid, "status": "human_won"})

    if board.check_draw():
        return jsonify({"board": board.grid, "status": "draw"})

    score, ai_column = minimax(depth, board, True, AI_PLAYER, AI_PLAYER, float("-inf"), float("inf"))

    if depth <= 2 and random.random() < 0.4:
        ai_column = random.choice(get_valid_columns(board))

    board.drop_piece(ai_column, AI_PLAYER)

    if board.check_win(AI_PLAYER):
        return jsonify({"board": board.grid, "status": "ai_won"})

    if board.check_draw():
        return jsonify({"board": board.grid, "status": "draw"})

    return jsonify({"board": board.grid, "status": "ongoing"})

@app.route("/reset", methods=["POST"])
def reset():
    global board
    board = Board()
    return jsonify({"board": board.grid, "status": "ongoing"})

if __name__ == "__main__":
    app.run(debug=True)