# LetterStorm

LetterStorm is a fun and interactive game where random letters fall from the top of the screen and the player needs to type the corresponding letters to score points. The game includes a beautiful background, sound effects, and a simple start screen.

## Features

- Random letters fall from the top of the screen.
- Players type the correct letters to score points.
- Sound effects play when a player scores.
- The game has a start screen and a game over screen.

## Requirements

- Python 3.x
- `pygame` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/daviddagyei/LetterStorm.git
    cd LetterStorm
    ```

2. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install pygame
    ```

## Running the Game

1. Ensure you are in the root directory of the repository where `fall.py` is located.

2. Run the game using the following command:

    ```bash
    python fall.py
    ```

## Game Instructions

- Press any key to start the game.
- Type the falling letters before they reach the bottom of the screen.
- Each correct input scores points.
- The game ends if three letters are missed.

## Assets

Place your background image in the `assets/images` directory with the filename `background.png`.

Place your sound effect file in the `assets/sounds` directory with the filename `score.wav`.

## Repository Structure

