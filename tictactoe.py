#Shebang command to make it into an executable
#!python3   
import copy
import random
import sys
import pygame
import random
import numpy as np
from constants import *

# PYGAME SET-UP
# Initializing the game modulea
pygame.init()

# Assigning the height and width of the display screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the caption of the screen
pygame.display.set_caption('TIC TAC TOE')

# Fill the screen with the background colourscreen.fill(BG_COLOR)

class Board:
    def __init__(self):
        """
        Initializes an instance of the class.

        - squares: numpy array
            Stores the positions of the squares in a tuple.

        - empty_sqrs: numpy array
            A list of empty squares. (Initially set as the same array as 'squares'.)

        - marked_sqrs: int
            The number of squares that have been marked.

        """
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def check_vertical_wins(self, squares, show):
        for col in range(COLS):
            if squares[0][col] == squares[1][col] == squares[2][col] != 0:
                if show:
                    self.draw_vertical_line(col)
                return squares[0][col]
        return 0

    def draw_vertical_line(self, col):
        color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
        iPos = (col * SQSIZE + SQSIZE // 2, 20)
        fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
        pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)

    def check_horizontal_wins(self, squares, show):
        for row in range(ROWS):
            if squares[row][0] == squares[row][1] == squares[row][2] != 0:
                if show:
                    self.draw_horizontal_line(row)
                return squares[row][0]
        return 0

    def draw_horizontal_line(self, row):
        color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
        iPos = (20, row * SQSIZE + SQSIZE // 2)
        fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
        pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)

    def check_descending_diagonal(self, squares, show):
        if squares[0][0] == squares[1][1] == squares[2][2] != 0:
            if show:
                self.draw_descending_diagonal()
            return squares[1][1]
        return 0

    def draw_descending_diagonal(self):
        color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
        iPos = (20, 20)
        fPos = (WIDTH - 20, HEIGHT - 20)
        pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)

    def check_ascending_diagonal(self, squares, show):
        if squares[2][0] == squares[1][1] == squares[0][2] != 0:
            if show:
                self.draw_ascending_diagonal()
            return squares[1][1]
        return 0

    def draw_ascending_diagonal(self):
        color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
        iPos = (20, HEIGHT - 20)
        fPos = (WIDTH - 20, 20)
        pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)

    def final_state(self, show=False):
        """
        Determines the final state of the tic-tac-toe game.

        - show: bool, optional
            Specifies whether to visually show the winning line. Defaults to False.

        Returns:
        - int
            The final state of the game:
            - 0: The game is a draw.
            - 1: Player 1 (represented by crosses) has won.
            - 2: Player 2 (represented by circles) has won.

        """

        result = self.check_vertical_wins(self.squares, show)
        if result:
            return result

        result = self.check_horizontal_wins(self.squares, show)
        if result:
            return result

        result = self.check_descending_diagonal(self.squares, show)
        if result:
            return result

        result = self.check_ascending_diagonal(self.squares, show)
        if result:
            return result

        # Draws
        return 0

    def mark_sqr(self, row, col, player):
        """
        Marks a square on the tic-tac-toe game board with the specified player's mark.

        Parameters:
        - row: int
            The row index of the square to be marked.

        - col: int
            The column index of the square to be marked.

        - player: int
            The player identifier whose mark will be placed on the square.
            - 1: Player 1 (represented by crosses).
            - 2: Player 2 (represented by circles).

        """
        self._update_square(row, col, player)
        self._update_marked_sqrs()

    def _update_square(self, row, col, player):
        self.squares[row][col] = player

    def _update_marked_sqrs(self):
        self.marked_sqrs = np.count_nonzero(self.squares)

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        """
        Finds and returns a list of empty squares on the tic-tac-toe game board.

        Returns:
        - empty_sqrs: list
            A list of tuples representing the coordinates of empty squares.
            Each tuple contains two values:
                - row: int
                    The row index of the empty square.
                - col: int
                    The column index of the empty square.

        """
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def isfull(self):
        return self._is_marked_sqrs_equal(9)

    def isempty(self):
        return self._is_marked_sqrs_equal(0)

    def _is_marked_sqrs_equal(self, value):
        return self.marked_sqrs == value

