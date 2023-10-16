# https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:

        prev = -1
        index = -1

        arr = []
        res = []

        for i in range(0, len(words)):
            if words[i] != "prev":
                arr.append(words[i])
                index += 1
                prev = index
            else:
                if prev >= 0:
                    res.append(int(arr[prev]))
                    prev -= 1
                else:
                    res.append(-1)

        return res


        
