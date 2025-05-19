#
# Solution of Fibonacci calculation using dynamic programming
# and memoization
#

# Create variable for memoization
memo = {}

def dynamic_fibonacci(num):
  answer = None
  if num <= 1:
    return num

  # Check if number is already memoized
  if num in memo.keys():
    answer = memo[num]
  else:
    # Memoize Fibonacci results
    memo[num - 1] = dynamic_fibonacci(num - 1)
    memo[num - 2] = dynamic_fibonacci(num - 2)

    # Calculate result from memoization
    answer = memo[num - 1] + memo[num - 2]
    
  return answer

if __name__ == '__main__':
  print(dynamic_fibonacci(20))
  print(dynamic_fibonacci(200))