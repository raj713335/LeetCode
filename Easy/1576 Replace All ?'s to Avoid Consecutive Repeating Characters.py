# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/


class Solution:
    def modifyString(self, s: str) -> str:
        
        s = list(s)

        words = ["a", "b", "c"]
        
        for i in range(0, len(s)):
            if i == 0:
                if s[i] == "?":
                    for each in words:
                        try:
                            if each != s[i+1]:
                                s[i] = each
                                break
                        except:
                            s[i] = each

            if i == len(s)-1:
                if s[i] == "?":
                    for each in words:
                        if each != s[i-1]:
                            s[i] = each
                            break

            if s[i] == "?":
                    for each in words:
                        if each != s[i+1] and each != s[i-1]:
                            s[i] = each
                            break


        return "".join(s)
            
            
        
