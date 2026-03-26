from bisect import bisect_left
from typing import List
# new approach, keep track of all occurances of a character
MAX = 100000
def all_possible_pairs():
    found = 0
    events = input()
    indices = {}
    for i, char in enumerate(events):
        if char not in indices:
            indices[char] = [i]
        else:
            indices[char].append(i)
    # have an instance and the next instance of a char
    # check each char, find if instance occurs between bounds
    # that is one valid pair
    indices = list(indices.values())
    for i in range(len(indices)):
        found += cross_compare(i, indices)

    return found

def cross_compare(k:int, rest : List[List[int]]):
    char1 :List[int] = rest[k]
    found = 0
    n = len(char1)
    for i in range (n):
        lower = char1[i]
        if i+1 < n:
            upper = char1[i+1]
        else:
            upper = MAX
        # if consecutive, skip
        if upper == lower+1:
            continue
        for j,arr in enumerate(rest):
            # don't compare to self
            if k==j:
                continue
            idx_upper = bisect_left(arr, upper)
            idx_lower = bisect_left(arr, lower)
            if idx_upper > idx_lower:
                # can't find anymore, skip
                found += 1
                continue

    return found

print(all_possible_pairs())
