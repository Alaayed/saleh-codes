def solve_middle(r,c):
	print(f"? {r} {c}")
	ans = int(input())
	# 2 2 case
	if ans == 1:
		# Up case
		print(f"? {r-1} {c}")
		ans = int(input())
		if ans == 1: # 2 2 and 1 2
			print(f"? {r-1} {c-1}")
			ans = int(input())
			if ans == 1:
				print(f"! {r-1} {c-1}")
				return 1
			print(f"! {r-1} {c}")
			return 1
		# left case
		print(f"? {r} {c-1}")
		ans = int(input())
		if ans == 1:
			print(f"! {r} {c-1}")
			return 1
		print(f"! {r} {c}")
		return 1
	return 0

def solve():
	if solve_middle(2, 2) == 1:
		return
	if solve_middle(4,4) == 1:
		return
	print("? 2 4")
	ans = int(input())
	if ans == 1:
		print("? 1 4")
		ans = int(input())
		if ans == 1:
			print("! 1 4")
			return
		print("! 2 4")
		return
	print("? 3 4")
	ans == int (input())
	if ans == 1:
		print("! 3 4")
	print("! 4 4")
solve()
