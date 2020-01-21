# Zombie Game of Life

Welcome to Conway's Game of Live, with zombies! The basic rules are the same, with a few new ones added on.

## Rules

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
1. Any live cell with two or three live neighbours lives on to the next generation.
1. Any live cell with more than three live neighbours dies, as if by overpopulation.
1. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
1. Any dying cell has a 10% chance of becoming a zombie
1. Any zombie with three or more live neighbors dies
1. Any live cell with two or more zombie neighbors becomes a zombie
1. Zombificiation takes priority over death of a cell

## Running the Game

This is a command line program built with python3. Run `main.py` in the terminal, and the game will start.