def sol():
	s = input()
	vowels = ["a", "e", "i", "o", "u"]
	res = 0
	for v in vowels: 
		res += s.count(v)
	y = s.count("y")
	print(f"{res} {res+y}")
sol()
