import timeit

setup = """
import random
import numpy as np
"""

t_py = timeit.timeit(
    "[random.randint(0, 100) for _ in range(1_000_000)]",
    setup=setup,
    number=20
)

t_np = timeit.timeit(
    "np.random.randint(0, 100, size=1_000_000).tolist()",
    setup=setup,
    number=20
)

t_np_no_list = timeit.timeit(
    "np.random.randint(0, 100, size=1_000_000)",
    setup=setup,
    number=20
)

print("Python list comprehension:", t_py)
print("NumPy -> tolist():        ", t_np)
print("NumPy (kept as ndarray):  ", t_np_no_list)
