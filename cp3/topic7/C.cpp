#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;
struct PT{
    ll temp;
    ll pos;
    PT(){}
};
ll TEMP(ll x, PT &p) {
    return p.temp + abs(p.pos - x);
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t; cin>>t;
    while(t--) {
        int n,k; cin>>n>>k;
        vector<PT> pts(k);
        for(int i = 0; i < k; ++i){
            cin>>pts[i].pos;
            --pts[i].pos;
        }
        for(int i = 0; i < k; ++i){
            cin>>pts[i].temp;
        }
        sort(pts.begin(), pts.end(), [](const PT &a, const PT &b) {
            return a.pos < b.pos;
        });
        vector<ll> ans(n, (ll) 1e18);
        vector<ll> tbp(n, (ll) 1e18);

        for (int i = 0; i < k; i++) 
        {
            tbp[pts[i].pos] = pts[i].temp;
        }
        int p = 0;
        for(ll x = 0; x < n; ++x) {
            // while (p != k-1 && (TEMP(x,pts[p+1]) < TEMP(x, pts[p]))) {
            //     ++p;
            // }
            if (tbp[x] < TEMP(x,pts[p])) {
                pts[p].pos = x;
                pts[p].temp = tbp[x];
            }
            ans[x] = min(ans[x], TEMP(x,pts[p]));
        }
        p = k-1;
        for(ll x = n-1; x >= 0; --x) {
            // while (p != 0 && (TEMP(x,z[p-1]) < TEMP(x, pts[p]))) {
            //     --p;
            // }
            if (tbp[x] < TEMP(x,pts[p])) {
                pts[p].pos = x;
                pts[p].temp = tbp[x];
            }
            ans[x] = min(ans[x], TEMP(x,pts[p]));
        }
        // for (int i = 0; i < k; i++) 
        // {
        //     ans[pts[i].pos] = pts[i].temp;
        // }
        for(int i = 0; i < n; ++i){
            cout<<ans[i]<<" ";
        }cout<<"\n";
    }
}

