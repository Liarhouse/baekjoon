import sys

while True:
    a = sys.stdin.readline()
    a, b = map(int, a.split())
    if a == 0 and b == 0:
        break
    print(a+b)