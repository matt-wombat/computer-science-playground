#
# Solution of the Knapsack Problem using 
# dynamic programming with a matrix for memoization
#

def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      elif weights[index-1] <= weight:
        matrix[index][weight] = max(
          matrix[index-1][weight],
          values[index-1]+matrix[index-1][weight-weights[index-1]])
      else:
        matrix[index][weight] = matrix[index-1][weight]        

  for index in range(rows):
    print(matrix[index])
  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# Use this to test your function:

if __name__ == '__main__':
  weight_cap = 50
  weights = [31, 10, 20, 19, 4, 3, 6]
  values = [70, 20, 39, 37, 7, 5, 10]
  # values = [70, 20, 39, 37, 30, 5, 10]
  print(dynamic_knapsack(weight_cap, weights, values))
