# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        output = [words[0]]

        for i in range(1, len(words)):
            if groups[i-1] != groups[i]:
                output.append(words[i])

        return output

        
