a,b = map(int,input().split())
num_list = []
for i in range(1,a+1):
    if a % i == 0:
        num_list.append(i)
try:
    print(num_list[b-1])
except:
    print(0)