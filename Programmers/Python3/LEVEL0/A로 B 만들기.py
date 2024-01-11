def solution(before, after):
  b = list(before)
  a = list(after)

  cnt = 0

  b.sort()
  a.sort()

  for k in range(len(b)):
    for j in range(len(a)):
      if k == j:
        if b[k] != a[j]:
          cnt += 1
  if cnt != 0:
    return 0
  else:
    return 1
