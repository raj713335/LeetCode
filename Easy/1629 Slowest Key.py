# https://leetcode.com/problems/slowest-key/description/


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        res = []
        max_pressed = 0
        release = [releaseTimes[0]]

        for i in range(1, len(releaseTimes)):
            release.append(releaseTimes[i] - releaseTimes[i-1])

        for i in range(0, len(keysPressed)):
            if release[i] > max_pressed:
                res = [keysPressed[i]]
                max_pressed = release[i]
            elif release[i] == max_pressed:
                res.append(keysPressed[i])

        res = sorted(res, reverse = True)

        return res[0]
        
