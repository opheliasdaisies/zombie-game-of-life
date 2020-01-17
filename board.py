import os
from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.grid = self.create()

    BLACK_BACKGROUND = '\u001b[40m'
    BLACK_TEXT = '\u001b[30m'
    WHITE_TEXT = '\u001b[37m'
    GREEN_TEXT = '\u001b[32m'
    UNICODE_BOX = '\u2588'
    TEXT_RESET = '\u001b[0m'

    RENDERING_STRINGS = {
        'dead': f'{BLACK_TEXT}{UNICODE_BOX}',   # black box
        'alive': f'{WHITE_TEXT}{UNICODE_BOX}',  # white box
        'zombie': f'{GREEN_TEXT}{UNICODE_BOX}', # green box
        'cursor': f'{WHITE_TEXT}X',             # white X
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
            rendered_board += '\n'

        print(rendered_board + self.TEXT_RESET)

    def populate_board(self, state):
        populating_cells = input(f'''Enter positions of starting {state} cells.\n
Format should be row_from_top,column_from_left. For example, the first cell is 1,1.\n
The second cell in the first row would be 1,2.\n
Multiple cells should be separated by spaces. So the two above cells would be inputted: 1,1 1,2\n
''')
        for cell in populating_cells.split(' '):
            coordinates = cell.split(',')
            self.grid[int(coordinates[0])-1][int(coordinates[1])-1].state = state
