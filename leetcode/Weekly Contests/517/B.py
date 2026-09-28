from math import floor,log10
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        s = 0
        mod = 10**9 + 7
        for n in nums:
            width = n % 10
            d = floor(n/10)
            total_digits = floor(log10(d))  
            bottom_digits = total_digits - width

            y = d % (10 ** bottom_digits)
            x = d // (10 ** bottom_digits)
            s += pow(x,y,mod)
            s %= mod
            print(f"n,x,y = {n}, {x}, {y}")

        print(s)
        return s
