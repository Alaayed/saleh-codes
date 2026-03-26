from heapq import heappush, heappop

INF = float('inf')

class MCMF:
    class Edge:
        def __init__(self, from_, to, rev, cap, cost):
            self.from_ = from_
            self.to = to
            self.rev = rev       # index of reverse edge in ed[to]
            self.cap = cap
            self.cost = cost
            self.flow = 0

    def __init__(self, N):
        self.N = N
        self.ed = [[] for _ in range(N)]
        self.pi = [0] * N
        self.dist = [INF] * N
        self.seen = [False] * N
        self.par = [None] * N  # par[v] = edge used to reach v

    def add_edge(self, from_, to, cap, cost):
        if from_ == to:
            return
        self.ed[from_].append(self.Edge(from_, to, len(self.ed[to]),   cap,  cost))
        self.ed[to  ].append(self.Edge(to, from_, len(self.ed[from_])-1, 0, -cost))

    def _path(self, s):
        self.seen = [False] * self.N
        self.dist = [INF] * self.N
        self.dist[s] = 0
        # min-heap of (dist, node)
        heap = [(0, s)]
        while heap:
            d, u = heappop(heap)
            if self.seen[u]:
                continue
            self.seen[u] = True
            di = self.dist[u] + self.pi[u]
            for e in self.ed[u]:
                if not self.seen[e.to] and e.cap - e.flow > 0:
                    val = di - self.pi[e.to] + e.cost
                    if val < self.dist[e.to]:
                        self.dist[e.to] = val
                        self.par[e.to] = e
                        heappush(heap, (self.dist[e.to], e.to))
        for i in range(self.N):
            self.pi[i] = min(self.pi[i] + self.dist[i], INF)

    def maxflow(self, s, t):
        totflow = 0
        totcost = 0
        while True:
            self._path(s)
            if not self.seen[t]:
                break
            # find bottleneck
            fl = INF
            x = self.par[t]
            while x is not None:
                fl = min(fl, x.cap - x.flow)
                x = self.par[x.from_]
            # augment
            x = self.par[t]
            while x is not None:
                x.flow += fl
                self.ed[x.to][x.rev].flow -= fl
                x = self.par[x.from_]
            totflow += fl
        for u in range(self.N):
            for e in self.ed[u]:
                totcost += e.cost * e.flow
        return totflow, totcost // 2

    def set_pi(self, s):
        """Call before maxflow if any edge costs are negative."""
        self.pi = [INF] * self.N
        self.pi[s] = 0
        changed = True
        iters = self.N
        while changed and iters > 0:
            changed = False
            iters -= 1
            for i in range(self.N):
                if self.pi[i] == INF:
                    continue
                for e in self.ed[i]:
                    if e.cap and self.pi[i] + e.cost < self.pi[e.to]:
                        self.pi[e.to] = self.pi[i] + e.cost
                        changed = True
        assert iters >= 0, "Negative cost cycle detected"


# ── Example: min-cost bipartite matching ────────────────────────────────────
if __name__ == "__main__":
    # cost[i][j] = cost of assigning worker i to job j
    cost = [
        [9, 2, 7],
        [3, 6, 1],
        [8, 4, 5],
    ]
    N = len(cost)
    S, T = 0, 2 * N + 1
    mcmf = MCMF(T + 1)

    for i in range(1, N + 1):
        mcmf.add_edge(S, i, 1, 0)           # source -> worker
    for j in range(1, N + 1):
        mcmf.add_edge(N + j, T, 1, 0)       # job -> sink
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            mcmf.add_edge(i, N + j, 1, cost[i-1][j-1])

    flow, total_cost = mcmf.maxflow(S, T)
    print(f"Workers assigned: {flow}/{N}")
    print(f"Minimum total cost: {total_cost}")

    print("Assignments:")
    for i in range(1, N + 1):
        for e in mcmf.ed[i]:
            if e.to != S and e.flow > 0:
                print(f"  Worker {i-1} -> Job {e.to - N - 1}  (cost {cost[i-1][e.to-N-1]})")