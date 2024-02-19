def devide_sum(x):
    for i in range(x):
        num_list = []
        y = i
        while y > 0:
            left = y % 10
            num_list.append(left)
            y = y // 10
        if i + sum(num_list) == x:
            break
        else:
            i = 0
    return i
            

num = int(input())
result = devide_sum(num)
print(result)