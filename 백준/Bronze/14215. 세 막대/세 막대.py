idx=[0,1,2]
x,y,z=(map(int,input().split()))
list=[x,y,z]
x=list.index(max(list))
idx.pop(x)
if list[x] >= list[idx[0]]+list[idx[1]]:
    while True:
        list[x] = list[x] - 1
        if list[x] < list[idx[0]]+list[idx[1]]:
            break
print(sum(list))