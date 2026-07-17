#include <iostream>
#include <string>
using namespace std;
void solve() {
	int n,k; cin >> n >> k;
	string bstr; cin >> bstr;
	for (int i = 0 ; i + k < (int) bstr.length(); i++) {
		if (bstr[i] == '1') {
			bstr[i] = '0';
			bstr[i+k] = bstr[i+k] == '1' ? '0' : '1';
		}
	}
	for (char c : bstr) {
		if (c == '1') {
			cout << "NO" << '\n';
			return;
		}
	}
	cout << "YES" << '\n';
}
int main() {
	int t; cin >> t;
	while (t--) {
		solve();
	}
}
