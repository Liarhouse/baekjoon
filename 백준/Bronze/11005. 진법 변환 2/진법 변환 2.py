a, num = map(int,input().split())
ans = ''
if num >= 10:
    while True:
        b = a%num
        if a//num == 0:
            if a >= 10:
                ans = chr(a+55) + ans
            else:
                ans = '{}'.format(a) + ans
            break
        else:
            a = a//num
        if b >= 10:
            ans = chr(b+55) + ans
        else:
            ans = '{}'.format(b) + ans
else:
    while True:
        b = a%num
        if a//num == 0:
            ans = '{}'.format(a) + ans
            break
        else:
            a = a//num
        ans = '{}'.format(b) + ans
print(ans)