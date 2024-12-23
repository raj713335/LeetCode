# https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        stack = [[] for i in range(0, k)]
        count = 0

        head1 = head

        while head:
            val = head.val
            stack[count%k].append(val)
            head = head.next
            
            count += 1

        res = []

        for nested in stack:
            dummy = ListNode()
            curr = dummy

            for each in nested:
                curr.next = ListNode(head1.val)
                curr = curr.next
                head1 = head1.next

            res.append(dummy.next)

        return res
        
