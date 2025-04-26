# https://leetcode.com/problems/unit-conversion-i/description/

from collections import deque

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        
        MOD = 10**9 + 7


        n = max(max(u, v) for u, v, _ in conversions) + 1


        graph = defaultdict(list)
        for u, v, factor in conversions:
            graph[u].append((v, factor))


        baseConversion = [-1] * n
        baseConversion[0] = 1


        queue = deque([0])

        while queue:
            u = queue.popleft()
            for v, factor in graph[u]:
                if baseConversion[v] == -1:  # not visited
                    baseConversion[v] = baseConversion[u] * factor % MOD
                    queue.append(v)

        return baseConversion
        
