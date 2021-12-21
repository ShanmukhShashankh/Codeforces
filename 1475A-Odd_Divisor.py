test_cases = int(input())
while test_cases!=0:
  x = int(input())
  n=1
  while n<x:
    n=n*2
  if n == x:
    print("NO")
  else:
    print("YES")
  test_cases-=1
  
#https://codeforces.com/problemset/problem/1475/A