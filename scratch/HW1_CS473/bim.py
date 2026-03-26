import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import numpy as np
from math import log, isclose

# -----------------------------
#  Data setup
# -----------------------------
def build_matrix():
    A = np.array([
        [2, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 2, 2, 1]
    ], dtype=float)
    terms = ["student", "course", "lecture", "patient", "clinic"]
    return A, terms

# -----------------------------
#  Ranking helper (ties)
# -----------------------------
def rank_with_ties(scores, tol=1e-5):
    sorted_docs = sorted(enumerate(scores, start=1), key=lambda x: x[1], reverse=True)
    ranked = []
    current_rank = 1
    for i, (doc, score) in enumerate(sorted_docs):
        if i > 0 and not isclose(score, sorted_docs[i-1][1], abs_tol=tol):
            current_rank = i + 1
        ranked.append((current_rank, doc, score))
    return ranked

# -----------------------------
#  Binary Independence Model
# -----------------------------
 -----------------------------
#  LaTeX Output
# -----------------------------
def print_latex_results():
    # ---- BIM ----
    terms, n_i, r_i, bim_scores = compute_bim()
    ranked_bim = rank_with_ties(bim_scores)

    # ---- BM25 ----
    idf, bm25_scores = compute_bm25()
    ranked_bm25 = rank_with_ties(bm25_scores)

    print(r"\documentclass{article}")
    print(r"\usepackage{booktabs}")
    print(r"\usepackage[a4paper,margin=1in]{geometry}")
    print(r"\begin{document}")
    print(r"\section*{Question 3: BIM and BM25}")

    # --- BIM TABLES ---
    print(r"\subsection*{Binary Independence Model (BIM)}")
    print(r"\begin{tabular}{lccc}")
    print(r"\toprule")
    print("Term & $n_i$ & $r_i$ & Weight $w_i$ \\\\ \\midrule")
    A, _ = build_matrix()
    N,R = A.shape[1],2
    for t, ni, ri in zip(terms, n_i, r_i):
        w = log(((ri+0.5)/(R-ri+0.5)) / ((ni-ri+0.5)/(N-ni-R+ri+0.5)))
        print(f"{t} & {ni} & {ri} & {w:.4f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    print(r"\subsubsection*{Document Scores and Ranking}")
    print(r"\begin{tabular}{ccc}")
    print(r"\toprule")
    print("Rank & Document & Score \\\\ \\midrule")
    for rank, doc, score in ranked_bim:
        print(f"{rank} & $d_{{{doc}}}$ & {score:.4f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    # --- BM25 TABLES ---
    print(r"\subsection*{BM25 Model}")
    print(r"\begin{tabular}{lcc}")
    print(r"\toprule")
    print("Term & $n_i$ & IDF \\\\ \\midrule")
    n_i = np.count_nonzero(A, axis=1)
    for t, ni, idfv in zip(terms, n_i, idf):
        print(f"{t} & {ni} & {idfv:.4f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    print(r"\subsubsection*{Document Scores and Ranking}")
    print(r"\begin{tabular}{ccc}")
    print(r"\toprule")
    print("Rank & Document & Score \\\\ \\midrule")
    for rank, doc, score in ranked_bm25:
        print(f"{rank} & $d_{{{doc}}}$ & {score:.4f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    print(r"\end{document}")

