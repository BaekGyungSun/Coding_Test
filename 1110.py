N = int(input())
new = N

cycle = 0
while (True):
    a = new // 10   # a는 십의 자리
    b = new % 10    # b는 일의 자리
    c = (a+b) % 10  # a+b 의 일의 자리
    new = b*10 + c    # new 는 b 가 십의 자리, c 가 일의 자리로 하는 새로운 수
    cycle += 1
    if N == new:
        break
print(cycle)