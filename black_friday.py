import math
n = int(input())
prices = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n + 1)]

dp[0][0] = 0
dp[0][1] = 0
dp[1][0] = prices[0]
dp[1][1] = prices[0]

for i in range(2, n+1):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i-1]


    new_list = []
    for j in range(math.ceil(i/2) , i):
        price_test = prices[j-1]
        price_test += min(dp[j - 1][0],dp[j - 1][1])
        new_list.append(price_test)

    dp[i][1] = min(new_list)

print(min(dp[n][0], dp[n][1]))
# print(dp)
