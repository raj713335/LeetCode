# https://leetcode.com/problems/next-greater-node-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        stack = []

        while head:
            val = head.val
            next_val = 0

            dummy = head

            while dummy:
                if dummy.val > val:
                    next_val = dummy.val
                    break
                
                dummy = dummy.next

            head = head.next
            stack.append(next_val)

        return stack
