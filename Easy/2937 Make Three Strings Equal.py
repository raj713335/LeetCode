# https://leetcode.com/problems/make-three-strings-equal/description/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        count = 0

        if s1 == s2 and s2 == s3:
            return 0

        for i in range(0, min(len(s1), len(s2), len(s3))):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                count += 1
            else:
                break

        if count < 1:
            return -1

        return ((len(s1) - count) + (len(s2) - count) + (len(s3) - count))

        
