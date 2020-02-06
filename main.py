import time
from board import Board

BLUE_TEXT = '\u001b[34m'
TEXT_RESET = '\u001b[0m'

def tick(board):
    for row in board.grid:
        for cell in row:
            cell.take_turn()
    board.draw_board()

    if board.has_changed_this_turn:
        board.has_changed_this_turn = False
        for row in board.grid:
            for cell in row:
                cell.reset_state()
    else:
        board.end_game()

def main():
    print(f'{BLUE_TEXT}Welcome to the ZOMBIE Game of Life{TEXT_RESET}')
    width = int(input('How many cells wide should the board be?\n'))
    height = int(input('How many cells high should the board be?\n'))
    board = Board(width, height)
    board.draw_board()

    try:
        board.populate_board()
        while board.game_has_not_ended:
            tick(board)
            time.sleep(1)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
