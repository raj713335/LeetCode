# https://leetcode.com/problems/remove-nodes-from-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        stack = []

        while head:
            val = head.val
            while stack and val > stack[-1]:
                stack.pop()
            
            stack.append(val)
            head = head.next 

        for each in stack:
            curr.next = ListNode(each)
            curr = curr.next

        return dummy.next
