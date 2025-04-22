# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        middle = len(stack) // 2

        stack = stack[:middle] + stack[middle+1:]

        for each in stack:
            curr.next = ListNode(each)
            curr = curr.next

        return dummy.next