from bisect import bisect_left

MODN = 10 ** 9 + 7
MAXN = 3000 + 5


def two_powers_mod():
	powers = [1 for _ in range(MAXN)]
	for i in range(1, MAXN):
		powers[i] = (powers[i - 1] << 1) % MODN
	return powers


powers = two_powers_mod()


def in_range_elements(i, j, positions, n):
	pi, pj = positions[i], positions[j]
	dx = pj - pi
	left_elements = bisect_left(positions, pi - dx)
	right_elements = bisect_left(positions, pj + dx)
	return left_elements + (n - right_elements)


def solve():
	n = int(input())
	positions = sorted(list(map(int, input().split())))
	possible_permutations = 0
	for i in range(n):
		for j in range(i + 1, n):
			in_range = in_range_elements(i, j, positions, n)
			possible_permutations += powers[in_range]
			possible_permutations %= MODN
	print(possible_permutations)


solve()
