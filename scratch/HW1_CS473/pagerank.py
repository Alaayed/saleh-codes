import os
# hitting thread limit on cs, make 1 thread
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import numpy as np
def print_latex_tables(M, B, ranked):
    pages = ['A', 'B', 'C', 'D', 'E', 'F']

    # --- Table 1: Adjacency Matrix M ---
    print("\\textbf{Adjacency Matrix $M$} \\\\")
    print("\\begin{tabular}{c|" + "c" * len(pages) + "}")
    print(" & " + " & ".join(pages) + " \\\\ \\hline")
    for i, row in enumerate(M):
        row_str = " & ".join(f"{int(x)}" for x in row)
        print(f"{pages[i]} & {row_str} \\\\")
    print("\\end{tabular}\n")

    # --- Table 2: Transition Matrix B ---
    print("\\textbf{Transition Matrix $B$} \\\\")
    print("\\begin{tabular}{c|" + "c" * len(pages) + "}")
    print(" & " + " & ".join(pages) + " \\\\ \\hline")
    for i, row in enumerate(B):
        row_str = " & ".join(f"{x:.2f}" if x != 0 else "0" for x in row)
        print(f"{pages[i]} & {row_str} \\\\")
    print("\\end{tabular}\n")

    # --- Table 3: Final Ranking ---
    print("\\textbf{PageRank Scores (after 30 iterations)} \\\\")
    print("\\begin{tabular}{c|c}")
    print("Page & Score \\\\ \\hline")
    for page, score in ranked:
        print(f"{page} & {score:.4f} \\\\")
    print("\\end{tabular}")
# M_ij = 1 if i points to j
M = np.array([
    [0, 1, 0, 1, 0, 0],  # A → B, D
    [0, 0, 0, 1, 0, 0],  # B → D
    [1, 1, 0, 0, 0, 0],  # C → A, B
    [0, 0, 0, 0, 1, 0],  # D → E
    [0, 0, 0, 0, 0, 1],  # E → F
    [0, 1, 1, 0, 0, 0]   # F → B, C
], dtype=float)
# Normalize each row of M by its outdegree to form B
B = np.zeros_like(M)
for i in range(M.shape[0]):
    outlinks = np.sum(M[i])
    if outlinks > 0:
        B[i] = M[i] / outlinks
# Initialize PageRank vector
r = np.ones(6) / 6  # uniform initial rank
iterations = 30

for _ in range(iterations):
    r = B.T @ r  # update rule
pages = ['A', 'B', 'C', 'D', 'E', 'F']
scores = sorted(zip(pages, r), key=lambda x: x[1], reverse=True)
print_latex_tables(M, B, scores)
