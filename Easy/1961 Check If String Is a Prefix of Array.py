# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        

        
        for i in range(0, len(words)):
            print(s, "".join(words[:i+1]))
            if s == "".join(words[:i+1]):
                return True
        return False
