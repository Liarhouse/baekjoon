a=input()
b, c = a.split()
b = int(b)
c = int(c)
if b > c:
    print('>')
elif b < c:
    print('<')
else:
    print('==')