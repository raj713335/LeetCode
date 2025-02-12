# https://leetcode.com/problems/find-the-town-judge/description/


from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        edges_list = defaultdict(int)

        for trustee, trust in trust:
            edges_list[trust] += 1
            edges_list[trustee] -= 1


        for person in range(1, n+1):
            if edges_list[person] == n - 1:
                return person
        
        return -1
        


        