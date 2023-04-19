a,b = map(int, input().split())
list = []
for i in range(a):
    list.append(i+1)
for _ in range(b):
    c, d = map(int, input().split())
    list[c-1], list[d-1] = list[d-1], list[c-1]
ans=''
for n, i in enumerate(list):
    i = f"{i}"
    if len(list) == n+1:
        ans += i
    else:
        ans += i
        ans += ' '
print(ans) 