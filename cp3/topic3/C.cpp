#include <bits/stdc++.h>
using namespace std;
long long diff[1000000 + 5];
int a[1000000 + 5];
static inline void range_add(int L, int R, long long v) {
    if (L > R ) return;     // clamp by 0
    diff[L] += v;
    diff[R + 1] -= v;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	//cout << "HERE" << endl;
    int n,w;
    cin >> n >> w;
	multiset<int> ms;
    for (int k = 0; k < n; k++) {
        int l; cin >> l;
        for (int i=0; i < l; i++) cin >> a[i];
        int addi=0, remi=0, prev=0, m=w-l;
        ms.clear();
    	//cout << m << endl;

        if (m != 0) ms.insert(0);
    	bool removed_first_zero = false;
    	bool added_last_zero    = false;
    	//cout << "HERE" << endl;
		while (addi < l or remi < l) {
			int cur_add, cur_rem,idx;
			cur_add = (addi < l ? addi : INT_MAX);
			cur_rem = (remi < l ? (m+remi) : INT_MAX);
			idx = min(cur_add, cur_rem);
			if (not removed_first_zero) {
				idx = min(idx, m);
				removed_first_zero = idx == m;
			}
			if (not added_last_zero) {
				idx = min(idx, w-m);
				added_last_zero = idx == w;
			}
			// cannot slide window away
			//if (idx == m) ms.erase(0);
			//if (idx == (w-m)) ms.insert(0);
			// handle the gap
			range_add(prev, idx-1, (ms.empty() ? 0 :*ms.rbegin()));
			// apply update
			if (addi < l and cur_add == idx) {
				ms.insert(a[addi]); addi++;
			}
			if (idx == w-m) ms.insert(0);
			range_add(idx, idx, *ms.rbegin());
			//
			if (remi < l and (m+remi) == idx) {

				auto it = ms.find(a[remi]);
				if (it != ms.end()) ms.erase(it);
				remi++;
			}
			// cannot shift after this
			if (idx == m-1) {
				auto it= ms.find(0);
				if (it != ms.end()) ms.erase(it);
			}
			prev = idx+1;
		}
    	//range_add(diff, prev, w-1, *ms.rbegin());
    }
	//cout <<"HERE"<<endl;
	long long prefix_sum=0;
	//cout << prefix_sum << endl;
	for (int j = 0 ; j < w; j++) {
		prefix_sum += diff[j];
		cout << prefix_sum << ' ';
	}
	cout  << endl;
}