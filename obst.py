def obst(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = freq[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = 999
            total = sum(freq[i:j + 1])
            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cost = left + right + total
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]
keys = [10, 20, 30]
freq = [34, 8, 50]
print("Minimum OBST cost:", obst(keys, freq))
