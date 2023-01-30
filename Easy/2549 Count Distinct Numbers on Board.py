# https://leetcode.com/problems/count-distinct-numbers-on-board/description/


class Solution:

    def distinctIntegers(self, n: int) -> int:

        count = 0

        res = set()

        if n == 1 or n == 2:

            return 1

        while n >= 2:

            for i in range(n-1, 0, -1):

                if n % i == 1:
                    

                    res.add(n)

                    res.add(i)

                    count += 1

            n -= 1

        return len(res)
