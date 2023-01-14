import sys
b=[i for i in range(1, 31)]
for i in range(28):
    a = int(sys.stdin.readline())
    b.remove(a)
    
print(min(b))
print(max(b))
    
