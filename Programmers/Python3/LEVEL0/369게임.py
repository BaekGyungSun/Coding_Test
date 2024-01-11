def solution(order):
  cnt = 0
  order = list(order)

  for k in range(len(order)):
    if order[k] == '3' or order[k] == '6' or order[k] == '9':
      cnt += 1

  return cnt
