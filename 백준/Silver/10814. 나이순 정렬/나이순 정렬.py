n = int(input())

l = []
for i in range(n):
    a, b = input().split(" ")
    l.append([int(a), str(b)])
for i in sorted(l, key=lambda x: x[0]):
    print(f"{i[0]} {i[1]}")
