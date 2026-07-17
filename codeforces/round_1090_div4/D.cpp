#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
// Need to generate primes up to 10^5 for this problem, so we can precompute them
vector<int> sieve(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (long long i = 2; i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}
// TODO: some error causing failure on testcase 8.
void verify_array(vector<ll> const &a) {
    int n = sz(a);
    unordered_set<ll> seen;
    rep(i,0,n-1) {
        int g = gcd(a[i], a[i+1]);
        if (seen.contains(g)) {
            cout << "Duplicate gcd found: " << g << '\n';
            return;
        }
        seen.insert(g);
    }
    cout << "All gcds are unique.\n";
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    vector<int> primes = sieve(300'000); // 20000th prime is 224737, so this is more than enough
    int t; cin >> t;
    while (t--) {
        int n; cin  >> n;
        vector<ll> a(n);
        rep(i , 0,n) a[i] = (ll) primes[i] * primes[i+1];
        rep(i , 0 , n) cout << a[i] << ' ';
        cout << '\n';
        //verify_array(a);
    }
}
