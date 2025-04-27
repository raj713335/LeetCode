# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

# Time: O(N + M), where N = len(s1), M = len(baseStr)
# Space: O(1) — because there are only 26 letters

class UnionFind:
    def __init__(self):
        self.parent = {} # For 'a' to 'z'

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        uf = UnionFind()
    
        for a, b in zip(s1, s2):
            uf.union(a, b)
        
        result = []
        for ch in baseStr:
            smallest = uf.find(ch)
            result.append(smallest)
        
        return ''.join(result)




class UnionFind:
    def __init__(self):
        self.parent = list(range(26))  # 'a' to 'z'

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        # Always keep the smaller one as the parent
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        uf = UnionFind()
    
        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        result = []
        for ch in baseStr:
            smallest = uf.find(ord(ch) - ord('a'))
            result.append(chr(smallest + ord('a')))
        
        return ''.join(result)
        
