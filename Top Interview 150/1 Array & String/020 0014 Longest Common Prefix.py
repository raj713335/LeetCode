# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        index = 0
        n = len(strs)

        flag = True

        while flag and index < len(strs[0]):
            try:
                val = strs[0][index]
                for i in range(1, n):
                    if val != strs[i][index]:
                        flag = False
                
                if flag:
                    index += 1
            except:
                flag = False

        return strs[0][:index]
             

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        index = -1

        try:
            prefix = strs[0][0]
        except:
            return ""

        for i in range(0, len(strs[0])):
            flag = True
            try:
                for j in range(0, len(strs)):
                    if strs[j][i] != prefix:
                        flag = False
                        break

                if flag:
                    index += 1
                    prefix = strs[0][index+1]
                else:
                    break
            except:
                return strs[0][:index+1]

        if index == -1:
            return ""
        else:
            return strs[0][:index+1]
                    
        
