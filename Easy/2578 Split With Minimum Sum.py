# https://leetcode.com/problems/split-with-minimum-sum/description/


class Solution:
    def splitNum(self, num: int) -> int:

        sum1 = ""
        sum2 = ""

        num = sorted(list(str(num)))

        for i in range(0, len(num)):
            if i % 2 == 0:
                sum1 += num[i]
            else:
                sum2 += num[i]

        return int(sum1) + int(sum2) 
