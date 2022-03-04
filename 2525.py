a, b = map(int, input().split(' ')) #현재 시각
c = int(input())

if b+c >= 60:
    t = (b+c)//60
    m = (b+c)%60
    if t+a > 23:
        print((a+t)-24, m)
    else:
        print(a+t, m)
else:
    print(a, b+c)
