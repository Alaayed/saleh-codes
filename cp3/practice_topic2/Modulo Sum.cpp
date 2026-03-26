// Look to Modulo Sum.py for episode 1 :)
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int n,m;
	// Input
	cin >> n >> m;
	vector<int> nums(n);
	rep(i , 0 , n) {
		cin >> nums[i];
	}
	if (n > m) { cout << 'YES' << '\n'; return 0;}
	// processing
	vi current(m, 0);
	vi previous(m,0);
	rep (i , 1, n+1) {
		swap(current, previous);
		fill(current.begin(), current.end(), 0);
		rep(j,0 , m) {// CPP mod operation keeps negative results :(
			current[j] = max(previous[j] , previous[((j-nums[i-1]) % m+m) % m]);
			current[j] = max(current[j], nums[i-1] % m == j ? 1 : 0);
		}
	}
	cout << (current[0] == 1 ? "YES" : "NO") << '\n';
}