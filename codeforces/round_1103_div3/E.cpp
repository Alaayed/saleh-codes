#include <iostream>
#include <vector>
#define rep(i,b,c) for(int i = b; i < c; i++)
// Assuming s1 > s2 
int joined_pair (int s1, int e1, int s2, int e2) {
	int l1 = s1-e1, l2 = s2-e2;
	int overlap = s2-e2;
	if (overlap < -1)
}
int brute_force_solve(const std::vector<std::pair<int,int>> & segments) {
	int best = 0;
	int n = segments.size();
	rep(i, 0, n) {
		rep(j, i, n) {
			if (i == j) { // check if can split i in half
				auto [s,e] = segments[i];
				best = (s-e % 2 == 0) ? std::max(best, (s-e)/2) : best;
				continue;
			}
			auto [s1,e1] = segments[i];
			auto [s2,e2] = segments[j];

		}
	}
	return best;
}
void solve() {
	int n; std::cin >> n;
	std::vector<int> a(n);
	rep(i , 0, n) { std::cin >> a[i];}
	if (n == 1) {
		std::cout << 0 << '\n';
		return;
	}
	int start = a[0];
	int prev = a[0];
	std::vector<std::pair<int,int>> goodSegments;
	rep(i, 1, n) {
		if ( not ((a[i]+1) == prev )) {
			// Record segment 
			goodSegments.emplace_back(start, prev);
			// Reset state
			start = a[i];
		}
		prev = a[i];
	}


	
}

int main() {
	int t; std::cin >> t;
	while(t--) {
		solve();
	}

}
