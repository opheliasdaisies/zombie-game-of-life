from cell import Cell

class Board:
    
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.board = self.create()

    def create(self):
        current_row = 0
        current_col = 0
        board = []
        
        while current_row < self.height:
            board.append([])
            while current_col < self.width:
                board[current_row].append(Cell('dead', current_row, current_col))
                current_col = current_col + 1
            current_row = current_row + 1
            current_col = 0
        
        return board
