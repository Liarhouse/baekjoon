while True:
    a = int(input())
    if a == -1:
        break
    num_list = []
    for i in range(1,a):
        if a % i == 0:
            num_list.append(i)
    if a == sum(num_list):
        ans = '{} = '.format(a)
        for i in range(len(num_list)):
            if i == len(num_list)-1:
                print(ans + '{}'.format(num_list[i]))
            ans += '{} + '.format(num_list[i])
    else:
        print('{} is NOT perfect.'.format(a))