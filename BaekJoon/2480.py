A, B, C = map(int, input().split(' '))

if 1 <= A <= 6 and 1 <= B <= 6 and 1 <= C <= 6:
	if A == B and B == C:
		print(10000 + int(A)*1000)
	if A == B and B != C:
		print(1000 + int(A)*100)
	if B == C and C != A:
		print(1000 + int(B)*100)
	if C == A and A != B:
		print(1000 + int(C)*100)
	if A != B and B != C and A != C:
		if A > B and A > C:
			print(int(A)*100)
		if B > A and B > C:
			print(int(B)*100)
		if C > A and C > B:
			print(int(C)*100)
