#Tic-Tac-Toe Game
This is a simple implementation of the classic game of Tic-Tac-Toe using the Python programming language and the Pygame library. The game supports both player vs. player (PvP) and player vs. AI modes, and it offers different levels of AI difficulty.

How to Run
Make sure you have Python 3 installed on your system.
Install the Pygame library by running the command: pip install pygame
Save the provided code in a file named tictactoe.py.
Open a terminal and navigate to the directory containing the tictactoe.py file.
Run the game by executing the command: python tictactoe.py
Gameplay
Game Modes
Press the 'g' key to toggle between player vs. player (PvP) and player vs. AI modes.
Press the '0' key to set the AI level to easy (random moves).
Press the '1' key to set the AI level to medium (minimax algorithm).
Controls
Left-click on an empty square to place your mark (X or O) on the board.
Press the 'r' key to restart the game.
Rules
The objective of the game is to form a horizontal, vertical, or diagonal line of three of your marks (X or O).
Players take turns placing their marks on the board.
The game ends when one player wins or the board is full (a draw).
Code Overview
The code consists of three main classes: Board, AI, and Game.
The Board class manages the game board, checks for wins and draws, and provides methods for marking squares.
The AI class handles AI logic and offers different levels of AI difficulty.
The Game class controls the gameplay loop, interactions, and user interface.
The game uses the Pygame library to create the graphical user interface and manage user input.
AI Difficulty Levels
Easy AI (Level 0): Makes random moves on the board.
Medium AI (Level 1): Uses the minimax algorithm to make smarter moves.
Credits
This implementation was created by Siddesh R Ohri as a simple showcase of Python programming and the Pygame library.

Feel free to modify and extend the code to add new features, improve the AI, or customize the game's appearance. Enjoy playing and experimenting with the code!
