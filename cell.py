from random import randrange

class Cell:
    #other variables: count_live_neighbors, count_zombie_neighbors
    def __init__(self, board, state, row, col):
        self.board = board
        self.state = state
        self.next_state = None
        self.row = row
        self.col = col
        self.count_alive_neighbors = 0
        self.count_zombie_neighbors = 0
        self.neighbors = self.get_neighbors()

    def get_neighbor_state(self, neighboring_cell):
        if neighboring_cell.state is 'alive':
            self.count_alive_neighbors += 1
        if neighboring_cell.state is 'zombie':
            self.count_zombie_neighbors += 1

    def find_horizontal_neighbors(self, row_offset):
        horiz_neighbors = []
        if self.col > 0:
            horiz_neighbors.append((self.row+row_offset, self.col-1))
        if self.col < self.board.width-1:
            horiz_neighbors.append((self.row+row_offset, self.col+1))
        return horiz_neighbors

    def get_neighbors(self):
        neighbor_coordinates = []

        neighbor_coordinates += self.find_horizontal_neighbors(0)
        if self.row > 0:
            neighbor_coordinates.append((self.row-1, self.col))
            neighbor_coordinates += self.find_horizontal_neighbors(-1)
        if self.row < self.board.height-1:
            neighbor_coordinates.append((self.row+1, self.col))
            neighbor_coordinates += self.find_horizontal_neighbors(+1)

        return neighbor_coordinates

    def check_neighboring_cells(self):
        board = self.board.grid

        for neighbor_coordinates in self.neighbors:
            neighbor_row = neighbor_coordinates[0]
            neighbor_col = neighbor_coordinates[1]
            self.get_neighbor_state(board[neighbor_row][neighbor_col])

    def update_state(self):
        if self.state == 'alive':
            if self.count_alive_neighbors < 2 or self.count_alive_neighbors > 3:
                if randrange(10) is 0:
                    self.next_state = 'zombie'
                else:
                    self.next_state = 'dead'
            if self.count_zombie_neighbors > 1:
                self.next_state = 'zombie'
        if self.state == 'dead':
            if self.count_alive_neighbors is 3:
                self.next_state = 'alive'
        if self.state == 'zombie':
            if self.count_alive_neighbors > 2:
                self.next_state = 'dead'
        if not self.next_state:
            self.next_state = self.state

    def take_turn(self):
        self.check_neighboring_cells()
        self.update_state()
        return self.state

    def reset_state(self):
        self.count_alive_neighbors = 0
        self.count_zombie_neighbors = 0
        self.state = self.next_state
        self.next_state = None
