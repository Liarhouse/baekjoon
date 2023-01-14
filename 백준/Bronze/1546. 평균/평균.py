import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline()
c = []
for i in b.split():
    c.append(int(i))
d = max(c)
e = []
for i in c:
    i = i/d*100
    e.append(i)
mean = sum(e) / len(e)
print(mean)