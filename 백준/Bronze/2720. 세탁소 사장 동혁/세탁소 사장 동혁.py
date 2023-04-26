ans_list=[]
coin=[25,10,5]
for _ in range(int(input())):
    ans=''
    a = int(input())
    for i in range(3):
      b = a//coin[i]
      a = a%coin[i]
      if i == 2:
        ans += '{0} {1}'.format(b, a)
        ans_list.append(ans)
      else:
        ans += '{} '.format(b)
for i in ans_list:
    print(i)