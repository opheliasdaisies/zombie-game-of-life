from board import Board

def main():
    print('Welcome to the Game of Life')
    board = Board(5, 5)
    print(board.board)

if __name__ == "__main__":
    main()
