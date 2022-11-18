# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/


class Solution:
    def makeFancyString(self, s: str) -> str:

        flag = True
        i = 0
        temp_count = 0
        last = ""
        ss = ""

        while flag:
            try:
                if last != s[i]:
                    temp_count = 1
                    last = s[i]
                    ss += s[i]
                    i += 1

                else:
                    temp_count += 1
                    if temp_count < 3:
                        ss += s[i]
                    i += 1
            except:
                return ss
                    
