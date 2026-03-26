//
// Created by saleh on 3/1/2026.
//
// https://codeforces.com/contest/2200/problem/C

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

bool remove_adj_chars(vector<char> &a) {
    bool mutated = false;
    vector<int> to_remove;
    for (int i = 0; i < sz(a) - 1; i++) {
        if (a[i] == a[i + 1]) {
            to_remove.push_back(i);
            mutated = true;
            i++;
        }
    }
    while (not to_remove.empty()) {
        int index = to_remove.back();
        to_remove.pop_back();
        a.erase(a.begin() + index, a.begin() + index + 2);
    }
    return mutated;
}

void solve_testcase() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<char> a(s.begin(), s.end());
    while (remove_adj_chars(a));
    cout << (a.empty() ? "YES" : "NO") << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int t;
    cin >> t;
    while (t--) solve_testcase();
}
