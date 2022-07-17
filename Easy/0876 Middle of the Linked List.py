# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        current = head
        idx = 0
        
        while (current!=None):
            current = current.next
            idx += 1
            
        idx = idx//2
        cur = 0
            
        while head:
            if cur == idx:
                return head
            head = head.next
            cur += 1
            
        
