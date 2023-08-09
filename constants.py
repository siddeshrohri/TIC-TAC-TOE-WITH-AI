"""
Initializes the constants used in the game, such as screen dimensions, board size, line width, circle width, cross width,
circle radius, offset, and colors.

"""
# SCREEN
# Initializing the Width of the screen
WIDTH = 600
# Initializing the Height of the screen
HEIGHT = 600

#BOARD
# Initializing the No.of Rows of the board
ROWS = 3
# Initializing the No.of Columns of the board
COLS = 3
# Calculate the size of each Square on the board
SQSIZE = WIDTH // COLS

#WIDTH
# Initialize the Width of the LINE
LINE_WIDTH = 15
# Initialize the Width of the CIRCLE
CIRC_WIDTH = 15
# Initialize the Width of the CROSS
CROSS_WIDTH = 20
# Calculate the Radius of the CIRCLE
RADIUS = SQSIZE // 4
OFFSET = 50

#COLOR
# RGB format to define the colours
# Initialize the Background Color
BG_COLOR = (255, 255, 255)
# Initialize the Line Color
LINE_COLOR = (0, 0, 0)
# Initialize the Circle Color
CIRC_COLOR = (255, 0, 0)
#Initialize the Cross Color
CROSS_COLOR = (0, 0, 255)