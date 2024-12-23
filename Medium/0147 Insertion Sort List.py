# https://leetcode.com/problems/insertion-sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        stack = []

        while head:
            val = head.val
            stack.append(val)
            head = head.next
        
        stack = sorted(stack)

        for each in stack:
            curr.next = ListNode(each)
            curr = curr.next

        return dummy.next
        
