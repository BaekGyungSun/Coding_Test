N = int(input())

N_list = list(map(int, input().split(' ')))
max_N = N_list[0]
sum = 0

for k in range(len(N_list)):
    if max_N < N_list[k]:
        max_N = N_list[k]

for m in range(len(N_list)):
    N_list[m] = N_list[m]/max_N*100

for j in range(N):
    sum += N_list[j]

print(sum/N)
