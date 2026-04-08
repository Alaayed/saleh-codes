import math
def solve(k,n) :
	largest_distance = k - n + 1
	smallest_distance = math.ceil(k / n)
	print(largest_distance)
	print(smallest_distance)
	# Let cur = largest_distance
	# While cur >= smallest_distance
	# Start with a set (1 * (n-1), cur)
	# let rem_obj = largest_distance - cur
	# Distrbute (rem_obj) into n-1 bins capped at cur-1
	# Use inclusion exclusion to do this
	# That gives you the number of ways to make set with the largest distance being cur
	# Use the expected value formula EV
	# cur -= 1
	# Repeat until break condition
	# Output the answer.
solve(20,5)