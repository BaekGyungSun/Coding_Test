# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def a(c):
    b = 0
    c_str = str(c)
    for i in range(len(c_str)):
        b += int(c_str[i])
    return b + c

n = 1
total = list(range(1,10001))
k = set()

while n <= 10000:
    m = n
    while True:
        m = a(m)
        if m <= 10000:
            k.add(m)
        else:
            break
    n += 1

k = list(k)

for j in k:
    total.remove(j)
for j in total:
    print(j)