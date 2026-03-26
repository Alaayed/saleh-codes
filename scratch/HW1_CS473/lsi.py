import re
import os
# hitting thread limit on cs, make 1 thread
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
from typing import List
from nltk.stem import PorterStemmer
from numpy import array
from numpy.linalg import norm
from scipy.linalg import svd
from math import log10, isclose
import numpy as np
# Read in input
def read_input():
	array: List[List[str]] = []
	index_by: List[str] = []
	with open("txtlsi.txt") as f:
		for i, line in enumerate(f):
			if i == 6:
				index_by = list(map(str.strip, line.lower().split(",")))
				continue
			# remove d*:
			line = list(map(str.lower, line[4:].split()))
			array.append(line)
	return array , index_by
# Stem wirds
def stem_list(words: List[str]):
    ps = PorterStemmer()
    return [ps.stem(re.sub(r'[^\w\s]', '', w.lower())) for w in words]
# Compute matrix 
def build_term_occurrence_matrix():
    docs, cols = read_input()
    ps = PorterStemmer()

    stemmed_cols = [ps.stem(c) for c in cols]
    stemmed_docs = [stem_list(d) for d in docs]

    # Build matrix: each row = term, each column = document
    matrix = []
    for term in stemmed_cols:
        row = [doc.count(term) for doc in stemmed_docs]
        matrix.append(row)
    return np.array(matrix), stemmed_cols
def compute_svd(k):
	occ, terms = build_term_occurrence_matrix()
	A   = array(occ)
	# SVF
	U , S , VT = svd(A , full_matrices = False)
	# take top k
	U_k = U[:, :k]
	S_k = np.diag(S[:k])
	VT_k= VT[:k , :]
	return U_k, S_k , VT_k, terms
def sim(q, d):
	return q @ d / (norm(q) * norm(d))
def compute_query():
	U,S,VT,terms = compute_svd(2)
	q = "students taking courses in clinics"
	q = stem_list(q.split())
	q_v= np.array([q.count(t) for t in terms])
	q_prime = q_v @ U @ np.linalg.inv(S)
	weighted_docs = S @ VT
	scores = []
	for i , d in enumerate(weighted_docs.T): 
		score = sim(q_prime, d)
		scores.append( (score , i+1) )
	scores.sort()
	scores.reverse()
	return score
def compute_query_vsm():
	a, terms = build_term_occurrence_matrix()
	n = 6
	df = np.count_nonzero(a, axis = 1)
	idf = np.log10(n / df)

	# ltc docs
	log_tf = np.where(a > 0, 1 + np.log10(a), 0)
	ltc = log_tf * idf[:, None]
	ltc /= norm(ltc, axis=0 , keepdims = True)
	q = stem_list("students taking courses in clinics".split())
	q_tf = array([q.count(t) for t in terms])
	lnc = np.where(q_tf > 0, 1 + np.log10(q_tf), 0)
	lnc /= np.linalg.norm(lnc)
	# ----- cosine similarity -----
	scores = [(float(ltc[:, i] @ lnc), i+1) for i in range(a.shape[1])]
	scores.sort(reverse=True)
	sims = ltc.T @ lnc
	return ltc, sims, terms
def rank_with_ties(sims, tol=1e-4):
    """Return list of tuples (rank, doc_id, score), where ties share the same rank."""
    sorted_docs = sorted(enumerate(sims, start=1), key=lambda x: x[1], reverse=True)
    ranked = []
    current_rank = 1
    for i, (doc, score) in enumerate(sorted_docs):
        if i > 0 and not isclose(score, sorted_docs[i-1][1], abs_tol=tol):
            current_rank = i + 1
        ranked.append((current_rank, doc, score))
    return ranked
def compute_bim():
    A, terms = build_term_occurrence_matrix()
    N, R = 4, 2   # N=4 (all docs), R=2 (p1,p2)

    # Relevant and Non-Relevant sets
    relevant_queries = [
        "students usually take 4 to 6 courses.",
        "advanced courses usually have less students."
    ]
    non_relevant_queries = [
        "lecture hall was full during the show",
        "all doctors in the clinic attended the guest lecture."
    ]

    # Stem and tokenize
    processed_rel = [stem_list(rq.split()) for rq in relevant_queries]
    processed_nonrel = [stem_list(nrq.split()) for nrq in non_relevant_queries]

    # Keep only words in our term list
    relevant = [dict.fromkeys([w for w in pq if w in terms], 1) for pq in processed_rel]
    non_relevant = [dict.fromkeys([w for w in pq if w in terms], 1) for pq in processed_nonrel]
    print("A", A)
    print("Relevant:", relevant)
    print("Non-Relevant:", non_relevant)

    r_i, n_i = [], []

    for i, term in enumerate(terms):
        # how many total docs contain term 
        ni = sum (1 for r in relevant if term in r)
        ni += sum (1 for nr in non_relevant if term in nr)


        # how many relevant docs contain term
        ri = sum(1 for r in relevant if term in r)

        n_i.append(ni)
        r_i.append(ri)

    # Compute term weights (natural log)
    w = [np.log(((ri + 0.5) / (R - ri + 0.5)) /
                ((ni - ri + 0.5) / (N - ni - R + ri + 0.5)))
         for ri, ni in zip(r_i, n_i)]

    print("Weights:", w)

    scores = []
    for d in range(A.shape[1]):
        present = A[:, d] > 0
        scores.append(np.sum(np.array(w)[present]))
    print(f"Value for (N, R): ({N}, {R})")
    return terms, n_i, r_i, scores

