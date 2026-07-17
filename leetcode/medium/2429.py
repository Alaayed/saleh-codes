class Solution:
	def minimizeXor(self, num1: int, num2: int) -> int:
		set_bits = num2.bit_count()
		x = 0
		while set_bits > 0:
			top_bit_pos = num1.bit_length() # grab the top bit
			if top_bit_pos == 0: break # no top bit to grab
			top_bit = (1 << (top_bit_pos-1))
			x |= top_bit # add it to x
			num1 ^= top_bit # rem from y
			set_bits -= 1
		lowest_bit = 1
		while set_bits > 0: # still need to meet bit len req
			if lowest_bit & x != lowest_bit: # found a bit to set
				x |= lowest_bit # set bit
				set_bits -= 1 # inc rec bit count
			lowest_bit <<=1
		return x