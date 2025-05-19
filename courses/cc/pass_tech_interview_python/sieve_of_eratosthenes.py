def sieve_of_eratosthenes(limit):
  primes = []

  candidates = [True for i in range(limit+1)]

  # 0 and 1 are no prime numbers
  candidates[0] = False
  candidates[1] = False

  # remove multiples
  for i in range(len(candidates)):
    j = i
    if candidates[i]:
      # start at multiple * 2 to leave 
      # the actual prime number
      j *= 2
      while j <= limit:
        candidates[j] = False
        j += i
    
  primes = [x for x in range(len(candidates)) if candidates[x] == True]

  return primes

if __name__ == '__main__':
  primes = sieve_of_eratosthenes(100)
  
  # should return:
  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  print(primes) 