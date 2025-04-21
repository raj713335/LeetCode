# https://leetcode.com/problems/satisfiability-of-equality-equations/description/

# Time: O(N × α(N)), where N = number of equations, and α is the inverse Ackermann function.
# Space: O(1), fixed size array of 26 elements for lowercase letters.

class UnionFind:
    def __init__(self):
        self.parent = list(range(26))  # For 'a' to 'z'

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        uf = UnionFind()

        # First, handle "==" equations
        for eq in equations:
            if eq[1:3] == "==":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                uf.union(x, y)

        # Then, handle "!=" equations and check for conflicts
        for eq in equations:
            if eq[1:3] == "!=":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False

        return True
        
