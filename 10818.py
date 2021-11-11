# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
N_list = list(map(int,input().split(' ')))

max_N = N_list[0]
min_N = N_list[0]

for k in N_list:
    if k > max_N:
        max_N = k
    if k < min_N:
        min_N = k

print('{} {}'.format(min_N,max_N))