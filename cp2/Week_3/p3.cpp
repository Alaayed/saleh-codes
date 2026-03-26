#include <bits/stdc++.h>  // This will work only for g++ compiler. 
using namespace std;
void solve(int k , int c);
void solve(int k, int c) {
	// Assumption, mod c below k
	c = c % k;
	//
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n,k,c;
	cin >> n;
	for (int i =0; i < n; i++) {
		cin >> k >> c;
		solve(k , c);
	}
	
	return 0;
}
