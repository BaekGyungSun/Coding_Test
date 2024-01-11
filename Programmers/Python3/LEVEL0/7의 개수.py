def solution(array):
    answer = 0
    
    for k in array:
        pr = []
        k = str(k)
        if k == '7':
            answer += 1
        if len(k) >= 2:
            for j in range(0, len(k)):
                pr.append(k[j])
            
            for m in range(0, len(pr)):
                if pr[m] == '7':
                    answer += 1
                    
    return answer
