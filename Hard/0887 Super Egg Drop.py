# https://leetcode.com/problems/super-egg-drop/description/


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        dp = {}

        def mcm(k, n):

            if n == 0 or n == 1:
                return n
            
            if k == 1:
                return n

            if (k, n) in dp:
                return dp[(k, n)]

            min_moves = float("inf")

            low, high = 1, n
            min_moves = float('inf')

            while low <= high:
                mid = (low + high) // 2

                if (k - 1, mid - 1) not in dp:
                    dp[(k - 1, mid - 1)] = mcm(k - 1, mid - 1)
                egg_break = dp[(k - 1, mid - 1)]

                if (k, n - mid) not in dp:
                    dp[(k, n - mid)] = mcm(k, n - mid)
                not_egg_break = dp[(k, n - mid)]

                temp = 1 + max(egg_break, not_egg_break)
                min_moves = min(min_moves, temp)

                # Use binary search to reduce worst-case number of checks
                if egg_break > not_egg_break:
                    high = mid - 1
                else:
                    low = mid + 1

            dp[(k, n)] = min_moves
            return dp[(k, n)]

        return mcm(k, n)
