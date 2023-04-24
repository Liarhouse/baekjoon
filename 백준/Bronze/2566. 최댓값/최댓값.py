num_list=[]
for _ in range(9):
    num_list+=list(map(int,input().split()))
maxi=max(num_list)
ind=num_list.index(maxi)
a=(ind//9)+1
b=(ind%9)+1
print(maxi)
print(a,b)
