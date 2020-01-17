import time
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
    print('\u001b[34mWelcome to the Game of Life\u001b[0m')
    width = int(input('How many cells wide should the board be?\n'))
    height = int(input('How many cells high should the board be?\n'))
    board = Board(width, height)
    board.draw_board()
    board.populate_board('alive')
    board.draw_board()
    board.populate_board('zombie')
    board.draw_board()

    try:
        while True:
            tick(board)
            time.sleep(1)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
