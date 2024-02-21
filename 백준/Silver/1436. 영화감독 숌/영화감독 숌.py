A = int(input())
count = 0
num = 666
while True:
    if str(666) in str(num):
        count+=1
        if count == A:
            break
        num+=1
    else:
        num+=1
    
print(num)