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

    def get_neighbor_state(self, neighboring_cell):
        if neighboring_cell.state is 'alive':
            self.count_alive_neighbors += 1
        if neighboring_cell.state is 'zombie':
            self.count_zombie_neighbors += 1

    def check_neighboring_cells(self):
        board = self.board.grid
        max_row = self.board.height-1
        max_col = self.board.width-1
        if self.row > 0:
            if self.col > 0:
                self.get_neighbor_state(board[self.row-1][self.col-1])
            if self.col < max_col:
                self.get_neighbor_state(board[self.row-1][self.col+1])
            self.get_neighbor_state(board[self.row-1][self.col])
        if self.row < max_row:
            if self.col > 0:
                self.get_neighbor_state(board[self.row+1][self.col-1])
            if self.col < max_col:
                self.get_neighbor_state(board[self.row+1][self.col+1])
            self.get_neighbor_state(board[self.row+1][self.col])
        if self.col > 0:
            self.get_neighbor_state(board[self.row][self.col-1])
        if self.col < max_col:
            self.get_neighbor_state(board[self.row][self.col+1])

    def update_state(self):
        if self.state == 'alive':
            if self.count_alive_neighbors < 2 or self.count_alive_neighbors > 3:
                self.next_state = 'dead'
                # TODO: if no zombies on the board, 5% chance of becoming a zombie
            if self.count_zombie_neighbors > 1:
                self.next_state = 'zombie'
        elif self.state == 'dead':
            if self.count_alive_neighbors is 3:
                self.next_state = 'alive'
        elif self.state == 'zombie':
            if self.count_alive_neighbors > 2:
                self.next_state = 'dead'
        else:
            self.next_state = self.state

    def take_turn(self):
        self.check_neighboring_cells()
        self.update_state()

    def reset_state(self):
        self.state = self.next_state
        self.next_state = None
