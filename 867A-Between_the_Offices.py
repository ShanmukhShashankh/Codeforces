length = int(input())
cities = input()

fs = 0
sf = 0

for i in range(1,length):
    if cities[i-1]=='F' and cities[i]=='S':
        fs += 1
    elif cities[i-1]=='S' and cities[i]=='F':
        sf += 1

if sf>fs:
    print("YES")
else:
    print("NO")

#https://codeforces.com/problemset/problem/867/A