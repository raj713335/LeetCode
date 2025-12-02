# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/description/

class Solution:
    def maxDistance(self, words: List[str]) -> int:

        max_distance = 0

        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] != words[j]:
                    temp = j - i + 1

                    if temp > max_distance:
                        max_distance = temp

        return max_distance
        
