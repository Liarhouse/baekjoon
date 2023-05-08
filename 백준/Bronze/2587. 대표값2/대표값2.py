def get_median_v2(data):
    data = sorted(data)
 
    centerIndex = len(data)//2
    return int((data[centerIndex ] + data[-centerIndex - 1])/2)

list=[]
for _ in range(5):
    list.append(int(input()))
print(int(sum(list) / len(list)))
print(get_median_v2(list))