def tetration():
	num = float(input())
	fin = num **(1/num)
	return round(fin, 6)
print(tetration())
