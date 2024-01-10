N = int(input())

for i in range(N):
    k = list(map(int, input().split()))
    average = float(sum(k[1:]))/float(k[0])
    count = 0
    for j in k[1:]:
        if j > average:
            count += 1
    print("%0.3f%%" %round(float(100*count)/float(k[0]),3)) # 소숫점 셋째자리까지만 표기, 넷째자리에서 반올림
