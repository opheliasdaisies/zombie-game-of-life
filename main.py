from board import Board

def tick(board):
    for row in board.grid:
        for cell in row:
            cell.take_turn()
    board.draw_board()

    for row in board.grid:
        for cell in row:
            cell.reset_state()

def main():
    print('Welcome to the Game of Life')
    board = Board(5, 5)
    board.draw_board()
    board.grid[2][2].state = 'alive'
    board.grid[2][3].state = 'alive'
    board.grid[3][3].state = 'alive'
    board.grid[3][2].check_neighboring_cells()
    tick(board)

if __name__ == "__main__":
    main()
