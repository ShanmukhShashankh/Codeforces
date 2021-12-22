a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if a+b == c+d or a+c == b+d or a+d == b+c or a+b+c == d or a+b+d == c or a+c+d == b or b+c+d == a:
    print("YES")
else:
    print("NO")
