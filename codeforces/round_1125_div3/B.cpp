#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
void solve() {
	int n; cin >> n;
	string cmds; cin >> cmds;
	// Set up a stack
	vi stack;
	// Set up bitset
	vector<bool> bitmask(n);
	int i = 0;
	int running_counter = 0;
	for (char c : cmds) {
		if (c ==  '1') {
			stack.push_back(i);
		} else if (c == '2') {
			if (!stack.empty()) {
				bitmask[stack.back()] = true;
				stack.pop_back();
				running_counter += 1;
			}
		} else {
			bitmask[i] = true;
			running_counter +=1;
		}
		i++;
	}
	cout << n - running_counter << '\n';
	i = 1;
	for (bool is_printed : bitmask) {
		if (!is_printed) {
			cout << i << " ";
		}
		i++;
	}
	cout << '\n';
}		
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t; cin >> t;

	while (t--) solve();
}
