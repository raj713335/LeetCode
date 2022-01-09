# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def make_num(link):
            if not link:
                return 0
            return link.val + 10 * make_num(link.next)
        
        def make_link(num):
            if not num:
                return None
            return ListNode(num % 10, make_link(num // 10))
			
        num = make_num(l1) + make_num(l2)
        if not num:
            return ListNode()
        return make_link(num)
        