#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
// Assumes 0<= pos <= n-5
ll triad(const vi& love, int pos) {
	return love[pos] + love[pos + 2] - love[pos + 4];
}
// Valid pairs for each audience love
// Keep count s.t. count[audience_love] = number of triads with love = audience_love
// We can keep keep count of the number of valid pairs where at each triad we count the valid pairs to its left 
// and minus overlapping prev triads. We therefor count each pair when we see its tail
void solve() {
	int n; cin >> n;
	vi love(n);
	unordered_map<ll,ll> love_counts(n);
	rep (i, 0, n) cin >> love[i];
	ll res = 0;
	// Solve
	rep (i, 0, n-4) {
		// get current triad value
		ll tlove = triad(love , i);
		// Number of pairs that have this love
		ll valid_pairs = love_counts[tlove];
		if (i >= 2 and triad(love, i-2) == tlove) valid_pairs--;
		if (i >= 4 and triad(love, i-4) == tlove) valid_pairs--;
			love_counts[tlove]++;
		res += valid_pairs; 

	}	
	cout << res << "\n";
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t; cin >> t;

	while (t--) solve();
}
