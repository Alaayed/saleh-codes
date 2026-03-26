#include <bits/stdc++.h>  // This will work only for g++ compiler.
using namespace std;
int tsize;
long tree[5000001];
inline void add(int index, int value) {
	for (int i = index; i < tsize; i += i & (-i)){
		tree[i] += value;
	}

}

inline long query (int index) {
	int ret =0;
	for (int i = index; i > 0; i -= i & (-i))
		ret += tree[i];
	return ret;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int q;
	cin >> tsize >> q;
	tsize++;
	int index , value , i;
	char operation;
	for (i = 0; i < q; i++) {
		cin >> operation >> index;
		if (operation == '+') {
			cin >> value;
			add (index+1 , value);
		} else {
			cout << query(index) << endl;
		}
	}
	return 0;
}
