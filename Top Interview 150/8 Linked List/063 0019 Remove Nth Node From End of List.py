# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        itr = 0
        stack = []

        while head:

            stack.append(head.val)
            head = head.next
            itr += 1

        remove_index = itr - n
        itr = 0
        
        for each in stack:
            if remove_index != itr:
                curr.next = ListNode(each)
                curr = curr.next
        
            itr += 1

        return dummy.next
        
