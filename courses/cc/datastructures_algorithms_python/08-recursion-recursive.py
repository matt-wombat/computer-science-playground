#
# Build a function that takes an integer as an input and returns the sum of all
# numbers from the input down to 1.
#

def sum_all_numbers(n):
  if n == 1:
    print("Base Case with n =", n)
    return n
  
  print("Current value of n =", n)
  return n + sum_all_numbers(n-1)

print(sum_all_numbers(7))