a,b = map(int, input().split())
list = []
for _ in range(a):
    list.append(0)
for _ in range(b):
    c, d, e = map(int, input().split())
    basket = range(c-1,d)
    for i in basket:
        list[i]=e
ans=''
for n, i in enumerate(list):
    i = f"{i}"
    if len(list) == n+1:
        ans += i
    else:
        ans += i
        ans += ' '
print(ans)