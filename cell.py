class Cell:
    #other variables: count_live_neighbors, count_zombie_neighbors
    def __init__(self, state, row, col):
        self.state = state
        self.previous_state = None
        self.row = row
        self.col = col
        self.count_live_neighbors = 0
        self.count_zombie_neighbors = 0
        self.count_live_neighbors = 0

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

    def update_state(self):
        self.previous_state = self.state
        if self.state == 'alive':
            if self.count_live_neighbors < 2 or self.count_live_neighbors > 3:
                self.state = 'dead'
                # TODO: if no zombies on the board, 5% chance of becoming a zombie
            if self.count_zombie_neighbors > 1:
                self.state = 'zombie'
        if self.state == 'dead':
            if self.count_live_neighbors is 3:
                self.state = 'alive'
        if self.state == 'zombie':
            if self.count_live_neighbors > 2:
                self.state = 'dead'


        # update state
        # check all neighbors and update counts of live and zombie neighbors
        # check to see if neighbors' state should change