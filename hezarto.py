maze = eval(input())

rows = len(maze)
cols = len(maze[0])

dp = [[0] * cols for _ in range(rows)]
dp[0][0] = maze[0][0]

for j in range(1, cols):
    dp[0][j] = dp[0][j - 1] + maze[0][j]

for i in range(1, rows):
    dp[i][0] = dp[i - 1][0] + maze[i][0]

for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + maze[i][j]

a = 10