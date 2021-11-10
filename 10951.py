import sys

try:
    while (True):
        A, B = map(int,sys.stdin.readline().split(' '))
        if 0 < A < 10 and 0 < B < 10:
            print(A+B)
        else:
            break # A, B가 조건에 맞지 않으면 중지
except:
    print(' ') # 공백이 들어와도 무시함