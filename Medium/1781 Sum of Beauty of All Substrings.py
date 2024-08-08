# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            counter = Counter()
            for j in range(i, len(s)):
                counter[s[j]] += 1
                ans += max(counter.values()) - min(counter.values())
        return ans
        
