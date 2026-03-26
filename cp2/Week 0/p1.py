from typing import List
from collections import deque


def find_solution() -> int:
    n = int(input())
    elements = list()
    for _ in range(n):
        elements.append(int(input()))
    peak = elements[0]
    current_score = 1
    best = -1
    for i in range(n):
        current_element = elements[i]
        # get previous
        if i == 0:
            prev = -1
        else:
            prev = elements[i - 1]
        # Stricitly increasing, add to stack
        if current_element > prev:
            peak = i
            current_score = 1
        elif current_element == prev:
            # erase queue, strictly in/decreasing condition not met
            peak = i
            current_score = 1
        elif current_element < prev:
            # check palindrome condition
            if current_element == elements[peak - abs(peak - i)]:
                current_score += 2
                best = max(best, current_score)
            else: # condition not met
                # erase stack, start from this element
                peak = i
                current_score = 1
    return best if best >= 3 else -1

print(find_solution())


