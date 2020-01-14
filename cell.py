from board import Board

class Cell:
    #other variables: count_live_neighbors, count_zombie_neighbors
    def __init__(self, board, state, row, col):
        self.board = board
        self.state = state
        self.previous_state = None
        self.row = row
        self.col = col
        self.count_alive_neighbors = 0
        self.count_zombie_neighbors = 0

    def adjust_neighbor_population_count(self, neighboring_cell):
        if self.previous_state is 'alive':
            neighboring_cell.count_alive_neighbors =- 1
        if self.previous_state is 'zombie':
            neighboring_cell.count_zombie_neighbors =- 1
        if self.state is 'alive':
            neighboring_cell.count_alive_neighbors =+ 1
        if self.state is 'zombie':
            neighboring_cell.count_zombie_neighbors =+ 1

    def update_neighboring_cells(self):
        board = self.board.board
        board[self.row-1][self.col-1]
        board[self.row-1][self.col]
        board[self.row-1][self.col+1]
        board[self.row][self.col-1]
        board[self.row][self.col+1]
        board[self.row+1][self.col-1]
        board[self.row+1][self.col]
        board[self.row+1][self.col+1]

    def update_state(self):
        self.previous_state = self.state
        if self.previous_state == 'alive':
            if self.count_live_neighbors < 2 or self.count_live_neighbors > 3:
                self.state = 'dead'
                # TODO: if no zombies on the board, 5% chance of becoming a zombie
            if self.count_zombie_neighbors > 1:
                self.state = 'zombie'
        if self.previous_state == 'dead':
            if self.count_live_neighbors is 3:
                self.state = 'alive'
        if self.previous_state == 'zombie':
            if self.count_live_neighbors > 2:
                self.state = 'dead'

        if self.previous_state is not self.state:
            self.update_neighboring_cells()
