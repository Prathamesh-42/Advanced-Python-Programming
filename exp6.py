# 0/1 Knapsack Problem

# Top-Down Approach (Memoization)
def knapsack_top_down(values, weights, W):
    n = len(values)
    memo = {}

    def solve(i, capacity):
        if i == 0 or capacity == 0:
            return 0

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        if weights[i - 1] <= capacity:
            include = values[i - 1] + solve(i - 1, capacity - weights[i - 1])
            exclude = solve(i - 1, capacity)
            memo[(i, capacity)] = max(include, exclude)
        else:
            memo[(i, capacity)] = solve(i - 1, capacity)

        return memo[(i, capacity)]

    return solve(n, W)


# Bottom-Up Approach (Tabulation)
def knapsack_bottom_up(values, weights, W):
    n = len(values)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]



values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Top-Down Result:", knapsack_top_down(values, weights, W))
print("Bottom-Up Result:", knapsack_bottom_up(values, weights, W))