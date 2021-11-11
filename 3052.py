# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

c = []
re = []

for k in range(1,11):
    A = int(input())
    c.append(A)

for i in range(0,10):
    re.append(c[i]%42)

diff_re = []

for m in range(0,10):
    if re[m] not in diff_re:
        diff_re.append(re[m])

print(len(diff_re))