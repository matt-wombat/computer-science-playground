#
# This is a Towers of Hanoi solver based on the Youtube Video from
# Computerphile. Source:
# https://www.youtube.com/watch?v=8lhxIOAfDss
#
# It uses the principle of recursion
#

def move(f, t):
  print("Move {} to {}".format(f, t))


# n = Number of discs
# f = From stack
# h = Helper stack
# t = To stack
def solve(n, f, h, t):
  # Check for the base case if there is no disk in the from stack
  if n == 0:
    pass
  else:
    solve(n-1, f, t, h)
    move(f, t)
    solve(n-1, h, f, t)

solve(4, "A", "B", "C")

