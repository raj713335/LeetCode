# https://leetcode.com/problems/number-of-senior-citizens/description/

class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0

        for i in range(0, len(details)):
            if int(details[i][-4:-2]) > 60:
                count += 1

        return count
