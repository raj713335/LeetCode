# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_ptr = head
        slow_ptr = head
        fast = 0 
        slow = 0

        while (fast_ptr.next != None):   # fast pointer not at the end
            fast_ptr = fast_ptr.next
            fast += 1
            if (fast - slow > n):
                slow_ptr = slow_ptr.next
                slow += 1

        #case1 - the removal is at the head position
        #case 2: removal is in middlle
        if (fast - slow < n): 
            head = head.next
        else:
            slow_ptr.next = slow_ptr.next.next

        return head
        
