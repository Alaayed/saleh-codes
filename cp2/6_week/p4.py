def stupid():
	n = int(input())
	inv = []
	for i in range(n):
		_ = input()
		heights = list(map(int , input().split()))
		heights.reverse()
		print()
		stack = []
		for h in heights:
			print(h , stack)
			popped = False
			while stack and stack[-1] < h :
				popped = True
				print("POPPPING")
				stack.pop()
			if stack and popped:
				print("BREAK")
				inv.append(i+1)
				break
			stack.append(h)
	print(len(inv))
	list ( map (print, inv))
stupid()
