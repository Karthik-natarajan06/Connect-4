from flask import Flask, request, jsonify, render_template
from engine.board import Board
from ai.minimax import minimax

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

    if board.drop_piece(column, HUMAN_PLAYER) is None:
        return jsonify({"error": "That column is full"}), 400

    if board.check_win(HUMAN_PLAYER):
        return jsonify({"board": board.grid, "status": "human_won"})

    if board.check_draw():
        return jsonify({"board": board.grid, "status": "draw"})

    score, ai_column = minimax(SEARCH_DEPTH, board, True, AI_PLAYER, AI_PLAYER, float("-inf"), float("inf"))
    board.drop_piece(ai_column, AI_PLAYER)

    if board.check_win(AI_PLAYER):
        return jsonify({"board": board.grid, "status": "ai_won"})

    if board.check_draw():
        return jsonify({"board": board.grid, "status": "draw"})

    return jsonify({"board": board.grid, "status": "ongoing"})

if __name__ == "__main__":
    app.run(debug=True)