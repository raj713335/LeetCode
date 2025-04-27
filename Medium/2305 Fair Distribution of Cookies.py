# https://leetcode.com/problems/fair-distribution-of-cookies/description/


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        distribution_tracking = [0] * k

        def dfs(i: int, zero_count: int) -> int:

            # if there are not enough cookies to distribute to children with zero cookies
            if n - i < zero_count:
                return float('inf')

            # return maximum unfairness of a distribution
            if i == n:
                return max(distribution_tracking)

            # distribute cookies to children
            res = float('inf')
            for j in range(k):
                # if this children has zero mean not distribute yet, minus 1 because now he can have the bag
                zero_count -= int(distribution_tracking[j] == 0)

                # now we distribute cookie for him
                distribution_tracking[j] += cookies[i]

                # we move to next cookie
                res = min(res, dfs(i + 1, zero_count))

                # now we backtrack, we should follow the order
                # so because above zero_count then distribution_tracking
                # thus here should be distribution_tracking then zero_count
                distribution_tracking[j] -= cookies[i]

                zero_count += int(distribution_tracking[j] == 0)

            return res

        return dfs(0, k)
