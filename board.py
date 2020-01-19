import os
import tty
import sys
from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.grid = self.create()

    BLACK_BACKGROUND = '\u001b[40m'
    WHITE_BACKGROUND = '\u001b[47m'
    GREEN_BACKGROUND = '\u001b[42m'
    BLACK_TEXT = '\u001b[30m'
    WHITE_TEXT = '\u001b[37m'
    GREEN_TEXT = '\u001b[32m'
    RED_TEXT = '\u001b[31m'
    UNICODE_BOX = '\u2588'
    TEXT_RESET = '\u001b[0m'

    RENDERING_STRINGS = {
        'dead': f'{BLACK_TEXT}{UNICODE_BOX}',   # black box
        'alive': f'{WHITE_TEXT}{UNICODE_BOX}',  # white box
        'zombie': f'{GREEN_TEXT}{UNICODE_BOX}', # green box
    }

    CURSOR = {
        'dead': f'{RED_TEXT}X',
        'alive': f'{WHITE_BACKGROUND}{RED_TEXT}X{BLACK_BACKGROUND}',
        'zombie': f'{GREEN_BACKGROUND}{RED_TEXT}X{BLACK_BACKGROUND}',
    }

    def create(self):
        current_row = 0
        current_col = 0
        board = []
        
        while current_row < self.height:
            board.append([])
            while current_col < self.width:
                cell_state = 'dead'
                board[current_row].append(Cell(self, cell_state, current_row, current_col))
                current_col = current_col + 1
            current_row = current_row + 1
            current_col = 0
        
        return board

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        rendered_board = f'{self.BLACK_BACKGROUND}'

        for row in self.grid:
            for cell in row:
                rendered_state = cell.next_state or cell.state
                rendered_board += self.RENDERING_STRINGS[rendered_state]
            rendered_board += '\n\u001b[1000D' # New line and move cursor to the left (1000 characters)

        print(rendered_board + self.TEXT_RESET)

    def populate_board(self):
        mode = tty.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin)
        cursor_row = 0
        cursor_col = 0

        instructions = ('Navigate the board with the arrow keys.\n\r'
                        'Use Spacebar to select a cell and toggle between '
                        f'{self.BLACK_BACKGROUND}{self.WHITE_TEXT}dead{self.TEXT_RESET}, '
                        f'{self.WHITE_BACKGROUND}{self.BLACK_TEXT}alive{self.TEXT_RESET}, and '
                        f'{self.BLACK_BACKGROUND}{self.GREEN_TEXT}zombie{self.TEXT_RESET} states.\n\r'
                        'Press Enter to begin the game once you are done selecting your starting cells.\n\n\r')

        while True: # continue taking input
            rendered_board = f'{instructions}{self.BLACK_BACKGROUND}'
            for row in self.grid:
                for cell in row:
                    if cell.row is cursor_row and cell.col is cursor_col:
                        rendered_board += self.CURSOR[cell.state]
                    else:
                        rendered_state = cell.next_state or cell.state
                        rendered_board += self.RENDERING_STRINGS[rendered_state]
                rendered_board += '\n\r'

            os.system('cls' if os.name == 'nt' else 'clear')
            print(rendered_board + self.TEXT_RESET)

            char = ord(sys.stdin.read(1)) # listen for arrow keys and get char code
            if char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 65: # Up
                        if cursor_row > 0:
                            cursor_row -= 1
                    elif next2 == 66: # Down
                        if cursor_row < self.height - 1:
                            cursor_row += 1
                    elif next2 == 67: # Right
                        if cursor_col < self.width - 1:
                            cursor_col += 1
                    elif next2 == 68: # Left
                        if cursor_col > 0:
                            cursor_col -= 1
            elif char == 32: # Space
                cell = self.grid[cursor_row][cursor_col]
                if cell.state is 'dead':
                    cell.state = 'alive'
                elif cell.state is 'alive':
                    cell.state = 'zombie'
                else:
                    cell.state = 'dead'
            elif char == 10 or char == 13: # Enter
                tty.tcsetattr(sys.stdin, tty.TCSAFLUSH, mode)
                return
