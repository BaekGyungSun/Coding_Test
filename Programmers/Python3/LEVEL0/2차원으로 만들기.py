# 변수 : num_list, n

def solution(num_list, n):
  result = []

  for k in range(len(num_list) // n):
    result.append(num_list[n*k:n*(k+1)])

  return result
