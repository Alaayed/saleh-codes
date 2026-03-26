from math import gcd
a= [4264, 4921, 6321, 6984, 2316, 8432, 6120 ,1026]
print(sorted(a))
a.sort()
print(*a)
last_popped= 0
dontPop = 0
for i in range(len(a)):
    last_popped = 0
    last_popped= (a.pop(len(a)-1 -dontPop))
    if gcd(*a) != 1:
        a.append(last_popped)
        dontPop+=1
print(a)