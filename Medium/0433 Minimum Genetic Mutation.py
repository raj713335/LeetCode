# https://leetcode.com/problems/minimum-genetic-mutation/description/

import collections

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        gene_move = ["A", "C", "G", "T"]
        
        
        q = collections.deque()
        q.append([startGene, 0])

        visited = set()

        while q:
            gene, move = q.popleft()
            visited.add(gene)
            for i in range(0, 8):
                mutation_gene = gene
                for each in gene_move:
                    mutation_gene = list(mutation_gene)
                    mutation_gene[i] = each
                    mutation_gene = "".join(mutation_gene)
                    if mutation_gene in bank  and mutation_gene not in visited:
                        if mutation_gene == endGene:
                            return move + 1
                        q.append([mutation_gene, move+1])
        return -1

