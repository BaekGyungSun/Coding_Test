N = int(input())

for x in range (1,N+1):
    if x != N:
        print(' '*(N-x) + '*'*x)
    else:
        print('*'*x)