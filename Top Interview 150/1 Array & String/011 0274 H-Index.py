# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def hIndex(self, citations: List[int]) -> int:


        citations = sorted(citations, reverse = True)

        for index, citation in enumerate(citations):
            if index >= citation:
                return index 

        return len(citations)
