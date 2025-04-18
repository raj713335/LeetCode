# https://leetcode.com/problems/remove-boxes/description/

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        dp = {}

        compressed = []
        count = 1
        for i in range(1, len(boxes)):
            if boxes[i] == boxes[i - 1]:
                count += 1
            else:
                compressed.append((boxes[i - 1], count))
                count = 1
        compressed.append((boxes[-1], count))

        colors = [c for c, _ in compressed]
        counts = [cnt for _, cnt in compressed]
        n = len(colors)

        cache = {}

        def dp(l, r, k):
            if l > r:
                return 0
            if (l, r, k) in cache:
                return cache[(l, r, k)]

            # Merge trailing boxes of the same color
            orig_r, orig_k = r, k
            while r > l and colors[r] == colors[r - 1]:
                k += counts[r - 1]
                r -= 1

            # Case 1: remove [r] and trailing boxes
            res = dp(l, r - 1, 0) + (counts[r] + k) ** 2

            # Case 2: try to merge earlier same-color boxes
            for i in range(l, r):
                if colors[i] == colors[r]:
                    res = max(res,
                              dp(l, i, counts[r] + k) + dp(i + 1, r - 1, 0))

            cache[(l, orig_r, orig_k)] = res
            return res

        return dp(0, n - 1, 0)
        
