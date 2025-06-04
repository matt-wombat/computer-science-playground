#
# This is a Sudoku solver based on the Youtube Video from
# Computerphile. Source
# https://www.youtube.com/watch?v=G_UYXzGuqvM
#
# It uses principles of recursion and backtracking.
#
#

import numpy as np

def possible(y, x, n):
  global grid

  # Check if number n already exists in given row y
  for i in range(0, 9):
    if grid[y][i] == n:
      return False
    
  # Check if number n already exists in given column x
  for i in range(0, 9):
    if grid[i][x] == n:
      return False

  # Check if number n already exists 9-field square given by row y and column x
  x0 = (x // 3) * 3
  y0 = (y // 3) * 3
  for i in range(0,3):
    for j in range(0,3):
      if grid[y0+i][x0+j] == n:
        return False
  
  return True

counter = 0
grid = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
  ]

print("Input:")
print(np.matrix(grid))

print("Solutions:")


def solve():
  global grid, counter

  for y in range(9):
    for x in range(9):
      if grid[y][x] == 0:
        for n in range(1, 10):
          if possible(y, x, n):
            grid[y][x] = n
            counter += 1
            solve()
            grid[y][x] = 0
        return
  
  print(np.matrix(grid))
  print("Number of attempts: ", counter)

solve()