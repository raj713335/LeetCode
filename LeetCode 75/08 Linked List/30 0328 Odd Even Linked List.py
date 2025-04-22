# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dump = ListNode(0)
        dump.next = head
        # po, pe are the pointers pointing to odd and even nodes, respectively
        po, even = head, head.next
        pe = even
        
        while pe and pe.next:
            po.next = po.next.next
            po = po.next
            if pe.next.next:
                pe.next = pe.next.next
                pe = pe.next
            else:
                pe.next = None
                
        po.next = even
        return dump.next
