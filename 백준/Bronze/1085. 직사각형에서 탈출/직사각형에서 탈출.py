x, y, w, h = map(int,input().split())
if x > w/2:
    x=w-x
if y > h/2:
    y=h-y
if x <= y:
    print(x)
else:
    print(y)