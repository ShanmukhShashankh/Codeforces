username = input()
username_final = []
for i in username:
    if i not in username_final:
        username_final.append(i)
if len(username_final)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

#https://codeforces.com/problemset/problem/236/A