# -----------------------------
#  BM25
# -----------------------------
def compute_bm25():
    A, terms = build_term_occurrence_matrix()
    N = 4              # total number of documents
    R = 2              # number of known relevant docs (feedback)

    # Relevant and Non-Relevant sets (same as in BIM)
    relevant_queries = [
        "students usually take 4 to 6 courses.",
        "advanced courses usually have less students."
    ]
    non_relevant_queries = [
        "lecture hall was full during the show",
        "all doctors in the clinic attended the guest lecture."
    ]

    # Stem and filter terms
    processed_rel = [stem_list(rq.split()) for rq in relevant_queries]
    processed_nonrel = [stem_list(nrq.split()) for nrq in non_relevant_queries]

    relevant = [dict.fromkeys([w for w in pq if w in terms], 1) for pq in processed_rel]
    non_relevant = [dict.fromkeys([w for w in pq if w in terms], 1) for pq in processed_nonrel]

    # Compute n_i (number of docs containing term) and r_i (number of relevant docs containing term)
    n_i, r_i = [], []
    for i, term in enumerate(terms):
        ni = sum (1 for r in relevant if term in r)
        ni += sum (1 for nr in non_relevant if term in nr)
        ri = sum(1 for r in relevant if term in r)         # how many relevant docs contain term
        n_i.append(ni)
        r_i.append(ri)

    # BM25 parameters
    k1, k2, b, K = 1.2, 100, 0.75 , 1.2
    L_d = np.sum(A, axis=0)
    L_avg = np.mean(L_d)

    # Query: combine relevant terms into one pseudo-query
    q_terms = set()
    for rel in relevant:
        q_terms.update(rel.keys())
    q = np.array([1 if t in q_terms else 0 for t in terms], dtype=float)
    q = array([1,1,0,0,1])
    # Compute document scores
    scores = []
    for d in range(6):
        tf = A[:, d].astype(float)
        s = 0.0
        for i, term in enumerate(terms):
            if q[i] > 0 and tf[i] > 0:
                # Full BM25 relevance-feedback formula
                w_i = np.log(
                    ((r_i[i] + 0.5) / (R - r_i[i] + 0.5)) /
                    ((n_i[i] - r_i[i] + 0.5) / (N - n_i[i] - R + r_i[i] + 0.5))
                )
                term_score = w_i * ((k1 + 1) * tf[i]) / (K + tf[i]) * ((k2 + 1) * q[i]) / (k2 + q[i])
                s += term_score
        scores.append(s)

    # Output
    print("===== BM25 with Relevance Feedback =====")
    print(f"N={N}, R={R}")
    print(f"Terms: {terms}")
    print(f"n_i: {n_i}")
    print(f"r_i: {r_i}")
    print(f"L_avg={L_avg:.2f}")
    print(f"Query terms: {list(q_terms)}")
    print("\nDocument Scores:")
    for i, sc in enumerate(scores, 1):
        print(f"d{i}: {sc:.4f}")

    ranked = sorted(enumerate(scores, 1), key=lambda x: x[1], reverse=True)
    print("\nFinal Ranking (highest → lowest):")
    print(" > ".join([f"d{doc}" for doc, _ in ranked]))

    return terms, n_i, r_i, scores
def print_results():
    # -------------------------------
    # Binary Independence Model (BIM)
    # -------------------------------
    terms, n_i, r_i, bim_scores = compute_bim()
    ranked_bim = sorted(enumerate(bim_scores, start=1), key=lambda x: x[1], reverse=True)

    print("===== Binary Independence Model (BIM) =====")
    for t, ni, ri in zip(terms, n_i, r_i):
        print(f"{t:<10s}  n_i={ni:<2d}  r_i={ri:<2d}")
    print("\nDocument Scores:")
    for i, s in enumerate(bim_scores, start=1):
        print(f"d{i}: {s:.4f}")
    print("\nFinal Ranking (highest → lowest):")
    print(" > ".join([f"d{doc}" for doc, _ in ranked_bim]))
    print("\n" + "="*60)

    # -------------------------------
    # BM25
    # -------------------------------
    terms, _,_, bm25_scores = compute_bm25()
    ranked_bm25 = sorted(enumerate(bm25_scores, start=1), key=lambda x: x[1], reverse=True)

    print("\n===== BM25 Model =====")
    print("\nDocument Scores:")
    for i, s in enumerate(bm25_scores, start=1):
        print(f"d{i}: {s:.4f}")
    print("\nFinal Ranking (highest → lowest):")
    print(" > ".join([f"d{doc}" for doc, _ in ranked_bm25]))
    print("="*60)

print_results()
