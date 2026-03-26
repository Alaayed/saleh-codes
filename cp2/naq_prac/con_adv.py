def sol():
	(n,k,c) = map(int , input().split())
	school_map = {}
	left_over = []
	made_it = []
	for i in range(n):
		(t,s) = map(int, input().split())
		squal = school_map.get(s , 0)
		if squal == c:
			left_over.append ( (i, t , s ) )
			continue
		if len(made_it) != k:
			made_it.append( ( i , t , s) )
			school_map[s] = squal + 1
	
	if len(made_it) != k:
		needed = k -len(made_it)
		made_it.extend(left_over[:needed])
		made_it.sort()
	for (i , t , s) in made_it:
		print(t)
sol()
