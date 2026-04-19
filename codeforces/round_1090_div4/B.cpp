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
    int t; cin  >> t;
    while (t--) {
        vi a(7); rep(i, 0, 7) cin >> a[i];
        sort(all(a));
        int sum = 0;
        rep (i , 0 , 6) sum += a[i] * -1;
        sum += a[6];
        cout << sum << '\n';
    }
}