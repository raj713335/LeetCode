# https://leetcode.com/problems/minimum-genetic-mutation/description/

from collections import deque  

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        mutation = ["A", "C", "G", "T"]

        q = deque()
        q.append([startGene, 0])

        visited = set()

        while q:

            gene, moves = q.popleft()

            if gene == endGene:
                return moves
                
            for i in range(0, 8):
                gene_mutate = list(gene)
                for m in mutation:
                    gene_mutate[i] = m
                    gene_mutate_str = "".join(gene_mutate)

                    if gene_mutate_str not in visited and gene_mutate_str in bank:
                        visited.add(gene_mutate_str)
                        q.append([gene_mutate_str, moves + 1])

        return -1
