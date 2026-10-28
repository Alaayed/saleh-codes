#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve_testcase() {
	int x,y,r; cin >> x >> y >> r;
	cout << x + r << " " << y << "\n"; 
}
void solve() {
	int t; cin >> t;
	while (t--) solve_testcase();
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	solve();
}
