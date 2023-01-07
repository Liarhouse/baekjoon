a=input()

a, b=a.split()
a=int(a)
b=int(b)

c=a*60+b-45

if c<0:
    c=1440+c
d=c//60
c=c%60

print(d,c)