import sys
list=[]
for _ in range(int(input())):
    list.append(int(sys.stdin.readline()))
list.sort()
for i in list:
    print(i)