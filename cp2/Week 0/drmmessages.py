
def solution():
	initial_string = input()
	h1,h2 = initial_string[0:len(initial_string)//2], initial_string[len(initial_string)//2:]
	n1,n2 = rotate_string(h1),rotate_string(h2)
	new_string = ""
	for c1,c2 in zip(n1,n2):
		v2 = ord(c2)-ord('A')
		new_char = chr ( 65 + (ord(c1)-ord('A') + v2) % 26)
		new_string += new_char
	return new_string
def rotate_string(h):
	s=sum([ord(char) - ord('A') for char in h])
	new_s = ''
	for char in h:
		new_char = chr(  65 + (ord(char)-ord('A') + s )% 26)
		new_s += new_char
	return new_s

print(solution())