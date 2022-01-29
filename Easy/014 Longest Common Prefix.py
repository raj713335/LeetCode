# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]
        iterx = 0
        
        while (iterx < (len(strs)-1)) and prefix!=0:
            iterx = 0
            for i in range(1, len(strs)):
                if strs[i].startswith(prefix):
                    iterx += 1
                    continue
                else:
                    prefix = prefix[:-1]
                    
        return prefix
                
            
                    
                    
            
            
        
