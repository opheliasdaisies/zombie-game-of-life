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
        rendered_board = f'{self.BLACK_BACKGROUND}'

        for row in self.grid:
            for cell in row:
                rendered_state = cell.next_state or cell.state
                rendered_board += self.RENDERING_STRINGS[rendered_state]
            rendered_board += '\n'

        print(rendered_board + self.TEXT_RESET)
