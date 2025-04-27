# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
        

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        dsu = DSU(n)
    
        for i in range(n-1):
            if nums[i+1] - nums[i] <= maxDiff:
                dsu.union(i, i+1)

        answer = []
        for u, v in queries:
            answer.append(dsu.find(u) == dsu.find(v))

        return answer

        
