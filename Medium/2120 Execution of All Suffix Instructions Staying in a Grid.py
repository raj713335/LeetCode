# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        res = []

        for l in range(0, len(s)):
            count = 0
            i, j = startPos[0], startPos[1]
            for m in range(l, len(s)):
                if s[m] == "L":
                    if j - 1 >= 0:
                        j -= 1
                        count += 1
                    else:
                        break
                elif s[m] == "R":
                    if j + 1 < n:
                        j += 1
                        count += 1
                    else:
                        break
                elif s[m] == "U":
                    if i - 1 >= 0:
                        i -= 1
                        count += 1
                    else:
                        break
                else:
                    if i + 1 < n:
                        i += 1
                        count += 1
                    else:
                        break
                
            res.append(count)

        return res

        
