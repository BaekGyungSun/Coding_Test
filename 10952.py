while (True):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
        