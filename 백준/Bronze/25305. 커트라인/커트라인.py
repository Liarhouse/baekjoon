a, b = map(int, input().split())
list = list(map(int,input().split()))
list.sort(reverse=True)
print(list[b-1])