class AI:
    def __init__(self, level = 1, player = 2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self, board, maximizing):
        case = board.final_state()

        if case == 1:
            return 1, None
        elif case == 2:
            return -1, None
        elif board.isfull():
            return 0, None

        if maximizing:
            return self.maximize(board)
        else:
            return self.minimize(board)

    def maximize(self, board):
        max_eval = -100
        best_move = None
        empty_sqrs = board.get_empty_sqrs()

        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_sqr(row, col, 1)
            eval, _ = self.minimax(temp_board, False)
            if eval > max_eval:
                max_eval = eval
                best_move = (row, col)

        return max_eval, best_move

    def minimize(self, board):
        min_eval = 100
        best_move = None
        empty_sqrs = board.get_empty_sqrs()

        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_sqr(row, col, self.player)
            eval, _ = self.minimax(temp_board, True)
            if eval < min_eval:
                min_eval = eval
                best_move = (row, col)

        return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            return self.random_choice(main_board)
        else:
            return self.minimax_choice(main_board)

    def random_choice(self, main_board):
        eval = 'random'
        move = self.rnd(main_board)
        print(f'AI has chosen to mark the square in pos {move} with an eval of {eval}')
        return move

    def minimax_choice(self, main_board):
        eval, move = self.minimax(main_board, False)
        print(f'AI has chosen to mark the square in pos {move} with an eval of {eval}')
        return move


class Game:
    def __init__(self):

        # Calling the function to draw the board
        self.board = Board()

        self.ai = AI()

        # Checks for which player is playing
        self.player = 1

        self.gamemode = 'ai'

        self.running = True

        # Prints the lines on the screen board
        self.show_lines()

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        # Switches the turn to the next player
        self.next_turn()

    def show_lines(self):
        #BG
        screen.fill(BG_COLOR)

        # Vertical Lines
        # Syntax pygame,draw,line(SURFACE, COLOUR, STARTING_COOR, ENDING_COOR, LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE, 0), (WIDTH-SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal Lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT-SQSIZE), (WIDTH, HEIGHT-SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        """
        Draws the player's mark (cross or circle) on the specified position of the game board.

        Parameters:
        - row: int
            The row index of the square where the mark is to be drawn.

        - col: int
            The column index of the square where the mark is to be drawn.

        """
        if self.player == 1:
            # Drawing a CROSS
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE +  OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # Drawing a CIRCLE
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        if self.gamemode == 'pvp':
            self.gamemode = 'ai'
        else:
            self.gamemode = 'pvp'

    def isover(self):
        return self.board.final_state(show = True) != 0 or self.board.isfull()

    def reset(self):
        self.__init__()

# The main function of the program
def tictactoe():

    # Creates a Game object
    game = Game()
    board = game.board
    ai = game.ai

    #MainLoop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # g- gamemode
                if event.key == pygame.K_g:
                     game.change_gamemode()
                 # r-restart
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai
                    # 0-random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                # 1-random ai
                if event.key == pygame.K_1:
                     ai.level = 1

            # Checks for the coordinates (in pixels) of the square upon a click
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Converts the pixels to the coordinates of rows and columns
                # Stores the positions of the click on the square
                pos = event.pos

                # Stores the value in the Y-Axis of the board
                row = pos[1] // SQSIZE

                # Stores the value in the X-Axis of the board
                col = pos[0] // SQSIZE

                # Checks for the empty square
                if board.empty_sqr(row,col) and game.running:
                    # Marks the squares on the board according to PLAYER - 1
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()

            # AI Methods
            row, col = ai.eval(board)
            game.make_move(row, col)
            if game.isover():
                game.running = False

        pygame.display.update()

# Calling the main function
tictactoe()
