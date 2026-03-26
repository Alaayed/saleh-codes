def print_dp():
	debt = 0
	n = int(input())
	stack = list(map(int, input().split()))
	stack.reverse()
	solutions = []
	for v in stack:
		(s, d) = solve(v+debt)
		debt  += d
		solutions.append(s)
	solutions.reverse()
	print("".join(solutions))
def solve(v):
	if v == 1:
		return ("1" , 0)
	(s , debt) = solve(v//2)
	if v % 2 == 1:
		return (s+ "d+"+"1+",debt + 2)
	else:
		return (s + "d+", debt + 1)
print_dp()
