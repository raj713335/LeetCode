# https://leetcode.com/problems/similar-string-groups/description/

# O(N^2 * K) where N is number of strings, K is string length (to compare each pair).
# Union-Find can optimize the grouping, especially for large input.


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def is_similar(a, b):
            diff = [(x, y) for x, y in zip(a, b) if x != y]
            return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])

        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)

        roots = set(uf.find(i) for i in range(n))
        return len(roots)
            
