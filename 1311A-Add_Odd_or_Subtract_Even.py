testcases = int(input())
while testcases != 0:
    a,b=input().split()
    a = int(a)
    b = int(b)
    cases = 0
    if a>b or a==b:
        diff = a-b
        if diff%2==0 and diff !=0:
            cases = 1
        elif diff==0:
            cases = 0
        else:
            cases = 2
    elif a<b:
        diff = b-a
        if diff%2==0:
            cases = 2
        else:
            cases = 1
    print(cases)
    testcases -= 1


#https://codeforces.com/problemset/problem/1311/A