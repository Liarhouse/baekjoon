a = int(input())

d = []
e = []
f = []
for i in range(a):
    b=input()
    b, c = b.split()
    b = int(b)
    c = int(c)
    d.append(b+c)
    e.append(b)
    f.append(c)

for i, o in enumerate(d):
    print('Case #%d: %d + %d =' %(i+1, e[i], f[i]), o)