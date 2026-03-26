def rational_sequence():
	n = int(input())
	for _ in range(n):
		line = input().split()
		k = int(line[0])
		n,d = map(int, line[1].split('/'))
		solve(k,n,d)

def solve(k , n , d):
	# Special case, is right most
	if d == 1:
		print(f'{k} {1}/{n+1}')
		return None
	# Make left child
	layers = n // d
	n = n - d * layers
	# Find parent of left child = d - n
	d = d - n
	# Go to right child = n+d
	n = n + d
	# Go down layers number of times left = d + n * layers
	d = d + n * layers
	# print result
	print(f"{k} {n}/{d}")
	return None


rational_sequence()
