# https://leetcode.com/problems/winner-of-the-linked-list-game/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:

        even = 0
        odd = 0

        index = 1
        prev = head.val
        head = head.next

        while head:

            if index % 2 == 0:
                prev = head.val
            else:
                new = head.val
                if new > prev:
                    odd += 1
                else:
                    even += 1

            head = head.next
            index += 1

        if even > odd:
            return("Even")
        elif even < odd:
            return("Odd")
        else:
            return("Tie")

