import sys
n = 0
f = sys.stdin.readline()
a = int(f)
while True:
    a = str(a)
    b = []
    for i in a:
        i=int(i)
        b.append(i)
    c = str(sum(b))
    a = int(str(b[-1])+c[-1])
    n += 1
    if a == int(f):
        break
print(n)