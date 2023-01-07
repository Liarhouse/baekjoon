a=input()
a, b, c = a.split()
a=int(a)
b=int(b)
c=int(c)


if a==b:
    if b==c:
        d=10000+a*1000
    else:
        d=1000+a*100
elif a==c:
    d=1000+a*100
elif b==c:
    d=1000+b*100
else:
    d = max(a, b, c) * 100
    
print(d)