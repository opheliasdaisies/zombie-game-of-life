from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.rendered_board_as_list = []
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
            self.rendered_board_as_list.append([])
            while current_col < self.width:
                cell_state = 'dead'
                board[current_row].append(Cell(self, cell_state, current_row, current_col))
                self.rendered_board_as_list[current_row].append(self.RENDERING_STRINGS[cell_state])
                current_col = current_col + 1
            current_row = current_row + 1
            current_col = 0
        
        return board

    def draw_board(self):
        first_and_last_rows = '_' * (self.width + 2) + '\n'
        rendered_board = first_and_last_rows
        for row in self.rendered_board_as_list:
            rendered_board += '|' + ''.join(row) + '|\n'
        rendered_board += first_and_last_rows

        print(rendered_board)
