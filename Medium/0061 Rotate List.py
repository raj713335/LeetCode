# https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        stack = []

        if head == None or k == 0:
            return head

        while head:
            val = head.val
            stack.append(val)
            head = head.next

        n = len(stack)
        rot =  n - k % n
        
        stack = stack[rot:] + stack[:rot]
        
        for each in stack:
            curr.next = ListNode(each)
            curr = curr.next

        return dummy.next
        
