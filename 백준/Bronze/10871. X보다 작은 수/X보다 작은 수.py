import sys
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
d = []
for i in c:
    if i < b:
        d.append(i)
for i in d:
    print(i, end=' ')