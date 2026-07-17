#include<iostream>
#include <vector>
#include <algorithm>
#define all(x) x.begin(), x.end()
int MAX_ALLOWED = 20'000;
int MIN_ELEMENT; 
bool roll_down(int roof, int k, std::vector<int> &arr) {
	auto max_below_threshold = [roof](int a, int b) {
		bool a_valid = a < roof;
		bool b_valid = b < roof;
		if (a_valid && b_valid) return a < b;
		return a_valid < b_valid;
	};
	if (roof <= MIN_ELEMENT) return false; // cant roll down
	int amax = * std::max_element(all(arr), max_below_threshold);
	int acount = std::count(all(arr), amax);
	// Second pick wins
	if (acount % 2 == 0) return true;
	// First pick wins, but some value exists that we jump off of.
	if (std::any_of(all(arr), [amax,k](int n) {return ((amax-n)<=k) and n < amax;})) {
		return true;
	}
	// nothing, roll down and check
	return roll_down(amax-k, k, arr);
}
void solve() {
	int n, k; std::cin >> n >> k;
	std::vector<int> arr(n);
	for (int i = 0; i < n; i++) std::cin >> arr[i];
	MIN_ELEMENT = * std::min_element(all(arr));
	std::cout << (roll_down(MAX_ALLOWED, k , arr) ? "YES" : "NO") << '\n';

}
int main() {
	int t; std::cin >> t;
	while (t--) solve();	
}
