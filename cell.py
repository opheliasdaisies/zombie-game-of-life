class Cell:
    #other variables: count_live_neighbors, count_zombie_neighbors
    def __init__(self, state, row, col):
        self.state = state
        self.row = row
        self.col = col

    # def check_neighboring(self):
        # self.row-1
        #     self.column-1
        #     self.column
        #     self.column+1
        # self.row
        #     self.column-1
        #     self.column+1
        # self.row+1
        #     self.column-1
        #     self.column
        #     self.column+1

