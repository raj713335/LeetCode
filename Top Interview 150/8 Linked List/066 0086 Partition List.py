# https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        lower = []
        higher = []

        while head:
            val = head.val
            if val < x:
                lower.append(val)
            else:
                higher.append(val)

            head = head.next
        
        for each in lower:
            curr.next = ListNode(each)
            curr = curr.next

        for each in higher:
            curr.next = ListNode(each)
            curr = curr.next
            
        return dummy.next
        
