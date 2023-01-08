import sys
a = int(input())
b = []
for i in range(a):
    c = sys.stdin.readline()
    c, d = map(int, c.split())
    b.append(c+d)
for i in b:
    print(i)