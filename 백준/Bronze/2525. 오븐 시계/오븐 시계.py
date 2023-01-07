a=input()
c=int(input())

a, b=a.split()
a=int(a)
b=int(b)

d=a*60+b+c

if d>=1440:
    d-=1440
e=d//60
d=d%60

print(e,d)