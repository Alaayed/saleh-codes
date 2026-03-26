from __future__ import annotations
from typing import List


class FenwickTree:
    """
    1-indexed Fenwick Tree (BIT) for prefix sums.
    Supports:
      - add(i, delta)
      - sum(i) = a[1] + ... + a[i]
      - range_sum(l, r) = sum(r) - sum(l-1)
    """

    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be positive")
        self.n = n
        self.bit = [0] * (n + 1)

    @staticmethod
    def _lsb(i: int) -> int:
        return i & -i

    def add(self, i: int, delta: int) -> None:
        if i <= 0 or i > self.n:
            raise IndexError("FenwickTree index out of bounds (must be 1..n)")
        while i <= self.n:
            self.bit[i] += delta
            i += self._lsb(i)

    def sum(self, i: int) -> int:
        """Prefix sum a[1..i]. If i == 0, returns 0."""
        if i < 0 or i > self.n:
            raise IndexError("FenwickTree prefix index out of bounds (must be 0..n)")
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self._lsb(i)
        return res

    def range_sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        if l <= 0 or r > self.n:
            raise IndexError("FenwickTree range out of bounds (must be within 1..n)")
        return self.sum(r) - self.sum(l - 1)

    @classmethod
    def from_list(cls, a_1_indexed: List[int]) -> FenwickTree:
        """
        Build from a 1-indexed list where a[0] is a dummy.
        Example: a = [0, 5, -2, 7]  # n=3
        """
        if len(a_1_indexed) < 2:
            raise ValueError("Need a 1-indexed list with a dummy 0 at index 0")
        n = len(a_1_indexed) - 1
        ft = cls(n)
        for i in range(1, n + 1):
            ft.add(i, a_1_indexed[i])
        return ft



from __future__ import annotations
from typing import List


class SegmentTreeMax:
    """
    Recursive segment tree for:
      - point update: a[pos] = val
      - range query: max(a[l..r])

    Matches the slides' template:
      - tree indexed like a heap (v, 2v, 2v+1)
      - pull(v) = max(children)
      - query has 3 cases: disjoint / contained / partial overlap
      - recommended size ~ 4*n
    :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}
    """

    def __init__(self, a_1_indexed: List[int]):
        if len(a_1_indexed) < 2:
            raise ValueError("Provide a 1-indexed list with dummy at index 0")
        self.n = len(a_1_indexed) - 1
        self.a = a_1_indexed
        self.t = [float("-inf")] * (4 * self.n + 5)
        self._build(1, 1, self.n)

    def _pull(self, v: int) -> None:
        self.t[v] = max(self.t[2 * v], self.t[2 * v + 1])

    def _build(self, v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.t[v] = self.a[tl]
            return
        tm = (tl + tr) // 2
        self._build(2 * v, tl, tm)
        self._build(2 * v + 1, tm + 1, tr)
        self._pull(v)

    def update(self, pos: int, val: int) -> None:
        """Set a[pos] = val (1-indexed)."""
        if pos <= 0 or pos > self.n:
            raise IndexError("pos out of bounds (must be 1..n)")
        self._update(1, 1, self.n, pos, val)

    def _update(self, v: int, tl: int, tr: int, pos: int, val: int) -> None:
        if tl == tr:
            self.t[v] = val
            return
        tm = (tl + tr) // 2
        if pos <= tm:
            self._update(2 * v, tl, tm, pos, val)
        else:
            self._update(2 * v + 1, tm + 1, tr, pos, val)
        self._pull(v)

    def query(self, l: int, r: int) -> int:
        """Return max(a[l..r]) (1-indexed)."""
        if l > r:
            return float("-inf")
        if l <= 0 or r > self.n:
            raise IndexError("query range out of bounds (must be within 1..n)")
        return self._query(1, 1, self.n, l, r)

    def _query(self, v: int, tl: int, tr: int, ql: int, qr: int) -> int:
        # case 1: disjoint
        if qr < tl or tr < ql:
            return float("-inf")
        # case 2: fully contained
        if ql <= tl and tr <= qr:
            return self.t[v]
        # case 3: partial overlap
        tm = (tl + tr) // 2
        left = self._query(2 * v, tl, tm, ql, qr)
        right = self._query(2 * v + 1, tm + 1, tr, ql, qr)
        return max(left, right)
