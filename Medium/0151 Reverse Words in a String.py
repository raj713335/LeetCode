# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        
        output = []
        s = s.strip().split(" ")
        
        print(s)
        
        for each in s:
            if each != "":
                output.append(each)
        
        return " ".join(output[::-1])
        
