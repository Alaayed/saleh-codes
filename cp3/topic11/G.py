def eat_cream(t, u, v, ice_cream, to_eat):
	# Cream remaining
	rem = max((ice_cream - t * v), 0)
	# cream we need to eat
	to_eat = min(to_eat, rem)
	if to_eat == 0: return 0, 0
	combined_rate = u+v
	to_eat_time = to_eat / u
	rem_time = rem / combined_rate
	if to_eat_time > rem_time: return rem_time*u, rem_time
	return to_eat, to_eat_time

def solve():
	n,v,u = map(int, input().split())
	ice_creams = list(map(int, input().split()))
	time_elapsed = 0
	cream_eaten = 0
	ice_creams.sort()
	current_cream = ice_creams[-1]
	j = 1
	nu = u
	diff = [0]+[ice_creams[i] - ice_creams[i-1] for i in range(1,n)]
	for i in range(n-1,0, -1):
		if current_cream == 0: break
		d = diff[i]
		c,t = eat_cream(time_elapsed, nu, v, current_cream,d)
		time_elapsed += t
		cream_eaten += c * j
		# Account for eaten
		current_cream -= c
		# Account for melt
		current_cream -= v*t
		# now another ice cream to be consumed
		j+=1
		nu = u / (j)
	if current_cream != 0:
		combined_rate = nu+v
		rem_time = current_cream / combined_rate
		cream_eaten += rem_time * nu * n
	print(f"{cream_eaten:.6f}")



solve()

