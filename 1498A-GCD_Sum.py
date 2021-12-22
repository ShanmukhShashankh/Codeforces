from math import gcd

testcases = int(input())

while testcases!=0:
  x = input()
  sum_x = 0
  for i in x:
    sum_x += int(i)
  x = int(x)
  while gcd(x,sum_x)==1:
    x+=1
    sum_x = 0
    for i in str(x):
      sum_x += int(i)
  else:
    print(x)
  testcases -= 1