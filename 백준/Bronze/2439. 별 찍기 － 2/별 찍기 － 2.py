import sys
a = int(sys.stdin.readline())

for i in range(a):
    i+=1
    f = a - i
    print(' '*f+'*'*i)