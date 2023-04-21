a=input()
b=list(a)
b.reverse()
b="".join(b)
if a == b:
    print(1)
else:
    print(0)