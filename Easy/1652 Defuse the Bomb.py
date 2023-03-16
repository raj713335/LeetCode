# https://leetcode.com/problems/defuse-the-bomb/


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        codex = code * 3
        n = len(code)

        res = []

        for i in range(0, len(code)):
            if k > 0:
                res.append(sum(codex[i+n+1:i+n+k+1]))
            elif k == 0:
                res.append(0)
            else:
                res.append(sum(codex[i+n+k:i+n]))
                
        return res



