# Connect-4
A Connect-4 engine with an AI opponent using minimax and alpha-beta pruning, plus a playable web interface.

# Connect-4

A Connect-4 engine with an AI opponent using minimax and alpha-beta pruning, plus a playable web interface.

## Overview

This project implements a complete Connect-4 game with an AI opponent built from classical search algorithms rather than a pre-trained model or external API. The core engine handles board state, legal move generation, and win/draw detection, while the AI uses minimax search with alpha-beta pruning and move ordering to choose strong moves efficiently. A web interface lets a human play against the AI at adjustable difficulty.

## Features

- [ ] Full Connect-4 rules engine (move validation, win/draw detection)
- [ ] Minimax AI with adjustable search depth
- [ ] Alpha-beta pruning for faster search
- [ ] Move ordering to improve pruning efficiency
- [ ] Transposition table to cache evaluated positions
- [ ] Web interface to play against the AI
- [ ] Difficulty selector (tied to search depth)

## Tech stack

- Python (game engine, AI logic)
- Flask (backend)
- HTML/CSS/JavaScript (frontend)

## Installation

```bash
git clone https://github.com/Karthik-natarajan06/connect-4.git
cd connect-4
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

## License

MIT
