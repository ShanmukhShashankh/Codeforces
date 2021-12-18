num1 = input()
num2 = input()
final_num = ''
for i in range(len(num1)):
    if num1[i] != num2[i]:
        final_num += '1'
    else:
        final_num += '0'
print(final_num)
