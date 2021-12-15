import math
def maxPrimeFactors (n):
  maxPrime = -1
  while n % 2 == 0:
    maxPrime = 2
    n >>= 1    
        
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
      maxPrime = i
      n = n / i
    
  if n > 2:
    maxPrime = n
    
  return int(maxPrime)

test_cases = int(input())
while test_cases != 0:
  p = int(input())
  if maxPrimeFactors(p) % 2 == 0:
    print("NO")
  else:
    print("YES")
  test_cases -= 1


#Not Submitted
#Time limit of 2 seconds exceeded

#https://codeforces.com/problemset/problem/1475/A