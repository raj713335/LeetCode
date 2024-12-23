# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        index = 1
        stack = []

        while head and index < left:
            curr.next = ListNode(head.val)
            curr = curr.next
            head = head.next

            index += 1
        
        while index <= right:
            stack.append(head.val)
            head = head.next

            index += 1

        for each in stack[::-1]:
            curr.next = ListNode(each)
            curr = curr.next

        while head:
            curr.next = ListNode(head.val)
            curr = curr.next
            head = head.next
        
        return dummy.next
