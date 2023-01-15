import sys



a = int(sys.stdin.readline())
d=[]
for i in range(a):
    b = sys.stdin.readline()
    b = list(map(int,b.split()))
    score = b[1:]
    c = sum(score)/b[0]
    def bigger(x):
        return x > c
    d.append(len(list(filter(bigger, score)))/b[0]*100)
    # print(round(len(list(filter(bigger, score)))/b[0]*100,3))
for i in d:
    print('%.3f%%' %i)