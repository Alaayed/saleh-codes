from typing import List, Tuple
DEBUG = False

def tabs_to_spaces():
    n = int(input())
    lines = []

    for i in range(n):
        lines.append(input())
    line_counts = []
    depth = 0
    for line in lines:
        s_count, t_count = 0,0
        for char in line:
            if char == 's':
                s_count += 1
            elif char == 't':
                t_count += 1
            elif char == '}':
                depth -= 1
        line_counts.append( ( s_count, t_count, depth ) )
        if line[-1] == '{':
            depth += 1
    # Check every possible value of t
    for i in range(1, 1000):
        if is_valid_t(line_counts, i):
            return i
    return -1

def is_valid_t(line_counts: List[Tuple[int, int, int]], t : int) -> bool:
    depth_check = {}
    for s_count, t_count, depth in line_counts:
        total_count = s_count + t_count * t
        print(f'{total_count}\t{depth}\t{total_count}')
        if depth_check.get(depth, -1) == -1:
            print(f'New depth: {depth} ')
            depth_check[depth] = total_count
        elif depth_check[depth] != total_count:
            return False
    i = depth_check.get(1, -1)

    if i == 0:
        return False
    elif i == -1:
        return True
    for depth, count in depth_check.items():
        if depth * i != count:
            return False
    return True

import builtins

_ORIG_PRINT = builtins.print
if not DEBUG:
    builtins.print = lambda *a, **k: None
sol = tabs_to_spaces()
builtins.print = _ORIG_PRINT
print(sol)