import tty
import sys
from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.grid = self.create()
        self.cursor_row = 0
        self.cursor_col = 0

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

    def get_borders(self):
        return {
            'top': f'{self.WHITE_TEXT}' + ('\u2581' * (self.width + 2)) + '\n\r',
            'bottom': f'{self.WHITE_TEXT}' + ('\u2594' * (self.width + 2)) + '\n\r',
            'left': f'{self.WHITE_TEXT}\u2590',
            'right': f'{self.WHITE_TEXT}\u258C',
        }

    def draw_board(self):
        borders = self.get_borders()
        print(chr(27) + '[2J' + chr(27) + '[0;0H') # clears terminal
        rendered_board = f'\n{self.GREEN_TEXT}Let the Game Begin!\n(press CTRL-C to exit)\n\n{borders["top"]}{self.BLACK_BACKGROUND}'

        for row in self.grid:
            rendered_board += borders['left']
            for cell in row:
                rendered_state = cell.next_state or cell.state
                rendered_board += self.RENDERING_STRINGS[rendered_state]
            rendered_board += f'{borders["right"]}\n'

        print(rendered_board + self.TEXT_RESET + borders['bottom'])

    def process_keyboard_input(self):
        char = ord(sys.stdin.read(1)) # listen for arrow keys and get char code
        if char == 27: # Arrow keys process as a sequence of three characters
            next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
            if next1 == 91: # The second character in the arrow key sequence
                if next2 == 65:
                    return 'up'
                elif next2 == 66:
                    return 'down'
                elif next2 == 67:
                    return 'right'
                elif next2 == 68:
                    return 'left'
        elif char == 32:
            return 'space'
        elif char == 10 or char == 13:
            return 'enter'
        elif char == 3: # CTRL-C
            return 'exit'

    def move_cursor_up(self):
        if self.cursor_row > 0:
            self.cursor_row -= 1

    def move_cursor_down(self):
        if self.cursor_row < self.height - 1:
            self.cursor_row += 1

    def move_cursor_right(self):
        if self.cursor_col < self.width - 1:
            self.cursor_col += 1

    def move_cursor_left(self):
        if self.cursor_col > 0:
            self.cursor_col -= 1

    def toggle_cell_state(self):
        cell = self.grid[self.cursor_row][self.cursor_col]
        if cell.state is 'dead':
            cell.state = 'alive'
        elif cell.state is 'alive':
            cell.state = 'zombie'
        else:
            cell.state = 'dead'

    def handle_keypress(self, keypress, mode):
        if keypress is 'up':
            self.move_cursor_up()
        elif keypress is 'down':
            self.move_cursor_down()
        elif keypress is 'right':
            self.move_cursor_right()
        elif keypress is 'left':
            self.move_cursor_left()
        elif keypress is 'space':
            self.toggle_cell_state()
        elif keypress is 'enter':
            tty.tcsetattr(sys.stdin, tty.TCSAFLUSH, mode)
            return False
        elif keypress is 'exit':
            tty.tcsetattr(sys.stdin, tty.TCSAFLUSH, mode)
            raise KeyboardInterrupt
        return True

    def populate_board(self):
        mode = tty.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin)
        accepting_input = True
        borders = self.get_borders()

        instructions = (f'{self.TEXT_RESET}Navigate the board with the arrow keys.\n\r'
                        'Use Spacebar to select a cell and toggle between '
                        f'{self.BLACK_BACKGROUND}{self.WHITE_TEXT}dead{self.TEXT_RESET}, '
                        f'{self.WHITE_BACKGROUND}{self.BLACK_TEXT}alive{self.TEXT_RESET}, and '
                        f'{self.BLACK_BACKGROUND}{self.GREEN_TEXT}zombie{self.TEXT_RESET} states.\n\r'
                        'Press Enter to begin the game once you are done selecting your starting cells.\n\n\r')

        while accepting_input:
            rendered_board = f'{instructions}{borders["top"]}{self.BLACK_BACKGROUND}'
            for row in self.grid:
                rendered_board += borders['left']
                for cell in row:
                    if cell.row is self.cursor_row and cell.col is self.cursor_col:
                        rendered_board += self.CURSOR[cell.state]
                    else:
                        rendered_state = cell.next_state or cell.state
                        rendered_board += self.RENDERING_STRINGS[rendered_state]
                rendered_board += f'{borders["right"]}\n\r'

            print(chr(27) + '[2J' + chr(27) + '[0;0H') # clears terminal
            print(rendered_board + self.TEXT_RESET + borders['bottom'])

            keypress = self.process_keyboard_input()
            accepting_input = self.handle_keypress(keypress, mode)
