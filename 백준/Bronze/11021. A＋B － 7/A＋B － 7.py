a = int(input())

d = []
for i in range(a):
    b=input()
    b, c = b.split()
    b = int(b)
    c = int(c)
    d.append(b+c)

for i, o in enumerate(d):
    i += 1
    print('Case #%d:' %i, o)