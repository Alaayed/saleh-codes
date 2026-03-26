//
// Created by saleh on 2/27/2026.
//
// link :https://codeforces.com/contest/2200/problem/A
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define read_v(n, a) for(int i = 0; i < n; i++) cin >> (a[i])
void solve_testcase() {
    int n; cin >> n;
    vi a(n);
    read_v(n, a);
    // Find the max
    int maximum = *max_element(a.begin(), a.end());
    int c   =  count(a.begin(), a.end(), maximum);
    cout << c << '\n';
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int t;
    cin >> t;
    while(t--) {
        solve_testcase();
    }
}