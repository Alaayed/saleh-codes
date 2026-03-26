#include <bits/stdc++.h>  // This will work only for g++ compiler.
using namespace std;
int tsize;
int tree[200001];

void update(vector<int> &tree, int index, int value) {
	for (int i = index; i < tree.size(); i += i & (-i))
		tree[i] += value;
}
int query (vector<int> &tree, int index) {
	int ret = 0;
	for (int i = index; i > 0; i -= i & (-i)) {
		ret += tree[i];
	}
	return ret;
}
void prep(vector<int> &tree, vector<int> &mapping, int m, int r) {
	for (int i =1+r; i < 1+r+m;i++)
		update(tree, i, 1);
	for (int i =1; i < m+1; i++)
		mapping[i] = i+r;
}
void handle_watch(
vector<int> &tree, 
vector<int> &mapping, 
int movie,
int prevreq,
int r
) {
	int above;
	// First, query the movies above
	above = query(tree, mapping[movie] - 1);
	// Change init pos to be 0
	update (tree, mapping[movie] , -1);
	// change mapping
	mapping[movie] = r- prevreq;
	// Change new mapping to 1
	update( tree, mapping[movie] , 1);
	if (prevreq != 0)
		cout << " " << above;
	else
		cout << above;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;
	for (int i = 0; i < n ; i++) {
		int m,r;
		cin >> m >> r;
		vector<int> tree (m+r +1, 0);
		vector<int> mapping(m+1, 0);

		prep(tree,mapping, m , r);
		for (int j = 0; j < r; j++) {
			int movie;
			cin >> movie;
			handle_watch( tree, mapping, movie, j , r);
		}
		cout << '\n';
	}
	return 0;
}
