# https://leetcode.com/problems/linked-list-cycle-ii/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast, entry = head, head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                while(slow!=entry):
                    slow = slow.next
                    entry = entry.next
                return entry

        return None
