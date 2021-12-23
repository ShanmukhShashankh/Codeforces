x = int(input())
stairs = input().split()
stairways=0
stairs_int = []
max_steps = []

for i in stairs:
    stairs_int.append(int(i))

for i in stairs:
    if int(i) == 1:
        stairways +=1

for i in range(1, len(stairs_int)):
    if stairs_int[i] == 1:
        max_steps.append(stairs_int[i-1])

max_steps.append(stairs_int[-1])

print(stairways)
print(*max_steps, sep=' ')

##https://codeforces.com/problemset/problem/1005/A