//
// Created by saleh on 2/27/2026.
//
// link: https://codeforces.com/contest/2200/problem/B

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

bool test_permutation(int mask, const vi &a, int n) {
    int prev = -1;
    // Check if none decreasing
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
            if ((prev > a[i])) return false;
            prev = a[i];
        }
    }
    return true;
}
void solve_test_case() {
    int n,current_min; cin >> n;
    vi a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int prev = -1;
    bool is_nondec = true;
    for (int i = 0; i < n; i++) {
        if (a[i] < prev) {is_nondec = false; break;}
        prev = a[i];
    }
    cout << (is_nondec ? n : 1) << '\n';
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int t; cin >> t;
    while(t--) { solve_test_case();}

}
