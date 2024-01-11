def solution(quiz):
    result = []

    for k in quiz:
        answer = k.split()

        if answer[1] == '-':
            an1 = int(answer[0])-int(answer[2])
            an2 = int(answer[4])

            if an1 == an2:
                result.append("O")
            else:
                result.append("X")

        elif answer[1] == '+':
            an1 = int(answer[0])+int(answer[2])
            an2 = int(answer[4])

            if an1 == an2:
                result.append("O")
            else:
                result.append("X")

    return result
