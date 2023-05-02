xx=[]
yy=[]
for _ in range(int(input())):
    x, y = map(int,input().split())
    xx.append(x)
    yy.append(y)
print((max(xx)-min(xx))*(max(yy)-min(yy)))