#include <bits/stdc++.h>  // This will work only for g++ compiler. 
#include <climits>
int UPPER_BOUND = 1e9;
using namespace std;
void solve(int k , int c);
int inverse(int,int);
void solve(int k, int c) {
}
// https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
int inverse(int a, int n) {
	int t, r, newt, newr, quotient, temp;
	newt = 1; r = n; newr = a; t = 0;
	while (newr != 0) {
		quotient = r / newr;
		temp = newt;
		newt = t - quotient * newt;
		t = temp;
		temp = newr;
		newr = r - quotient * newr;
		r = temp;
	}
	if (r > 1) return INT_MIN;
	if (t < 0) return t+n;
	return t;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n,k,c;
	cin >> n;
	for (int i =0; i < n; i++) {
		cin >> k >> c;
		// Case k = 1, c = 1
		if (k==1 && c==1) {cout << 2 << endl; continue;}
		if (k==1) { cout << 1 <<endl; continue;}
		int res = inverse(c , k) + (c==1 ? k : 0);
		//cout << "res result: " << res << endl << "inverse: " << inverse(c,k) << endl; 
		if (res == INT_MIN || res > UPPER_BOUND || res == 0) 
		cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 0;
}
