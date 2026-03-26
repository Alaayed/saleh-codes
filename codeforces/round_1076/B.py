def solve():
	t = int(input())
	for _ in range(t):
		n = int(input())
		nums = list(map(int, input().split()))
		# Get index of largest out of order
		inorder = 0
		while n > 0:
			if nums[inorder] == n:
				inorder += 1
				n-=1
			else:
				break
		if n == 0:
			print(' '.join(map(str,nums)))
			continue
		largest_index = nums.index(n)
		initial_section= nums[:inorder]
		first_section = nums[inorder:largest_index+1]
		second_section = nums[largest_index+1:]
		print(' '.join(map(str,initial_section + list(reversed(first_section)) + second_section)))
solve()