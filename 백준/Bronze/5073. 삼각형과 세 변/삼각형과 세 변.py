while True:
    idx=[0,1,2]
    x,y,z=(map(int,input().split()))
    list=[x,y,z]
    if list[0] == 0:
        break
    x=list.index(max(list))
    idx.pop(x)
    if list[x] >= list[idx[0]]+list[idx[1]]:
        print('Invalid')
    else:
        if list[0] == list[1] and list[1] == list[2]:
            print('Equilateral')
        elif list[0] == list[1] or list[0] == list[2] or list[1] == list[2]:
            print('Isosceles')
        else:
            print('Scalene')