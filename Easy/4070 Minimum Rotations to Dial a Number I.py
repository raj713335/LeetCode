# https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/description/

class Solution:
    def minRotations(self, s: str) -> int:

        rotations = 0
        initial = 0

        for dial in s:
            dial = int(dial)
            forward = abs(dial-initial)
            backward = min(abs(9-initial) + dial, abs(initial) + abs(9-dial)) + 1

            if forward <= backward:
                rotations += forward
            else:
                rotations += backward

            initial = dial


        return rotations

        
