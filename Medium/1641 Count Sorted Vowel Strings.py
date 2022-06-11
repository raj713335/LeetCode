https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # The formula is (n+5-1)C(n)=(n+4)C(n)
	    return (n+4)*(n+3)*(n+2)*(n+1)//24
        
