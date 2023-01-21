a = int(input())
list = []
for i in range(a):
    b,c,d = map(int,input().split())
    e = d // b + 1 # 몫(방번호)
    f = d % b # 나머지(층수)
    if f == 0:
        e -= 1
        f = b
    if e < 10:
        list.append('%d0%d' %(f, e))
    else:
        list.append('%d%d' %(f,e))

for i in list:
    print(int(i))