#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define MAXN 100005
#define MOD 998244353
vi adj[MAXN];
vi dfs(int cur, int parent) {
    int dangling_edges = 0;
    int must_use_edges = 0;
    for (int child : adj[cur]) {
        if (child == parent) continue;
        vi res = dfs(child, cur);
        must_use_edges += res[0];
        dangling_edges += res[1];
    }
    return {must_use_edges, dangling_edges};
}
int main()
{
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int n;
    cin >> n;
    int m = n - 1;
    rep(i, 0, m)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    // arb root at 1
    cout << dfs(1, -1)[2] << '\n';
}