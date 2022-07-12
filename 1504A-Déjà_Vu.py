def Palindrome(strg):
    length = len(strg)
    new_strg = ''
    for i in range(1, length+1):
        new_strg += strg[-i]
    if strg == new_strg:
        return True
    else:
        return False


testcases = int(input())
while testcases!=0:
    s = input()
    all_a = True
    for i in range(len(s)):
        if s[i]!='a':
            all_a = False
    if all_a:
        print("NO")
    else:
        if not Palindrome('a'+s):
            print("YES")
            print("a"+s)
        else:
            print("YES")
            print(s+"a")
    testcases -= 1