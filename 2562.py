# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

max_a = 0
index_a = 0

for i in range(1,10):
    n = input()
    if int(n) > max_a:
        max_a = int(n)
        index_a = i

print(max_a)
print(index_a)