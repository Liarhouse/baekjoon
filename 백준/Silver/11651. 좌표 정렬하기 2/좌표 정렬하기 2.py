A = int(input())
num_list = []
for _ in range(A):
    a, b = map(int, input().split(" "))
    num_list.append([b, a])
s_num_list = sorted(num_list)

for y, x in s_num_list:
    print(x, y)