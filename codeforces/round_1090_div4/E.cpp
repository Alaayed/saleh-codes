// link : https://codeforces.com/contest/2218/problem/E
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
    int t; cin >> t;
    while(t--) {
        int n; cin  >> n;
        int cmax = -1;
        vi a(n);
        rep(i , 0 , n) cin >> a[i];
        rep(i,0,n) {
            rep(j, i+1, n) {
                cmax = max(cmax, a[i] ^ a[j]);
            }
        }
        cout << cmax << '\n';
    }

}