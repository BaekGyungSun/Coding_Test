# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

A = int(input())
B = int(input())
C = int(input())

k = A*B*C
index = []
if 100 <= A < 1000 and 100 <= B < 1000 and 100 <= C < 1000:
    for g in range(0,10):
        index.append(0)

    for m in str(k):
        for i in range(0,10):
            if int(m) == i:
                index[i] += 1

    for j in range(0,10):
        print(index[j])
