#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

class lab {
public:
	ll a,b,c, cost;
	lab() : a(0), b(0),c(0) {}
	friend istream& operator>>(istream&in , lab& obj) {
		in >> obj.a >> obj.b >> obj.c;
		return in;
	}
	[[nodiscard]] ll upfront_cost() {
		// if c > b > a, 
		// b += sgn(a-ci)*(b-a+1)
		// b =b -b+a-1
		// b = a-1
		// since our total score also tanked
		// Double to get back to baseline
		if  (c == b and b == a)  {
			return LLONG_MAX;
		}
		return c >= b and b >= a ? 2*(min(c-b,b-a) + 1) : 0;
	}
	void calculate_cost() {
		cost = c+b+a;
	}
};
void solve() {
	int n; ll k; cin >> n >> k;
	vector<lab> labs(n);
	rep(i , 0, n) {
		cin >> labs[i];
		//cout << "abc: ";
		//cout << labs[i].a << labs[i].b << labs[i].c << '\n';
		labs[i].calculate_cost();
		//cout << "cost: " << labs[i].cost << '\n';
	}
	sort(all(labs), [](const lab& x, const lab& y) {
				return x.cost < y.cost;
			} 
			);
	ll actions_budget = k;
	ll min_lab = labs[0].cost;
	// pay initial upfront cost 
	actions_budget = max(0ll, actions_budget - labs[0].upfront_cost() );
	rep(i, 1, n) {
		// Question in each loop, how much get everything below up to i?
		int elements_beneath = i;
		// Assume upfront costs already paid.
		ll difference = labs[i].cost - labs[i-1].cost;
		ll total_difference = difference*elements_beneath;
		// Do we have the budget?
		if (actions_budget >= total_difference) {
			// yes, pay it.
			actions_budget -= total_difference;
			min_lab = labs[i].cost;
		} else {
			// No, we cant make it pay as much as possible
			min_lab += ll (actions_budget/elements_beneath);
			cout << min_lab << "\n";
			return;
		}
		// pay upfront cost
		ll upfront_cost = labs[i].upfront_cost();
		if (upfront_cost > actions_budget) {
			cout << min_lab << '\n';
			return;
		}
		actions_budget -= labs[i].upfront_cost();
	}
	if (actions_budget > 0) {
		// integer divison 
		min_lab += ll (actions_budget/n);
	}
	cout << min_lab << "\n";
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t; cin >> t;

	while (t--) solve();
}
