# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        ans = []
        rem = 0

        for i in range(0, len(word)):
            rem = (rem * 10 +int(word[i]))%m 
            if int(rem) % m == 0:
                ans.append(1)
            else:
                ans.append(0)

        return ans
        
