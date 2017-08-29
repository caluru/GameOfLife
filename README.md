# GameOfLife
Implements Conway's Game of Life in C++ and Python, parallel version using MPI
See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for details

Uses the standard rules:

1) Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2) Any live cell with two or three live neighbours lives on to the next generation.
3) Any live cell with more than three live neighbours dies, as if by overpopulation.
4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

C++ GUI implemented using Qt
Python GUI implemented using Tkinter

TODO (Python):
1) Add gui to input grid size
2) Add option to run for n iterations