import sys

T = int(sys.stdin.readline().rstrip()) # 빠른 출력을 원하는 경우, 'sys.stdin.readline().rstrip() 사용.

for i in range(T):
    A, B = map(int,sys.stdin.readline().rstrip().split(' '))
    print(A+B)