def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If we don't take the current item
            dp[i][w] = dp[i - 1][w]

            # If we take the current item (check if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][capacity]
