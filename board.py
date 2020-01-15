from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.grid = self.create()

    RENDERING_STRINGS = {
        'dead': '.',
        'alive': 'o',
        'zombie': 'x',
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
        border_row = '_' * (self.width + 2) + '\n'

        rendered_board = border_row

        for row in self.grid:
            rendered_board += '|'
            for cell in row:
                rendered_state = cell.next_state or cell.state
                rendered_board += self.RENDERING_STRINGS[rendered_state]
            rendered_board += '|\n'
        rendered_board += border_row

        print(rendered_board)
