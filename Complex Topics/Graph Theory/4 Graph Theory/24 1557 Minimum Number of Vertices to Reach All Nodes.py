# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        reachable = set()
    
        for from_node, to_node in edges:
            reachable.add(to_node)
        
        result = []
        for i in range(n):
            if i not in reachable:
                result.append(i)
        
        return result
        
