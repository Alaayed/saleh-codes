//
// Created by saleh on 3/2/2026.
//
// Link : https://codeforces.com/contest/2200/problem/D

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
vi cyclic_shift (const vi & a, int x, int y) {
    vi middle(a.begin() + x, a.begin()+y);
    auto min_pos = min_element(middle.begin(), middle.end());
    rotate(middle.begin(), min_pos, middle.end() );
    return middle;
}
void solve_testcase() {
    int n,x,y;
    // middle section [x,y)
    cin >> n >> x >> y;
    vi a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vi cyclic_section = cyclic_shift (a, x, y);
    int cyclic_min = cyclic_section.empty() ? std::numeric_limits<int>::max() : cyclic_section[0];
    vi remaining_section;
    remaining_section.insert(remaining_section.begin(), a.begin(), a.begin()+x);
    remaining_section.insert(remaining_section.end(), a.begin()+y, a.end());

    auto it = find_if(
        remaining_section.begin(),
        remaining_section.end(),
        [cyclic_min](int x) {
            return cyclic_min < x;
        });
    remaining_section.insert(it, cyclic_section.begin(), cyclic_section.end());
    for (int v : remaining_section) cout << v << " ";
    cout << '\n';
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int t; cin >> t;
    while (t--) solve_testcase();
}
