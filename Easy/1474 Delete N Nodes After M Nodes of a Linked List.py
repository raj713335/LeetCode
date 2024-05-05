# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:

        root = head
        index = 0

        while head.next:
            index += 1
            if index % (m + n) < m:
                head = head.next
            else:
                head.next = head.next.next
            
        return root
        
