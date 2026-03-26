from math import comb
def bruteForce(n=5 , sections = 5):
	permutations =0
	for i in range(1, n):
		left_side = i
		right_side = (n-i)
		permutations += left_side * right_side
	print(permutations)

bruteForce(n=5, sections=5)

# Case 1, they are int
# how about the case where they are
def betterpermutations(n=5 , sections=5):
	permutations =0
	for i in range(2, 3):
		# Case 1: normal permutations
		permutations += comb(n-1, i-1)
		print(f"Case 1: {permutations}")
		# Case 2: One of them experiences descent
		permutations += comb(n-i, 1) * (n-2)
		print(f"Case 2: {permutations}")
		# Case 3: both experience descent
		permutations += comb(n-i, 1) * (n-2) * (n-3)
		print(f"Case 3: {permutations}")
	return permutations

s= 5
for r in range(0, s):
	res = []
	for c in range(0, s):
		res.append((r+c) % s + 1)
	print(f'r,perm : {r} -> {res}')
