#Rules

[1] Any live cell with fewer than two live neighbours dies, as if by underpopulation.
[2] Any live cell with two or three live neighbours lives on to the next generation.
[3] Any live cell with more than three live neighbours dies, as if by overpopulation.
[4] Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

[5] If there are no zombies, any dying cell has a 5% chance of becoming a zombie
[6] Any zombie with three or more live neighbors dies
[7] Any live cell with two or more zombie neighbors becomes a zombie
[8] Zombificiation takes priority over death of a cell