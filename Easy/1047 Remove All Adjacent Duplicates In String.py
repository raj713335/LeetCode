# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        res = []
        
        for each in s:
            if res and res[-1] == each:
                res.pop()
            else:
                res.append(each)
                
        return "".join(res)
        
