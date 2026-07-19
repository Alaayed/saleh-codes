#include<iostream>
#include <vector>
#include <algorithm>
#include <format>
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
void solve() {
	int n, k; std::cin >> n >> k;
	std::vector<int> arr(n);
	for (int i = 0; i < n; i++) std::cin >> arr[i];
	// Sort in descending order
	std::sort(rall(arr));
	// Build freq table 
	std::vector<std::pair<int,int>> freq;
	int cur = arr[0];
	int count = 0;
	for (int i : arr ){
		if (i == cur) {
			count++;
		} else {
			freq.emplace_back(cur, count);
			cur = i;
			count = 1;
		}
	}
	// push the dangling cur and count
	freq.emplace_back(cur, count);
	for (int i = 0; i < (int) freq.size(); i++) {
		auto [num,count] = freq[i];
		if (count % 2 == 0) {
			std::cout << "YES\n";
			return;
		}
		// ensure there is another item to check
		if (i+1 == (int) freq.size()) {
			break;
		}
		auto [nextNum, _] = freq[i+1];
		// if it's in reach, jump there and egor insta wins
		if (nextNum + k >= num) {
			std::cout << "YES\n";
			return;
		}
		// otherwise, keep searching.
	}
	std::cout << "NO\n";
}
int main() {
	int t; std::cin >> t;
	while (t--) solve();	
}
