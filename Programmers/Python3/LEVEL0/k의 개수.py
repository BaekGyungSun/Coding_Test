def solution(i, j, k):
    start = i
    end = j
    target = k

    cnt = 0

    for m in range(start, end+1):
        m = str(m)
        if len(m) == 1:
            if m == str(target):
                cnt += 1
        elif len(m) >= 2:
            nums = list(m)
            for u in range(len(nums)):
                if nums[u] == str(target):
                    cnt += 1
    
    return cnt
