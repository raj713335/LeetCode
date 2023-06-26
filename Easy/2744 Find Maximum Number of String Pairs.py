# https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        count = 0

        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                temp = words[i]+words[j]
                if temp == temp[::-1]:
                    count += 1

        return count
