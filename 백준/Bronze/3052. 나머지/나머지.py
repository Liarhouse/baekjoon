import sys
b = []

for i in range(10):
    a = int(sys.stdin.readline())
    a = a%42
    b.append(a)
    
print(len(set(b)))