T = int(input())

for k in range(1,T+1):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print('Case #{}: {} + {} = {}'.format(k,A,B,A+B))
