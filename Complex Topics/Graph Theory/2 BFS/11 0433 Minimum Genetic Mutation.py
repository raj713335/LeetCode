# https://leetcode.com/problems/minimum-genetic-mutation/description/

import collections

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        q = deque()
        q.append((startGene, 0))

        visited = set()
        visited.add(startGene)

        mutations = ["A", "C", "G", "T"]  

        while q:

            gene, steps = q.popleft()

            if gene == endGene:
                return steps


            for i in range(0, 8):
                mutates_gene = gene
                for each in mutations:
                    mutates_gene = list(mutates_gene)
                    mutates_gene[i] = each
                    mutates_modified_gene = "".join(mutates_gene)
                    if mutates_modified_gene in bank and mutates_modified_gene not in visited:
                        visited.add(mutates_modified_gene)
                        q.append((mutates_modified_gene, steps + 1))

        return -1

