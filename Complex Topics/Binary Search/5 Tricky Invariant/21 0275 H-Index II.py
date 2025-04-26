# https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations = citations[::-1]

        for index, citation in enumerate(citations):
            if index >= citation:
                return index
        
        return len(citations)
        
