def solve():
	(r,g,b) = map(int , input().split())
	(cr,cg,cb)= map(int, input().split())
	(crg, cgb)= map(int, input().split())
	nr =  max(0, r - cr)
	nb=  max(0, b - cb)
	ng= max(0, g - cg )

	# handle red first
	brg = nr
	if brg > crg: 
		print(-1)
		return
	crg -= brg
	bgb = nb
	if bgb > cgb:
		print(-1)
		return
	cgb -= bgb
	if ng > cgb + crg:
		print(-1)
		return
	print(ng + brg + bgb)
solve()
