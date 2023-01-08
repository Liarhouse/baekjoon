a = int(input())
b = int(input())
c = 0
for i in range(b):
    d = input()
    d, e = d.split()
    d = int(d)
    e = int(e)
    c += (d*e)

if a == c:
    print('Yes')
else:
    print('No')