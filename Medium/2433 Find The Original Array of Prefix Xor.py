# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        output = [pref[0]]
        val = output[0]
        for i in range(1, len(pref)):
            if len(output) > 1:
                val ^= output[-1]
            output.append(val ^ pref[i])

        return output
