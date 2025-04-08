# https://leetcode.com/problems/ones-and-zeroes/description/


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        nn = len(strs)

        pairs = []

        # Count the number of zeros and ones in each string and store as pairs
        for each in strs:
            zero = each.count("0")
            one = each.count("1")
            pairs.append([zero, one])

        dp = {}

        def dfs(index, zero, ones):
            # If we exceed the limits of zeros or ones, return 0
            if zero > m or ones > n:
                return 0
            elif index == nn:
                return 0
            elif (index, zero, ones) in dp:
                return dp[(index, zero, ones)]
            
            skip = dfs(index + 1, zero, ones)

            take = 0

            if zero + pairs[index][0] <= m and ones + pairs[index][1] <= n:  
                take = 1 + dfs(index + 1, zero + pairs[index][0], ones + pairs[index][1])

           
            dp[(index, zero, ones)] = max(skip, take)
            return dp[(index, zero, ones)]

        return dfs(0, 0, 0)
