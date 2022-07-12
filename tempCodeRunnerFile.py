number = input()
count = 0
for i in number:
    if i == "4" or i == "7":
        count+=1

count = str(count)

lucky_number = True

for i in count:
    if i != "4" or i != "7":
        lucky_number = False
        break

if lucky_number:
    print("YES")
else:
    print("NO")
