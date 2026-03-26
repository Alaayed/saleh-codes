//
// Created by saleh on 3/10/2026.
//

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
vi bfs( const vector<vi> & graph, int n) {
    vi dist((n+1)*2, INT_MAX);
    queue<int> q;
    dist[1] = 0;
    q.push(1);
    while(!q.empty()) {
        int v = q.front();
        q.pop();
        // Process children
        for (int child : graph[v]) {
            if (dist[child] != INT_MAX) continue;
            dist[child] = dist[v]+1;
            q.push(child);
        }
    }
    return dist;
}
void solve_testcase() {
    int n,m,l; cin >> n >> m >> l;
    // 1 .. n
    // 0 .. n-1
    vector<vi> graph((n+1)* 2);
    // Read in A
    multiset<int> A;
    rep (i , 0 ,l) {int t; cin >> t; A.insert(t);}
    // Find largest even and odd sums possible in A
    int sum = accumulate(A.begin(), A.end(), 0);
    int sodd = accumulate(A.begin(), A.end(), INT_MAX, [] (int acc , int x)
        {return (x % 2 == 1 and x < acc) ? x : acc;}
        );
    int even = sum % 2 == 0 ? sum : sum - sodd;
    int odd  = sum % 2 == 1 ? sum : sum - sodd;
    // read in the graph
    rep (i, 0, m) {
        int u,v; cin >> u >> v;
        // U_o -> V_e
        graph[u + n].push_back(v);
        graph[v].push_back(u+n);
        // U_e -> U_o
        graph[v+n].push_back(u);
        graph[u].push_back(v+n);
    }
    vi dist = bfs(graph, n);
    rep(i, 1 , n+1) {
        if (dist[i] <= even or dist[i+n] <= odd) cout << '1';
        else cout << '0';
    }
    cout << '\n';
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int t; cin >> t;
    while (t--) solve_testcase();
}