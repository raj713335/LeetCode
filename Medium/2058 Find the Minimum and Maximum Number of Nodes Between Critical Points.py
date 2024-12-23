# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/


import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        stack = []

        prev = head.val
        head = head.next

        curr = head.val
        j = 1
        head = head.next
        minDistance, maxDistance = math.inf, -1

        while head:

            if curr > prev and curr > head.val:
                try:
                    val = j - stack[-1]
                    if val > 0 and val < minDistance:
                        minDistance = val
                except:
                    pass
                stack.append(j)
            elif curr < prev and curr < head.val:
                try:
                    val = j - stack[-1]
                    if val > 0 and val < minDistance:
                        minDistance = val
                except:
                    pass
                stack.append(j)


            prev = curr
            curr = head.val
            j += 1

            head = head.next
        
        try:
            val = stack[-1] - stack[0]
            if val != 0:
                maxDistance = val
        except:
            pass

        if minDistance == math.inf:
            minDistance = -1

        return [minDistance, maxDistance]
        
