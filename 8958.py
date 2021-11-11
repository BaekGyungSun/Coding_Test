n = int(input())

for i in range(n):
    test = input()
    score = 0
    k = 0
    for ox in test:
        if ox == 'O':
            k += 1
            score += k
        else:
            k = 0
    print(score)