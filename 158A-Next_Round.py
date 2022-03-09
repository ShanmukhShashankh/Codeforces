n,k = input().split()
n= int(n)
k = int(k)
s = input().split()
scores = []
count = 0

for i in s:
    scores.append(int(i))

qua_m = scores[k-1]

for i in scores:
    if i > 0:
        if i >= qua_m:
            count += 1

print(count)