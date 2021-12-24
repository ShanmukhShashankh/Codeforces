testcases = int(input())
while testcases!=0:
    string_len = int(input())
    string = input()
    count_parantheses = 0
    count_letters = 0
    for i in reversed(range(string_len)):
        if string[i]==")" and string[i-1]==")":
            count_parantheses += 1
        else:
            break
    if string_len!=1:
        count_parantheses+=1
    count_letters = string_len - count_parantheses
    
    if count_parantheses>count_letters:
        print("Yes")
    else:
        print("No")
    testcases -= 1


#https://codeforces.com/problemset/problem/1411/A