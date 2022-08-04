# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        value = letters[0]
        
        for each in letters:
            if each > target:
                return each
                
        return value
        
