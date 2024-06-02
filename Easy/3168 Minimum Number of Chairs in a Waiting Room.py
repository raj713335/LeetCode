# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/


class Solution:
    def minimumChairs(self, s: str) -> int:

        stack = []

        max_count = 0

        for each in s:
            if each == "E":
                stack.append("E")
            else:
                stack.pop()

            val = len(stack)
            if val > max_count:
                max_count = val
        
        return max_count
        
