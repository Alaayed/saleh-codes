#include <iostream>
#include <vector>
#include <algorithm>
using namespace std; 
int main() {
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		vector <int> h(n);
		for (int j =0; j < n; j++) { cin >> h[j];}
		int hMin,hMax;
		hMax = *max_element(h.begin(), h.end());
		hMin = *min_element(h.begin(), h.end());
		cout << hMax - hMin + 1 << '\n';
	} 
	return 0;
}
