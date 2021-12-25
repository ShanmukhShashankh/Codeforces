testcases = int(input())
list_totals = []

while testcases!=0:
    list_str = input().split()
    list_int = []

    for i in list_str:
        list_int.append(int(i))

    total = 0

    for i in list_int:
        total += i

    list_totals.append(total)

    testcases -= 1

rank = list_totals[0]
list_totals.sort(reverse=True)

for i in range(len(list_totals)):
    if list_totals[i]==rank:
        print(i+1)
        break

#DO NOT KNOW WHERE I MESSED UP


# testcases = int(input())
# i = 1
# rank = 0
# reference = 0
# while testcases!=0:
#     a, b, c, d = input().split()
#     a, b, c, d = int(a), int(b), int(c), int(d)
#     total = a+b+c+d
#     if total>=reference:
#         reference = total
#         rank = i
#     i += 1
#     testcases -= 1

# print(rank)