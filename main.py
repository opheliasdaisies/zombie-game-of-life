import time
import os
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
    board.grid[1][3].state = 'alive'
    board.draw_board()
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            tick(board)
            time.sleep(1)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
