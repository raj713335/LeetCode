def unbounded_knapsack(W, wt, val, n):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def knapsack(i, w):
        # Base Case: No capacity or no items
        if i == 0 or w == 0:
            return 0

        if wt[i - 1] <= w:
            # Option 1: include current item (stay at i)
            # Option 2: exclude item (move to i - 1)
            return max(
                val[i - 1] + knapsack(i, w - wt[i - 1]),  # include item
                knapsack(i - 1, w)                        # exclude item
            )
        else:
            return knapsack(i - 1, w)  # Can't include item

    return knapsack(n, W)
