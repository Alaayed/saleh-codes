#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define readv(a, i,n) rep(i, 0 , n) cin >> a[i]
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int evaluate_end_node(vi& memo,vi& amemo, const vi& a, const vi& b, int n, int end_node) {
	// evaluate the forward pass
	if (memo[end_node] != 0) return memo[end_node];
	int cur = end_node;
	int cost = 0;
	int flip = 0;
	while (cur != n-1) {
		if (flip++ % 2 == 0)
			cost += a[cur] == b[cur+1] ? 2 : 1;
		else{
			cost += b[cur] == a[cur+1] ? 2 : 1;
			// Record the A result to remove from B later
			amemo[cur+1] = cost;
		}
		cur++;
	}
	// End of the forward pass
	if (flip++ % 2 == 0)
		cost += a[cur] == b[cur] ? 2 : 1;
	else{
		cost += b[cur] == a[cur] ? 2 : 1;
	}
		// backward pass
	
	while (cur != end_node) {
		if (flip++ % 2 == 0) {
			cost += a[cur] == b[cur-1] ? 2 : 1;
			memo[cur-1] = cost - amemo[cur-1];
		}else
			cost += b[cur] == a[cur-1] ? 2 : 1;
		cur--;
	}
	return cost;
}
void solve() {
	int n; cin >> n;
	vi a_memo(n ,0); vi b_memo(n,0);
	vi a(n); vi b(n);
	readv(a, i , n);
	readv(b,i,n);
	int best = -1;
	int running_cost = 0;
	for (int i = 0; i < n; i++) {
		int end_cost = evaluate_end_node(b_memo,a_memo, a, b,n, i);
		best = max(best, end_cost + running_cost);
		// Keep it pushing
		running_cost += a[i] == b[i] ? 2 : 1;
		// Connect diag connection
		if (i != n-1) 
			running_cost += b[i] == a[i+1] ? 2 : 1;
		else
			best = max(best, running_cost);
	}
	cout << best << "\n";
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t; cin >> t;
	while (t--) solve();
}
