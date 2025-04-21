def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False  # Cannot split odd total into two equal parts

    target = total_sum // 2
    n = len(arr)
    memo = {}

    def dfs(i, remaining):
        if remaining == 0:
            return True
        if i == 0:
            return arr[0] == remaining
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        not_take = dfs(i - 1, remaining)
        take = False
        if arr[i] <= remaining:
            take = dfs(i - 1, remaining - arr[i])

        memo[(i, remaining)] = take or not_take
        return memo[(i, remaining)]

    return dfs(n - 1, target)
