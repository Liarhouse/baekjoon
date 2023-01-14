import sys

b = []
for i in range(9):
    a = int(sys.stdin.readline())
    b.append(a)
c = max(b)
d = b.index(c)
print(c)
print(d+1)