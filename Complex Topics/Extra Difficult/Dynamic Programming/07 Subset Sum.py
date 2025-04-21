def subset_sum_recursive(arr, target):
    n = len(arr)
    memo = {}

    def dfs(i, remaining):
        # Base Case: If sum is 0, we can always achieve it (empty subset)
        if remaining == 0:
            return True
        # If no items left or remaining < 0
        if i == 0:
            return arr[0] == remaining

        # Check memo
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Option 1: Not take the current item
        not_take = dfs(i - 1, remaining)

        # Option 2: Take the current item if it fits
        take = False
        if arr[i] <= remaining:
            take = dfs(i - 1, remaining - arr[i])

        memo[(i, remaining)] = take or not_take
        return memo[(i, remaining)]

    return dfs(n - 1, target)
