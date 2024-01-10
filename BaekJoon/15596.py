# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

def solve(a):
    sum = 0
    for k in a:
        sum += k
    return sum

print(solve([1,2,3]))
