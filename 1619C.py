testcases = int(input())
while testcases!=0:
    b = ''
    x = ''
    b_list = []
    a, s = input().split()
    for i in range(1, len(a)+1):
        if s[-i]>a[-i]:
            b += str(abs(int(s[-i])-int(a[-i])))
        elif s[-i]<a[-i]:
            b += str(abs(int(s[-i-1])-int(a[-i])))
            i -= 1
    for i in b:
        b_list.append(i)
    
    b_list.reverse()

    print(b_list)

    for i in range(0,len(b_list)):
        if b_list[i]!='0':
            x=i
            break

    b_list = b_list[x:]
    
    for i in b_list:
        x += i
    
    print(x)
    testcases -= 1


#https://codeforces.com/contest/1619/problem/C