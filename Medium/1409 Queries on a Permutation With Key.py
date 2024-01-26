# https://leetcode.com/problems/queries-on-a-permutation-with-key/description/


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        res = []

        P = [x for x in range(1, m+1)]


        for i in range(0, len(queries)):
            for j in range(0, len(P)):
                if P[j] == queries[i]:
                    val = P[j]
                    del P[j]
                    P.insert(0, val)
                    res.append(j)
                    break

        return res
            
        
