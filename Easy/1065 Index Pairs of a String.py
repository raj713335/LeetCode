# https://leetcode.com/problems/index-pairs-of-a-string/description/

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        ans = []

        for each in words:
            length = len(each)
            for i in range(0, len(text)-length+1):
                if text[i:i+length] == each:
                    ans.append([i, i+length-1])

        return sorted(ans)
        
