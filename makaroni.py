k, n = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(k + 1):
    dp[i][0] = 0
for j in range(n + 1):
    dp[0][j] = 0

for trials in range(1, n + 1):
    for structures in range(1, k + 1):
        dp[structures][trials] = dp[structures - 1][trials - 1] + dp[structures][trials - 1] + 1
        if dp[structures][trials] >= n:
            print(trials)
            exit()

print(-1)
