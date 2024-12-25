# https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        
        while head:
            stack = []
            balance = k
            length = 0
            while head and balance > 0:
                
                stack.append(head.val)
                head = head.next
                length += 1
                balance -= 1
                
            if len(stack) == k:
                for each in stack[::-1]:
                    curr.next = ListNode(each)
                    curr = curr.next
            else:
                for each in stack:
                    curr.next = ListNode(each)
                    curr = curr.next

        return dummy.next
        
