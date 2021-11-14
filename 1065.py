# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

def k(x):
    x_str = str(x) # 받은 숫자를 문자형으로 변경
    x_len = len(x_str) # 문자형으로 변경한 것의 길이값
    m_set = set()
    if (x_len == 1) | (x_len == 2):
        return 1
    else:
        for i in range(x_len-1):
            m_set.add(int(x_str[i]) - int(x_str[i+1]))
        if len(m_set) == 1:
            return 1
        else:
            return 0

n = int(input())
count = 0

for j in range(1, n+1):
    count += k(j)

print(count)