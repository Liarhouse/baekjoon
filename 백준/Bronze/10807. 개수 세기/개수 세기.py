import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
c = int(sys.stdin.readline())
b = list(map(int, b.split()))
print(b.count(c))