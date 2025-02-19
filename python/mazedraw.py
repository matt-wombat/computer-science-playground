#
# This program is supposed to test, if it is possible
# to output a changing two-dimensional list to the console
# and updating the output after base data has changed
#

import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

maze = [[0 for x in range(10)] for x in range(10)]

for x in range(1000):
  for row in range(10):
    for col in range(10):
      maze[row][col] += 1

  clear()
  for elem in maze:
    print(' '.join([str(number) for number in elem]))

