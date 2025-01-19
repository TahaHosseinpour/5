#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> prices(n);
    for (int i = 0; i < n; ++i) {
        cin >> prices[i];
    }

    vector<vector<int>> dp(n + 1, vector<int>(2, 0));

    dp[0][0] = 0;
    dp[0][1] = 0;
    dp[1][0] = prices[0];
    dp[1][1] = prices[0];

    for (int i = 2; i <= n; ++i) {
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i - 1];

        vector<int> new_list;
        for (int j = ceil(i / 2.0); j < i; ++j) {
            int price_test = prices[j - 1];
            price_test += min(dp[j - 1][0], dp[j - 1][1]);
            new_list.push_back(price_test);
        }

        dp[i][1] = *min_element(new_list.begin(), new_list.end());
    }

    cout << min(dp[n][0], dp[n][1]) << endl;

    return 0;
}
