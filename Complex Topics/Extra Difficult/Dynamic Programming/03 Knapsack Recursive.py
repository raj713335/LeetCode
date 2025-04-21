def knapsack_recursive(weights, values, capacity):
    n = len(weights)
    memo = {}

    def dfs(index, remaining):
        # Base case: no items or no capacity
        if index == n or remaining == 0:
            return 0

        # Check memoization
        if (index, remaining) in memo:
            return memo[(index, remaining)]

        # Option 1: skip current item
        not_take = dfs(index + 1, remaining)

        # Option 2: take current item (if it fits)
        take = 0
        if weights[index] <= remaining:
            take = values[index] + dfs(index + 1, remaining - weights[index])

        memo[(index, remaining)] = max(take, not_take)
        return memo[(index, remaining)]

    return dfs(0, capacity)
