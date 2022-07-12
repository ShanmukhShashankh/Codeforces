magnets = int(input())
arrangement = []
groups = 0
for i in range(magnets):
    x = int(input())
    arrangement.append(x)

for i in range(1, magnets):
    if arrangement[i-1] != arrangement[i]:
        groups += 1
        
groups += 1
print(groups)
    


#https://codeforces.com/problemset/problem/344/A
