testcases = int(input())
while testcases!=0:
    n = int(input())
    a = input().split()
    arr = []
    count = 0
    for i in a:
        arr.append(int(i))
    for i in range(n):
        for j in range(n):
            if i<j:
                if (arr[j]-arr[i])==(j-i):
                    count += 1
    print(count)
    testcases -= 1