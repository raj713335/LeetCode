# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

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
                    
        
