// Link : https://codeforces.com/contest/2218/problem/F
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
    while (t--) {
        int even,odd; cin >> even >> odd;
        int parity = (even+odd) % 2;
        // Each even subtree node must have 1 odd terminal node child. if two even subtrees share the same
        // odd terminal node, then there is one odd node between the two subtrees, as one must be the ancestor of the other. 
        // Therefore, each even subtree must have a unique odd node child. 
        // Therefore, the number of even subtrees must be less than or equal to the number of odd nodes.   
        if (even > odd || (parity == 0 and even == 0) || (parity == 1 and odd == 0)) {cout  << "NO\n"; continue;}
        cout << "YES\n";
        if (parity == 0) even--;
        else odd--;
        int cur = 2;
        while (even) {
            cout << "1 " << cur << '\n';
            cout << cur << ' ' << cur+1 << '\n';
            cur += 2;
            even--;
            odd--;
        }
        while (odd--) {
            cout << "1 " << cur << '\n';
            cur++;
        }

    }
}